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
import SubScripts.UnicodeChecker as uc



###############################################################################
# INFO
###############################################################################

# NOTE: To save the results as .md file you'll need to habe the 'tabulate' 
#       package installed

# TODOs:
# - Paper Quality:
#    + Check the uniformity of used chars like apostrophes, quotes, and dashes
#    + Check if references match the statement they are supposed to support
#        (e.g., by checking the abstract on Scholar)
#    + Sind alle Referenzen im Text auch im Literaturverzeichnis hinterlegt??
#        + Ist die Referenzierung sinnvoll (zB nur a und b hinter einem Jahr, 
#          wenn auch zwei Paper vom Auhtor aus dem, selben jahr zitiert werden)?



###############################################################################
# Gloal Variables
###############################################################################

# 'headings' contains thruples of (number, text, page_no) for each heading 
#    found in the document; the number is 'R' for the references section
headings = []
# 'references_starting_page_no' is the page number where the references section
#    starts; it is 0 if no references section was found
references_starting_page_no = 0
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

# Formatting template to use for parsing
# NOTE: These are only used in this file by the "check_document_structure" function
supported_formatting_templates = ["springer", "aaai_acm", "acm"]
formatting_template = "springer"

# Paper template - formatting specifications
springer_formatting_template = {
    # Always skip first two lines in the springer template as they are: 
    #   page_lines[0] = Shortitle/Author; page_lines[1] = page number
    'name': "springer",
    "header_lines": 2,
}
aaai_acm_formatting_template = {
    # Always skip first X lines in the AAAI/ACM template as they are: 
    #   page_lines[0] = Shortitle/Author; page_lines[1] = page number
    'name': "aaai_acm",
    "header_lines": 2,
}
acm_formatting_template = {
    # Always skip first X lines in the ACM template as they are: 
    #   page_lines[0] = Shortitle/Author; page_lines[1] = page number
    'name': "acm",
    "header_lines": 2,
}

# Bibliography template to use for parsing
# NOTE: These are used in the AuhtorChecker and the ReferenceChecker
supported_bib_templates = ["springer", "aaai_acm", "acm"]
bib_template = "springer"


# Referencing template to use for parsing
# NOTE: These are used in the ReferenceChecker
supported_referencing_templates = ["numeric", "authoryear"]
referencing_template = "numeric"




###############################################################################
# Helper functions
###############################################################################

def check_document_structure(doc):
    global formatting_template
    global supported_formatting_templates
    global headings
    global references_starting_page_no
    global unicode_counter
    global unicode_lines

    print("###############################")
    print("# Starting Structure Check")
    print("###############################")

    #==========================================================================
    # Check template and get specifics
    #==========================================================================
    lineskip = 0
    for template in supported_formatting_templates:
        if template['name'] == formatting_template:
            lineskip = template["header_lines"]
    
    
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
            # Springer headings are parsed as a single number in one line
            #   and the heading in the next
            heading_match = re.match(r'^(?:[1-9]|[1-9]\d)$', line)
            if heading_match:
                number = heading_match.group(0)

                # Check if the current line is not the last
                if line_index + 1 < len(page_lines):
                    if len(headings) > 0:
                        last_index = len(headings) - 1
                        last_heading_no = int(headings[last_index][0].strip())
                        if int(number.strip())-1 == last_heading_no:
                            text = page_lines[line_index + 1].strip()
                            print(f"- Found following heading '{number} - {text}' on page {page_no + 1}")
                            headings.append((number, text, page_no + 1))
                    else:
                        text = page_lines[line_index + 1].strip()
                        print(f"- Found first heading '{number} - {text}' on page {page_no + 1}")
                        headings.append((number, text, page_no + 1))
                
            # Check for "References" or "Literature" (case-insensitive)
            elif line.lower() in ["references", "literature"]:
                print(f"=> Found references/literature section on page {page_no + 1}")
                last_number =headings[len(headings)-1][0]
                headings.append((int(last_number) + 1, line, page_no + 1))
                references_starting_page_no = page_no + 1
                return

        page_no += 1



###############################################################################
# Main code
###############################################################################

