###############################################################################
# Imports
###############################################################################
from collections import Counter
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pymupdf
import re
import sys

import SubScripts.AuthorsChecker as ac
import SubScripts.RankingChecker as ran_c
import SubScripts.ReferenceChecker as ref_c
import SubScripts.RefIntextChecker as rit_c
import SubScripts.UnicodeChecker as uc



###############################################################################
# INFO
###############################################################################

# NOTE: To save the results as .md file you'll need to habe the 'tabulate' 
#       package installed



###############################################################################
# Gloal Variables
###############################################################################

# 'headings' contains thruples of (number, text, page_no) for each heading 
#    found in the document; the number is 'R' for the references section
headings = []
# 'references_starting_page_no' is the page number where the references section
#    starts; it is 0 if no references section was found
references_starting_page_no = 0
# 'references_ending_page_no' is the page number where the references section
#    ends; it is 0 if no references section was found
references_ending_page_no = 0
heading_after_references = ""
# 'unicode_counter' counts the occurences of different Unicode chars like 
#    apostrophes, quotes, and dashes in the document
unicode_counter = Counter()
# 'unicode_lines' is a list of four lists, where the inner lists contain tuples
#    of (line: str, page_no: int) of their respective occurences
#   [0] lines with Unicode apostrophes, 
#   [1] lines with Unicode quotes,
#   [2] lines with Unicode dashes,
#   [3] lines with Unicode non-breakingspaces
unicode_lines = [[], [], [], []]

# Paper template - formatting specifications
springer_formatting_template = {
    # Always skip first two lines in the springer template as they are: 
    #   page_lines[0] = Shortitle/Author; page_lines[1] = page number
    "name": "springer",
    "header_lines": 2,
    "footer_lines": 0
}
acm_formatting_template = {
    "name": "acm",
    "header_lines": 0,
    "footer_lines": 2
}

# Formatting template to use for parsing
# NOTE: These are only used in this file by the "check_document_structure" function
supported_formatting_templates = [springer_formatting_template, acm_formatting_template]
formatting_template = ""

# Bibliography template to use for parsing
# NOTE: These are used in the AuthorChecker and the ReferenceChecker
supported_bib_layouts = ref_c.get_supported_bib_templates()
bib_template = ""

# Referencing template to use for parsing
# NOTE: These are used in the ReferenceChecker
supported_referencing_templates = rit_c.get_supported_ref_templates()
referencing_template = ""




###############################################################################
# Helper functions
###############################################################################

def get_letter_pos_in_alphabet(letter: str) -> int:
    if len(letter) == 1:
        return ord(letter.lower()) - 96
    else:
        print(f"-> Warning: The given string '{letter}' is not a single char!")
        return -1
    

def parse_numbered_headings(page_no: int, page_lines: list, line_index: int, \
                            headings: list) -> list:
    """
    parse_numbered_headings checks for lines with only a number in it
    assesses if the number is the last heading's number +1, and if so,
    appends the *next* line (where the title should be) to the
    headings list.

    Returns:
      - The updated headings list
    """
    
    global references_starting_page_no
    global references_ending_page_no
    global heading_after_references

    line = page_lines[line_index].strip()

    if len(line) <= 2:

        heading_match = re.match(r'^(?:[1-9]|[1-9]\d)$', line)
        if heading_match:
            number = heading_match.group(0)

            # Check if the current line is not the last, and
            #       if the next line is non-empty & not only numerical
            if line_index + 1 < len(page_lines) and page_lines[line_index + 1] \
                and not page_lines[line_index + 1].strip().isdigit():
                # If this is not the first heading found
                if len(headings) > 0:
                    last_index = len(headings) - 1
                    last_heading_no = headings[last_index][0]
                    text = page_lines[line_index + 1].strip()

                    # If the parsed heading number matches the last found heading's number +1
                    if references_starting_page_no == 0 \
                        and str(int(number.strip())-1) == last_heading_no \
                        and text[0].isupper():
                        print(f"- Found following heading '{number} - {text}' on page {page_no + 1}")
                        headings.append((number, text, page_no + 1))
                    # If the parsed heading number does NOT match
                    # -> Might be the case for sections after the References section
                    elif references_starting_page_no > 0 \
                        and (str(int(number.strip())-1) == last_heading_no
                            or number.strip() == last_heading_no) \
                        and text[0].isupper():
                        print(f"- Found heading after References '{number} - {text}' on page {page_no + 1}")
                        headings.append((number, text, page_no + 1))

                        # Only update the references_ending_page_no for the first heading
                        # after the reference section
                        if references_ending_page_no == 0:
                            references_ending_page_no = page_no + 1
                            heading_after_references = text
                # If this is the first heading found
                else:
                    text = page_lines[line_index + 1].strip()
                    print(f"- Found first heading '{number} - {text}' on page {page_no + 1}")
                    headings.append((number, text, page_no + 1))
                    
        # Check for Apendix match
        elif len(line) == 1 and references_starting_page_no > 0 \
            and not line.isdigit() and line.isupper():

            # Get the numerical representation of that letter
            num = get_letter_pos_in_alphabet(line)

            # Check if this would be the first section after References
            if len(headings) > 0:
                last_index = len(headings) - 1
                last_heading_no = headings[last_index][0]
                text = page_lines[line_index + 1].strip()

                if isinstance(last_heading_no, int) or str(last_heading_no).isdigit():
                    # Match 'A'
                    if line == "A":
                        print(f"- Found first appendix '{line} - {text}' on page {page_no + 1}")
                        headings.append((line, text, page_no + 1))

                        # Only update the references_ending_page_no for the first heading
                        # after the reference section
                        if references_ending_page_no == 0:
                            references_ending_page_no = page_no + 1
                            heading_after_references = text

                else:
                    # Check if this is the next letter
                    last_num = get_letter_pos_in_alphabet(last_heading_no)
                    if last_num+1 == num:
                        print(f"- Found following appendix '{line} - {text}' on page {page_no + 1}")
                        headings.append((line, text, page_no + 1))

                        # Only update the references_ending_page_no for the first heading
                        # after the reference section
                        if references_ending_page_no == 0:
                            references_ending_page_no = page_no + 1
                            heading_after_references = text

        
    # Check for "References" or "Literature" (case-insensitive)
    elif line.lower() in ["references", "literature"]:
        print(f"=> Found references/literature section on page {page_no + 1}")
        last_number = int(headings[len(headings)-1][0])
        headings.append((str(last_number + 1), line, page_no + 1))
        references_starting_page_no = page_no + 1
    
    return headings


def parse_unnumbered_headings(page_no: int, line: str, headings: list) -> list:
    """
    parse_unnumbered_headings checks lines for common heading titles

    Returns:
      - The updated headings list
    """

    global references_starting_page_no

    line_lower = line.lower()
    if line_lower in ["related work", "related works",
                      "background", "literature review",
                      "background and literature review",
                      "problem definition", "research questions",
                      "problem definition and research questions"
                      "methods", "methodology",
                      "research agenda", "survey", "survey methods",
                      "data", "data and methods",
                      "implementation", "implementation details", 
                      "experiments", "experimental setup", "case studies",
                      "experimental setup and case studies",
                      "results", "results and analysis",
                      "discussion", "discussion and conclusion",
                      "discussion and future work",
                      "limitations", "limitations and future work",
                      "implications", "theoretical implications",
                      "practical relevance",
                      "conclusion", "future work",
                      "conclusion and future work",
                      "conclusion, limitations, and future work",
                      "ethical statement", "positionality statement",
                      "broader impact", "acknowledgments"
                     ]:

        print(f"- Found {line} on page {page_no + 1}")
        headings.append((len(headings)+1, line, page_no + 1))
    
    # Check for "References" or "Literature" (case-insensitive)
    elif line_lower in ["references", "literature"]:
        print(f"=> Found references/literature section on page {page_no + 1}")
        headings.append((len(headings)+1, line, page_no + 1))
        references_starting_page_no = page_no + 1
    
    return headings