def main():
    """
    x
    """
    global supported_formatting_templates
    global formatting_template
    global supported_bib_templates
    global bib_template
    global supported_referencing_templates
    global referencing_template

    global headings
    global references_starting_page_no
    global unicode_lines


    #==========================================================================
    # Get Input Infos
    #==========================================================================
    path_to_pdf = input("Enter the path to the PDF file: ").strip().strip('"')

    input_formatting_template = input(f"Enter a supported formatting template ({supported_formatting_templates}): ").strip().strip('"')
    if input_formatting_template not in supported_formatting_templates:
        print(f"ERROR: Formatting template '{input_formatting_template}' not supported yet!")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        formatting_template = input_formatting_template
    
    input_bib_template = input(f"Enter a supported bibliography template ({supported_bib_templates}): ").strip().strip('"')
    if input_bib_template not in supported_bib_templates:
        print(f"ERROR: Biblography template '{input_bib_template}' not supported yet!")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        bib_template = input_bib_template
    
    input_ref_template = input(f"Enter a supported referencing template ({supported_referencing_templates}): ").strip().strip('"')
    if input_ref_template not in supported_referencing_templates:
        print(f"ERROR: Referencing template '{input_ref_template}' not supported yet!")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        referencing_template = input_ref_template


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
        references_df, ref_stats, entries = ref_c.main(doc, references_starting_page_no)
    
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
    
    #if not unicode_counter['\u00A0'] == total_no_of_nonbreaking_spaces:
    #    print(f"WARNING: The unicode_stats counted {total_no_of_nonbreaking_spaces} which is not equal to the unicode_counter's count.")

    # TODO: Check if all references used in the text are also listed in the references

    # Check the references rankings
    outlets_df = ran_c.main(extracted_references)
    
    # TODO: Check if all references support the statements made in the paper


    #==========================================================================
    # Check how often an author appears in the references
    #==========================================================================
    # NOTE: This dict is unsorted
    # TODO: Use extracted_references here?
    frequent_authors = ac.main(references_df, bib_template)


    #==========================================================================
    # RESULTS
    #==========================================================================
    # NOTE: Results will be saved in the same folder as the input PDF
    #       with the name "PQC_results.md"
    results_folder_dir = os.path.dirname(path_to_pdf)


    #--------------------------------------------------------------------------
    # Create Pie Chart with the literature validation results
    #--------------------------------------------------------------------------
    link_labels = ['No link provided', 'Valid link', 'Invalid link']
    link_values = [ref_stats["no_link_provided"], ref_stats["valid_links"], ref_stats["invalid_links"]]
    
    searches_labels = ['Skipped searches', 'Successful searches', 'Mismatching infos', 'NO ENTRY FOUND']
    searches_values = [ref_stats["skipped_searches"], ref_stats['successful_searches'], ref_stats["mismatching_infos"], ref_stats["no_entry_found"]]

    lit_fig = go.Figure(data=[go.Pie(labels=link_labels, values=link_values), go.Pie(labels=searches_labels, values=searches_values)])
    literature_validation_results_fig_path = os.path.join(results_folder_dir, "literature_validation_results_fig.jpg")
    lit_fig.write_image(literature_validation_results_fig_path)


    #--------------------------------------------------------------------------
    # Create Pie Chart with the outlet ranking results
    #--------------------------------------------------------------------------
    jq_rating_labels = ['A+', 'A', 'B', 'C', 'D', 'unkonwn']
    jq_rating = [len(outlets_df[outlets_df["jq_ranking"] == 'A+']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'A']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'B']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'C']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'D']), \
                 len(outlets_df[outlets_df["jq_ranking"] == 'unkown'])
                ]
    
    core_rating_labels = ['A*', 'A', 'B', 'C', 'D', 'unkonwn']
    core_rating_values = [len(outlets_df[outlets_df["jq_ranking"] == 'A*']), \
                          len(outlets_df[outlets_df["jq_ranking"] == 'A']), \
                          len(outlets_df[outlets_df["jq_ranking"] == 'B']), \
                          len(outlets_df[outlets_df["jq_ranking"] == 'C']), \
                          len(outlets_df[outlets_df["jq_ranking"] == 'D']), \
                          len(outlets_df[outlets_df["jq_ranking"] == 'unkown'])
                         ]

    # Create subplots: use 'domain' type for Pie subplot
    rank_fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    rank_fig.add_trace(go.Pie(labels=jq_rating_labels, values=jq_rating, name="JQ Ranking"),
                1, 1)
    rank_fig.add_trace(go.Pie(labels=core_rating_labels, values=core_rating_values, name="CORE Ranking"),
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
        f.write("# Paper Quality Check Results\n\n\n")
        f.write("## Document Structure\n\n\n")
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
            if invalid_unicode_lines[3]:
                f.write("Non-breaking spaces:\n")
                f.write("- Stats:\n")
                f.write(f"  - Valid uses: {unicode_stats['valid_nonbreaking_spaces']}/{total_no_of_nonbreaking_spaces}={unicode_stats['valid_nonbreaking_spaces']/total_no_of_nonbreaking_spaces*100:.2f}%\n")
                f.write(f"  - Invalid uses: {unicode_stats['invalid_nonbreaking_spaces']}/{total_no_of_nonbreaking_spaces}={unicode_stats['invalid_nonbreaking_spaces']/total_no_of_nonbreaking_spaces*100:.2f}%\n")
                f.write("- Lines containing invalid non-breaking spaces:\n")
                for line, page_no in invalid_unicode_lines[3]:
                    f.write(f"  - Page {page_no}: {line}\n")
            f.write("\n\n")
        
        # Print the rankings of the outlets
        f.write("\n## Outlet Rankings\n\n")
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
            f.write(f"	- References count from this outlet: {row['references_count']}\n")
        f.write("")
        f.write(f"![Outlet Ranking Results]({ranking_results_fig_path})")
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
            f.write(f"- No link provided: {ref_stats['no_link_provided']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['no_link_provided']/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            f.write(f"- Valid links: {ref_stats['valid_links']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['valid_links']/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            f.write(f"- Invalid link: {ref_stats['invalid_links']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['invalid_links']/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            if invalid_entries:
                f.write("	- Invalid entries:\n")
                for entry in invalid_entries:
                    f.write(f"		- {entry}\n")
            f.write(f"- Successful searches: {ref_stats['successful_searches']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['successful_searches']/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            f.write(f"- Skipped searches: {ref_stats['skipped_searches']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['skipped_searches']/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            f.write(f"- Mismatching infos: {ref_stats['mismatching_infos']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['mismatching_infos']/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            if mismatching_entries:
                f.write("	- Mismatching entries:\n")
                for entry in mismatching_entries:
                    f.write(f"		- {entry}\n")
            f.write(f"- No entry found: {ref_stats['no_entry_found']}/{TOTAL_NO_OF_REFERENCES}={ref_stats['no_entry_found']/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            if unfound_entries:
                f.write("	- Unfound entries:\n")
                for entry in unfound_entries:
                    f.write(f"		- {entry}\n")
            f.write("")
            f.write(f"![References Validation Results]({literature_validation_results_fig_path})")
            f.write("\n\n")

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
    
    print("---")
    print("FINISHED!")
    print(f" -> Results saved to {results_path}")



###############################################################################
# Run Main
###############################################################################
if __name__ == "__main__":
    main()