def check_document_structure(doc):
    global formatting_template
    global supported_formatting_templates
    global headings
    global references_starting_page_no
    global references_ending_page_no
    global unicode_counter
    global unicode_lines

    print("##########################################################")
    print("# Starting Structure Check")
    print("##########################################################")

    #==========================================================================
    # Check template and get specifics
    #==========================================================================
    lineskip = 0
    for template in supported_formatting_templates:
        if template['name'] == formatting_template:
            lineskip = template["header_lines"]
    
    numbered_headings = 2
    
    #==========================================================================
    # Iterate pages AND per page all lines
    #==========================================================================
    # NOTE: doc[page_number] is 0-based
    for page_no in range(0, doc.page_count):
        page_text = doc[page_no].get_text()

        # Replace "-\n" with nothing to remove obvious mid-sentence line breaks
        page_text = page_text.replace("-\n", "")

        # Iterate over all page lines to check headings and find the refrences
        page_lines = page_text.split("\n")

        # NOTE: Lineskip for headers is template-specific
        for line_index in range(lineskip, len(page_lines)):
            line = page_lines[line_index].strip()
            
            #==================================================================
            # Check Unicode characters
            #==================================================================
            line_counter = uc.count_occurences(line)
            unicode_counter.update(line_counter)

            # If any of the Unicode chars were found:
            if line_counter:                
                # Extend unicode_lines respectivly
                temp_unicode_lines = uc.get_unicode_line_lists(line, page_no)
                unicode_lines = [a + b for a, b in zip(unicode_lines, temp_unicode_lines)]


            #==================================================================
            # Check line for headings
            #==================================================================

            # First, find the introduction (every paper has it), and check if
            # the headings are numbered or not
            if line_index > 0 and numbered_headings == 2:
                if "Introduction" in line:

                    # If the there is nothing prefixing "Introduction"
                    if line.find("Introduction") == 0:
                        previous_line = page_lines[line_index-1].strip()
                        heading_match = re.match(r'^(?:[1-9]|[1-9]\d)$', previous_line)
                        if heading_match:
                            number = heading_match.group(0)
                            numbered_headings = 1
                            print(f"- Found {line} on page {page_no + 1}")
                            headings.append((str(number), line, page_no + 1))
                        else:
                            numbered_headings = 0
                    else:
                        prefix = line[0:line.find("Introduction")]
                        if prefix.strip().isdigit():
                            # TODO: Numberes are in the same line as the heading!!
                            print(f"=> Error: Inline numbered headings are not supported yet!")
                            print(" -> The programm will exit now. :)")
                            sys.exit(0)

            # If the headings are numbered
            elif numbered_headings == 1:
                headings = parse_numbered_headings(page_no, page_lines, \
                                                   line_index, headings)
            
            # If the headings are not numbered
            elif numbered_headings == 0:
                headings = parse_unnumbered_headings(page_no, line, headings)
            
            #if references_starting_page_no != 0:
            #    return

        page_no += 1
    
    if references_ending_page_no == 0:
        references_ending_page_no = doc.page_count



###############################################################################
# Main code
###############################################################################

def main():
    """
    x
    """
    global supported_formatting_templates
    global formatting_template
    global supported_bib_layouts
    global bib_template
    global supported_referencing_templates
    global referencing_template

    global headings
    global references_starting_page_no
    global references_ending_page_no
    global heading_after_references
    global unicode_lines


    #==========================================================================
    # Get Input Infos
    #==========================================================================
    path_to_pdf = input("Enter the path to the PDF file: ").strip().strip('"')
    lineskip = 0

    print("---")
    print("INFO:")
    print(" - 'springer' = Has two headerlines to skip (1st = Shortitle/Author; 2nd = page number)")
    print(" - 'acm'      = Has no headerlines to skip")
    input_formatting_template = input(f"Enter a supported formatting template ({[t['name'] for t in supported_formatting_templates]}): ").strip().strip('"')
    res = next((ft for ft in supported_formatting_templates if ft['name'] == input_formatting_template), None)
    if not res:
        print(f"ERROR: Formatting template '{input_formatting_template}' not supported yet!")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        formatting_template = input_formatting_template
        for form_temp in supported_formatting_templates:
            if form_temp['name'] == input_formatting_template:
                lineskip = form_temp['header_lines']
    
    print("---")
    print("INFO:")
    print(" - 'LFflTOY' = Lastname, Firstname (firstletter), Title, Outlet, Year")
    print("            -> This is, for example, used by Springer Nature")
    print(" - 'LFflYTO' = Lastname, Firstname (firstletter), Year, Title, Outlet")
    print("            -> This is, for example, used by the AAAI/ACM Conference")
    print(" - 'FLYTO'   = Firstname, Lastname, Year, Title, Outlet")
    print("            -> This is, for example, used by ACM")
    print(" - 'FLTOY'  = Firstname, Lastname, Title, Outlet, Year")
    print("            -> This is, for example, used by the NeurIPS Conference")
    input_bib_layout = input(f"Enter a supported bibliography layout ({[t['name'] for t in supported_bib_layouts]}): ").strip().strip('"')
    res = next((bt for bt in supported_bib_layouts if bt['name'] == input_bib_layout), None)
    if not res:
        print(f"ERROR: Biblography layout '{input_bib_layout}' not supported yet!")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        bib_template = input_bib_layout
        ref_c.set_given_bib_layout(input_bib_layout, lineskip)
    
    print("---")
    print("INFO:")
    print(" - 'natbib'           = No numbering; reference in 'References' section starts with the authors' names")
    print(" - 'numbered_squares' = Reference in 'References' section starts with, e.g., '[1]'")
    print(" - 'number_with_dot'  = Reference in 'References' section starts with, e.g., '1.'")
    supported_bib_numberings = ref_c.get_supported_bib_numberings()
    input_bib_numbering = input(f"Enter a supported bibliography numbering ({[t['name'] for t in supported_bib_numberings]}): ").strip().strip('"')
    res = next((bt for bt in supported_bib_numberings if bt['name'] == input_bib_numbering), None)
    if not res:
        print(f"ERROR: Biblography numbering '{input_bib_layout}' not supported yet!")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        ref_c.set_given_given_bib_numbering(input_bib_numbering)

    print("---")
    print("INFO:")
    print(" - 'numeric'           = A number placed inside square brackets (e.g., [28])")
    print("                      -> Multiple references are separated by a comma (e.g., [28,29])")
    print(" - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Speckmann et al., 2025))")
    print("                      -> Multiple references are separated by a semicolon (e.g., (Speckmann et al. 2025; Janiesch et al. 2021))")
    print("                      -> Please note that the author and year are *not* separated")
    print(" - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Speckmann et al., 2025])")
    print("                      -> Multiple references are separated by a comma (e.g., [Speckmann et al., 2025, Janiesch et al., 2021])")
    print("                      -> Please note that the author and year are also separated by a comma")
    input_ref_template = input(f"Enter a supported referencing template ({[t['name'] for t in supported_referencing_templates]}): ").strip().strip('"')
    res = next((rt for rt in supported_referencing_templates if rt['name'] == input_ref_template), None)
    if not res:
        print(f"ERROR: Referencing template '{input_ref_template}' not supported yet!")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        referencing_template = input_ref_template
        rit_c.set_given_ref_style(input_ref_template)


    #==========================================================================
    # Read input PDF
    #==========================================================================
    doc = pymupdf.open(path_to_pdf, filetype="txt")
    check_document_structure(doc)


    #==========================================================================
    # Extract and check references
    #==========================================================================
    # NOTE: Check out ref_c.main() doc. for details on the dict's ('ref_stats') keys
    ref_stats = {}
    # NOTE: 'entries' is a list of three lists: 
    #       [invalid_link_entries, mismatching_entries, unfound_entries]
    entries = [[], [], []]

    if references_starting_page_no <= 0:
        print("ERROR: No references section found in the document.")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        global references_df
        references_df, ref_stats, entries = ref_c.main(doc, references_starting_page_no, references_ending_page_no, heading_after_references)
    
    extracted_references = references_df.drop('full_reference', axis=1)

    TOTAL_NO_OF_REFERENCES = ref_stats["total_no_of_references"]
    invalid_entries = entries[0]
    mismatching_entries = entries[1]
    unfound_entries = entries[2]


    #==========================================================================
    # Check paper quality:
    #==========================================================================
    # Check the uniformity of used chars like apostrophes, quotes, and dashes
    invalid_unicode_lines, unicode_stats = uc.check_if_unicode_is_sus(unicode_lines)
    total_no_of_nonbreaking_spaces = unicode_stats["valid_nonbreaking_spaces"] + unicode_stats["invalid_nonbreaking_spaces"]
    total_no_of_minus_signs = unicode_stats["valid_minus_sign_uses"] + unicode_stats["invalid_minus_sign_uses"]
    
    # Sanity Check
    #if not unicode_counter['\u00A0'] == total_no_of_nonbreaking_spaces:
    #    print(f"WARNING: The unicode_stats counted {total_no_of_nonbreaking_spaces} which is not equal to the unicode_counter's count.")

    # Check if all references used in the text are also listed in the references
    sentences_and_ref_df_indexes, sentences_with_unfound_refs = rit_c.compare_intext_references_to_bib(doc, references_starting_page_no, extracted_references, referencing_template)
    
    # Check if all references support the statements made in the paper
    # -> ref_and_sentences_df['sentences'] contains a list of tuples of the form (sentence, thematically related/relevant: bool, stance: str)
    # -> if stance = "unknown", that it wasn't checked by the LLM due to a missing abstract
    # -> TODO: List them!
    ref_and_sentences_df = rit_c.validate_sentence_references(references_df, sentences_and_ref_df_indexes)
    related_statements, unrelated_statements = rit_c.get_statement_relevance_dicts(ref_and_sentences_df, references_df)
    
    # Check the references rankings
    outlets_df = ran_c.main(extracted_references)


    #==========================================================================
    # Check how often an author appears in the references
    #==========================================================================
    # NOTE: This dict is unsorted
    frequent_authors = ac.get_frequent_authors(references_df)


    #==========================================================================
    # RESULTS
    #==========================================================================
    # NOTE: Results will be saved in the same folder as the input PDF
    #       with the name "PQC_results.md"
    results_folder_dir = os.path.dirname(path_to_pdf)


    #--------------------------------------------------------------------------
    # Create Pie Chart with the literature validation results
    #--------------------------------------------------------------------------
    link_labels = ['No link provided', 'Unchecked links', 'Valid links', 'Invalid links', 'Mismatching links']
    link_values = [ref_stats["no_link_provided"], ref_stats["unchecked_links"], ref_stats["valid_links"], ref_stats["invalid_links"], ref_stats["different_links"]]
    
    searches_labels = ['Skipped searches', 'Successful searches', 'Mismatching infos', 'NO ENTRY FOUND']
    searches_values = [ref_stats["skipped_searches"], ref_stats['successful_searches'], ref_stats["mismatching_infos"], ref_stats["no_entry_found"]]

    # Create subplots: use 'domain' type for Pie subplot
    lit_fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    lit_fig.add_trace(go.Pie(labels=link_labels, values=link_values, name="Links"),
                1, 1)
    lit_fig.add_trace(go.Pie(labels=searches_labels, values=searches_values, name="Searches"),
                1, 2)

    # Use `hole` to create a donut-like pie chart
    lit_fig.update_traces(hole=.4)

    lit_fig.update_layout(
        title_text="Literature Search Results",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Links', x=sum(lit_fig.get_subplot(1, 1).x) / 2, y=0.5,
                        font_size=20, showarrow=False, xanchor="center"),
                    dict(text='Searches', x=sum(lit_fig.get_subplot(1, 2).x) / 2, y=0.5,
                        font_size=20, showarrow=False, xanchor="center")])
    literature_validation_results_fig_path = os.path.join(results_folder_dir, "literature_validation_results_fig.jpg")
    lit_fig.write_image(literature_validation_results_fig_path)


    #--------------------------------------------------------------------------
    # Create Pie Chart with the outlet ranking results
    #--------------------------------------------------------------------------
    rating_labels = ['A+', 'A', 'B', 'C', 'D', 'unkonwn']
    jq_rating = [len(outlets_df[outlets_df["jq_ranking"] == 'A+']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'A']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'B']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'C']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'D']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'unknown'])
                ]
    core_rating_values = [len(outlets_df[outlets_df["core_ranking"] == 'A*']), \
                          len(outlets_df[outlets_df["core_ranking"] == 'A']), \
                          len(outlets_df[outlets_df["core_ranking"] == 'B']), \
                          len(outlets_df[outlets_df["core_ranking"] == 'C']), \
                          len(outlets_df[outlets_df["core_ranking"] == 'D']), \
                          len(outlets_df[outlets_df["core_ranking"] == 'unknown'])
                         ]

    # Create subplots: use 'domain' type for Pie subplot
    rank_fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    rank_fig.add_trace(go.Pie(labels=rating_labels, values=jq_rating, name="JQ Ranking"),
                1, 1)
    rank_fig.add_trace(go.Pie(labels=rating_labels, values=core_rating_values, name="CORE Ranking"),
                1, 2)

    # Use `hole` to create a donut-like pie chart
    rank_fig.update_traces(hole=.4)

    rank_fig.update_layout(
        title_text="Outlet Ranking Results",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='JQ', x=sum(rank_fig.get_subplot(1, 1).x) / 2, y=0.5,
                        font_size=20, showarrow=False, xanchor="center"),
                    dict(text='CORE', x=sum(rank_fig.get_subplot(1, 2).x) / 2, y=0.5,
                        font_size=20, showarrow=False, xanchor="center")])
    ranking_results_fig_path = os.path.join(results_folder_dir, "ranking_results_fig.jpg")
    rank_fig.write_image(ranking_results_fig_path)


    #--------------------------------------------------------------------------
    # Log results into a markdown file
    #--------------------------------------------------------------------------
    results_path = os.path.join(results_folder_dir, "PQC_results.md")

    with open(results_path, "x", encoding="utf-8") as f:
        f.write("# Paper Quality Check Results\n\n")
        f.write(os.path.basename(path_to_pdf).split('/')[-1])
        f.write("\n\n\n")

        f.write("## Document Structure\n\n")
        if not headings:
            f.write("No headings found in the document.\n\n\n")
        else:
            for number, text, page_no in headings:
                f.write(f"{number}) '{text}' -- p. {page_no}\n")
        
        # Print Unicode Checker results
        f.write("\n## Unicode Character Usage\n\n")
        if all(not sublist for sublist in invalid_unicode_lines):
            f.write("No invalid seeming Unicode characters found in the document.\n\n")
        else:
            # TODO: Extend for other Unicode lists
            if invalid_unicode_lines[2]:
                f.write("Dashes:\n")
                f.write("- Stats for minus signs ():\n")
                f.write(f"	- Valid uses: {unicode_stats['valid_minus_sign_uses']}/{total_no_of_minus_signs}={unicode_stats['valid_minus_sign_uses']/total_no_of_minus_signs*100:.2f}%\n")
                f.write(f"	- Invalid uses: {unicode_stats['invalid_minus_sign_uses']}/{total_no_of_minus_signs}={unicode_stats['invalid_minus_sign_uses']/total_no_of_minus_signs*100:.2f}%\n")
                f.write("- Sentences with invalid dahes:\n")
                f.write("	- Lines containing invalid dashes:\n")
                for line, page_no in invalid_unicode_lines[2]:
                    f.write(f"		- Page {page_no}: {line}\n")
            if invalid_unicode_lines[3]:
                f.write("Non-breaking spaces:\n")
                f.write("- Stats:\n")
                f.write(f"  - Valid uses: {unicode_stats['valid_nonbreaking_spaces']}/{total_no_of_nonbreaking_spaces}={unicode_stats['valid_nonbreaking_spaces']/total_no_of_nonbreaking_spaces*100:.2f}%\n")
                f.write(f"  - Invalid uses: {unicode_stats['invalid_nonbreaking_spaces']}/{total_no_of_nonbreaking_spaces}={unicode_stats['invalid_nonbreaking_spaces']/total_no_of_nonbreaking_spaces*100:.2f}%\n")
                f.write("	- Lines containing invalid non-breaking spaces:\n")
                for line, page_no in invalid_unicode_lines[3]:
                    f.write(f"		- Page {page_no}: {line}\n")
            f.write("\n")
        
        # Print RefIntextChecker results
        f.write("\n## References not in Bibliography\n\n")
        if len(sentences_with_unfound_refs) == 0:
            f.write(f"All references used in the document's text were also found in the 'References' section.\n\n")
        else:
            f.write("*The sentences listed below contain references that were not found in the 'References' section*\n")
            f.write("*Please note that this list may contain false positives as, e.g., the content of a normal bracket might have been mistaken for a reference, ")
            f.write("or a natural reference (Authorname in text and year in brackets) might have been mismatched:*\n")
            for sen in sentences_with_unfound_refs:
                f.write(f"- {sen}\n")
            f.write("\n\n")

        # Print frequently referenced authors sorted by value (count) descending
        f.write("\n## Frequently Referenced Authors\n\n")
        for author, count in sorted(
            frequent_authors.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            f.write(f"- {author}: {count}\n")
        
        # Print Reference Checker results        
        f.write("\n## Reference Checker Results\n\n")
        if references_starting_page_no <= 0:
            f.write("No references section found in the document.\n")
        else:
            f.write(f"References section starts on page {references_starting_page_no}.\n\n")
            f.write(f"- No link provided: ${ref_stats['no_link_provided']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['no_link_provided']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            f.write(f"- Unchecked links: ${ref_stats['unchecked_links']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['unchecked_links']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            f.write(f"- Valid links: ${ref_stats['valid_links']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['valid_links']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            f.write(f"- Mismatching links: ${ref_stats['different_links']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['different_links']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            f.write(f"- Invalid link: ${ref_stats['invalid_links']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['invalid_links']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            if invalid_entries:
                f.write("	- Invalid entries:\n")
                for entry in invalid_entries:
                    entry_no_sb = entry.replace("[", "\[").replace("]", "\]")
                    f.write(f"		- {entry_no_sb}\n")
            f.write("\n")
            f.write(f"- Successful searches: ${ref_stats['successful_searches']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['successful_searches']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            f.write(f"- Skipped searches: ${ref_stats['skipped_searches']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['skipped_searches']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            f.write(f"- Mismatching infos: ${ref_stats['mismatching_infos']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['mismatching_infos']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            if mismatching_entries:
                f.write("	- Mismatching entries:\n")
                for entry in mismatching_entries:
                    entry_no_sb = entry.replace("[", "\[").replace("]", "\]")
                    f.write(f"		- {entry_no_sb}\n")
            f.write(f"- No entry found: ${ref_stats['no_entry_found']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['no_entry_found']/TOTAL_NO_OF_REFERENCES*100:.2f}\%$\n")
            if unfound_entries:
                f.write("	- Unfound entries:\n")
                for entry in unfound_entries:
                    entry_no_sb = entry.replace("[", "\[").replace("]", "\]")
                    f.write(f"		- {entry_no_sb}\n")
            f.write("\n")
            f.write(f"![References Validation Results]({literature_validation_results_fig_path})")
            f.write("\n\n")

        f.write("\n## References Support for Statements\n\n")
        f.write("*Please note that only references with a retrieved abstract can be checked here.*\n")
        f.write("*You can find a complete list, including which sentences were skipped due to a missing abstract, at the bottom of the report.*\n")
        f.write("\n")
        f.write("Thematically related / relevant papers that refute the sentence they are referenced in:\n")
        if len(related_statements['refuted']) > 0:
            for tuple in related_statements['refuted']:
                # [0] = sentence
                f.write(f"- '{tuple[0]}'\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")
        f.write("\n")
        f.write("Thematically unrelated / irrelevant papers:\n")
        if len(unrelated_statements['refuted']) > 0 \
            or len(unrelated_statements['not_enough_info']) > 0 \
            or len(unrelated_statements['supported']) > 0:
            for tuple in unrelated_statements['refuted']:
                # [0] = sentence
                f.write(f"- '{tuple[0]}'\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
            for tuple in unrelated_statements['not_enough_info']:
                # [0] = sentence
                f.write(f"- '{tuple[0]}'\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
            for tuple in unrelated_statements['supported']:
                # [0] = sentence
                f.write(f"- '{tuple[0]}'\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")
        f.write("\n\n\n")
        f.write("---")
        
        # Print the rankings of the outlets
        f.write("\n## Outlet Rankings\n\n")
        f.write("### References and Their Rankings\n\n")
        for i, row in outlets_df.iterrows():
            # outlets_df layout: 0=index, 1=parsed_name, 2=outlet_name, 3=jq_ranking,
            #                    4=core_ranking, 5=impact_factor, 6=references_count
            if row['outlet_name'] and row['outlet_name'] != "unknown":
                f.write(f"- {row['outlet_name']}\n")
                f.write(f"	- Parsed as: {row['parsed_name']}\n")
            else:
                f.write(f"- {row['parsed_name']}\n")
            if row['jq_ranking'] and row['jq_ranking'] != "unknown":
                f.write(f"	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = {row['jq_ranking']}\n")
            if row['core_ranking'] and row['core_ranking'] != "unknown":
                f.write(f"	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = {row['core_ranking']}\n")
            if row['impact_factor'] and row['impact_factor'] != "unknown":
                f.write(f"	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = {row['impact_factor']}\n")
            f.write(f"	- References literatures count from this outlet: {row['references_count']}\n")
        f.write("\n")
        f.write("### Outlet Ranking Results\n\n")
        f.write(f"![Outlet Ranking Results]({ranking_results_fig_path})")
        f.write("\n\n")

        f.write("---")
        # Print the references DF using df.to_markdown(tablefmt="grid")
        f.write("\n## Extracted References\n\n")
        for index, row in extracted_references.iterrows():
            f.write(f"- Number {index + 1}:\n")
            f.write(f"	- Ref. ID: *{row['ref_id']}*\n")
            f.write(f"	- Authors: *{row['authors']}*\n")
            f.write(f"	- Title: *{row['title']}*\n")
            f.write(f"	- Year: *{row['year']}*\n")
            f.write(f"	- Outlet: *{row['outlet']}*\n")
            f.write(f"	- Link: *{row['link']}*\n")
            f.write(f"	- **Valid?**: *{row['valid']}*\n")
        f.write("\n\n\n")
        
        f.write("---")
        f.write("\n## Full List of Reference Support Check\n\n")
        f.write("Thematically related / relevant papers that refute the sentence they are referenced in:\n")
        if len(related_statements['refuted']) > 0:
            for tuple in related_statements['refuted']:
                # [0] = sentence
                f.write(f"- '{tuple[0]}'\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")
        f.write("Thematically related / relevant papers that we had not enough info about:\n")
        if len(related_statements['not_enough_info']) > 0:
            for tuple in related_statements['not_enough_info']:
                # [0] = sentence
                f.write(f"- '{tuple[0]}'\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")
        f.write("Thematically related / relevant papers that support the sentence they are referenced in:\n")
        if len(related_statements['supported']) > 0:
            for tuple in related_statements['supported']:
                # [0] = sentence
                f.write(f"- '{tuple[0]}'\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")

        f.write("\n")

        f.write("Thematically unrelated / irrelevant papers that refute the sentence they are referenced in:\n")
        if len(unrelated_statements['refuted']) > 0:
            for tuple in unrelated_statements['refuted']:
                # [0] = sentence
                f.write(f"- {tuple[0]}\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")
        f.write("Thematically unrelated / irrelevant papers that we had not enough info about:\n")
        if len(unrelated_statements['not_enough_info']) > 0:
            for tuple in unrelated_statements['not_enough_info']:
                # [0] = sentence
                f.write(f"- {tuple[0]}\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")
        f.write("Thematically unrelated / irrelevant papers that support the sentence they are referenced in:\n")
        if len(unrelated_statements['supported']) > 0:
            for tuple in unrelated_statements['supported']:
                # [0] = sentence
                f.write(f"- {tuple[0]}\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")

        f.write("\n")

        f.write("Papers that we didn't have an abstract for to check against:\n")
        if len(related_statements['unknown']) > 0 or len(unrelated_statements['unknown']) > 0:
            for tuple in related_statements['unknown']:
                # [0] = sentence
                f.write(f"- '{tuple[0]}'\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
            for tuple in unrelated_statements['unknown']:
                # [0] = sentence
                f.write(f"- {tuple[0]}\n")
                f.write(f"	- Ref. ID: {tuple[3]}\n")
        else:
            f.write(f"- None\n")
        f.write("\n\n\n")
    
    print("---")
    print("FINISHED!")
    print(f" -> Results saved to {results_path}")



###############################################################################
# Run Main
###############################################################################
if __name__ == "__main__":
    main()