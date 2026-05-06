###############################################################################
# Imports
###############################################################################
import copy
import pandas as pd
import random
import re
import requests
import sys
import time

import SubScripts.BibSearcher as bib_searcher
import SubScripts.UnicodeChecker as uc



###############################################################################
# INFO
###############################################################################

# NOTE: The references section needs to be named "References" or "Literature"


#==============================================================================
# Bibliography Styles
#==============================================================================

# Springer Nature (LaTeX) Template for references
# - DESRIST Conference:
    # 1. <Lastname>, <Firstname-FirstLetter>.: <Title>. <Outlet + Volume/Issue>, <PageRange> (<Year>). <URL/DOI>
    # Examples:
    #   16. Meyer, C., Schneider, T.: Automated detection of hallucinated academic references using neural consistency models. Journal of Synthetic Knowledge Studies 12(3), 145–162 (2024). https://doi.org/10.1234/jsks.2024.03145
    # Specifics:
    #   header_lines = 2
    #   author_separator = ,

# AAAI/ACM 
# - AIES Conference Template
    # <Lastname>, <Firstname-FirstLetter>. <Year>. <Title>. <Outlet + "," + Volume/Issue>: <PageRange>
    # Examples:
    #   Kim, D. J.; Yim, M.-S.; Sugumaran, V.; and Rao, H. R. 2016. Web assurance seal services, trust and consumers’ concerns: An investigation of e-commerce transaction intentions across two nations. European Journal of Information Systems, 25(3): 252–273
    # Specifics:
    #   header_lines = ?
    #   auhtor_separator = ;

# ACM General?
# - CHI Conference Template
    # [1] <Firstname> <Lastname>. <Year>. <Title>. <Outlet + Volume/Issue>. (<Date>), <PageRange>. <URL/DOI>
    # Examples:
    #   [5] Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology. Qualitative Research in Psychology 3, 2 (Jan. 2006), 77–101. https://doi.org/10.1191/1478088706qp063oa
    # Specifics:
    #   header_lines = ?
    #   author_separator = ,



###############################################################################
# Gloal Variables
###############################################################################

# NOTE: MAX_SCHOLAR_ENTRIES_TO_CHECK needs to be >= 11
MAX_SCHOLAR_ENTRIES_TO_CHECK = 25

# Bibliography Style Specifics
given_bib_type = ""
given_line_skip = 0

SPRINGER_BIB_STYLE = "springer"
springer_bib = {
    "name": SPRINGER_BIB_STYLE,
    "authors_rest_separator": ":",
    "author_separator": ","
}
AAAIACM_BIB_STYLE = "aaai_acm"
aaai_acm_bib = {
    "name": AAAIACM_BIB_STYLE,
    "authors_rest_separator": ".",
    "author_separator": ";"
}
ACM_BIB_STYLE = "acm"
acm_bib = {
    "name": ACM_BIB_STYLE,
    "authors_rest_separator": ".",
    "author_separator": ","
}
supported_bib_templates = [springer_bib, aaai_acm_bib, acm_bib]
inferred_bib_template = SPRINGER_BIB_STYLE

# Counters
no_link_provided_counter = 0
link_not_checked_counter = 0
valid_link_counter = 0
invalid_link_counter = 0
different_link_found_counter = 0

skipped_searches_counter = 0
successful_searches_counter = 0
mismatching_infos_counter = 0
no_entry_found_counter = 0

invalid_link_entries = []
mismatching_entries = []
unfound_entries = []



###############################################################################
# Helper functions
###############################################################################

def get_supported_bib_templates():
    global supported_bib_templates
    return supported_bib_templates

def set_given_bib_type(bib_type, lineskip):
    global given_bib_type
    global given_line_skip
    given_bib_type = bib_type
    given_line_skip = lineskip


def append_line_to_references(page_references, line):
    """
    append_line_to_references takes a list of already found references and a 
    line and checks if the last reference of the list contains a link; 
    if so, it appends the line to the last reference without a space, 
    otherwise with a space in between.
    """

    if len(page_references) > 0:
        last_reference = page_references[len(page_references)-1].lower()
        if "http" in last_reference:
            return line.strip()
        else:
            return ' ' + line.strip()
    else:
        print(f"""WARNING: Trying to append a line to references, but no  
              reference found yet! Line: '{line}'""")
        return line.strip()


def check_page_text(p_page_references, p_page_text, line_skip):
    """
    check_page_text takes
        1) a list of already found references (empty for the first page),
        2) the text of the current page, and 
        3) the lines to skip (e.g., header lines; only 1 for the first page)
    and returns an updated list of all found references, where each reference
    is just one string parsed from the given file
    """

    page_references = copy.deepcopy(p_page_references)

    # Replace "-\n" with nothing to remove obvious mid-sentence line breaks
    page_text = p_page_text.replace("-\n", "")

    page_lines = page_text.split("\n")

    # Skip first (and second) line, since this is the header, PDF author, or PDF page number
    #for line in page_lines[line_skip:]: 
    for line_index in range(line_skip, len(page_lines)):
        # Ensure that the line is long enough to check for the reference schema, 
        # otherwise append it to the last reference if it exists
        if len(page_lines[line_index]) > 4:

            if given_bib_type == SPRINGER_BIB_STYLE:
                # Matches the Springer Nature Template for references, where
                # each reference starts with, e.g., "1. " or "12. "
                if page_lines[line_index][0].isdigit() and page_lines[line_index][1] == "." and page_lines[line_index][2] == " ":
                    page_references.append(page_lines[line_index].strip())
                elif page_lines[line_index][0].isdigit() and page_lines[line_index][1].isdigit() and page_lines[line_index][2] == "." and page_lines[line_index][3] == " ":
                    page_references.append(page_lines[line_index].strip())
                # If this schema is not found, but we already have at least one reference,
                # append the line to the last reference
                else:
                    if not page_references:
                        page_references.append(page_lines[line_index].strip())
                    else:
                        page_references[len(page_references)-1] += append_line_to_references(page_references, page_lines[line_index])

            elif given_bib_type == AAAIACM_BIB_STYLE:
                # Matches the AAAI/ACM Template for references, where
                # each reference starts with the authornames
                current_line = page_lines[line_index].strip()

                if not page_references:
                    page_references.append(current_line)
                    continue

                # Usual case, as a new reference starts with mostly multiple auhtors that
                # are seperated by ; which is also a char very unlikely to be used in the
                # title / outlet / etc. 
                sep = aaai_acm_bib['author_separator']
                year_cl = re.search(r'(?:^|[\s,.;:(])((?:18|19|20)\d{2})\.', current_line)
                if year_cl and year_cl.start()-2 >= 0:
                    if current_line[year_cl.start()-2:year_cl.start()+1].lower() == "in " \
                       or current_line[year_cl.start()-2:year_cl.start()+1].lower() == "n: ":
                        year_cl = None
                year_pl = re.search(r'(?:^|[\s,.;:(])((?:18|19|20)\d{2})\.', page_lines[line_index-1])
                if re.search(r'\bin\s', page_lines[line_index-1].lower()):
                    year_pl = None

                # If both lines (previous and this) contain years -> new reference
                if year_cl and year_pl:
                    page_references.append(current_line)
                    continue
                # If the current line contains ; and the previous doesn't contain a ; nor a year
                elif sep in current_line and sep not in page_lines[line_index-1] and not year_pl:
                    page_references.append(current_line)
                    continue
                # If the current line contains a year and the previous doesn't contain a ;
                elif year_cl and sep not in page_lines[line_index-1]:
                    page_references.append(current_line)
                    continue
                
                year_pr = re.search(r'(?:^|[\s,.;:(])((?:18|19|20)\d{2})\.', page_references[len(page_references)-1])
                ed_cl = re.search(r'\b(in\s|eds\.)', current_line.lower())

                # If the current contains a ; and not "In " / "eds.", and the previous reference contains a year
                # NOTE: Here, a line that should be added to the previous reference might be recognized as new
                #       -> Its fine for about >85% of the cases, but yeah, can happen
                if sep in current_line and not ed_cl and year_pr:
                    # If a firstname is alone at the beginning, append to prev. ref.
                    if current_line[1] == "." and (current_line[2] == " " or current_line[2] == ";"):
                        page_references[len(page_references)-1] += append_line_to_references(page_references, current_line)
                    else:
                        page_references.append(current_line)
                # Otherwise, append to previous line's reference
                else:
                    page_references[len(page_references)-1] += append_line_to_references(page_references, current_line)
            
            elif given_bib_type == ACM_BIB_STYLE:
                # Matches the ACM Template for references, where
                # each reference starts with the [xx]
                if page_lines[line_index][0] == "[" and page_lines[line_index][1].isdigit() and page_lines[line_index][2] == "]":
                    page_references.append(page_lines[line_index].strip())
                elif page_lines[line_index][0] == "[" and page_lines[line_index][1].isdigit() and page_lines[line_index][2].isdigit() and page_lines[line_index][3] == "]":
                    page_references.append(page_lines[line_index].strip())
                elif page_lines[line_index][0] == "[" and page_lines[line_index][1].isdigit() and page_lines[line_index][2].isdigit() and page_lines[line_index][3].isdigit and page_lines[line_index][43] == "]":
                    page_references.append(page_lines[line_index].strip())
                # If this schema is not found, but we already have at least one reference,
                # append the line to the last reference
                else:
                    if not page_references:
                        page_references.append(page_lines[line_index].strip())
                    else:
                        page_references[len(page_references)-1] += append_line_to_references(page_references, page_lines[line_index])

            else:
                print(f"=> ERROR: given_bib_tye = {given_bib_type} not recognized!")

        else:
            if line_index == line_skip:
                page_references.append(page_lines[line_index].strip())
            else:
                page_references[len(page_references)-1] += append_line_to_references(page_references, page_lines[line_index])

    return page_references


def check_outlet(outlet: str) -> str:
    """
    check_outlet takes an outlet string and checks for common patterns to clean it up,
    such as removing leading "In: ", trailing page numbers, or specific page references.
    """

    # Remove leading "In: "
    if outlet[0:4].lower() == "in: ":
        outlet = outlet[4:]
    elif outlet[0:3].lower() == "in ":
        outlet = outlet[3:]
    
    # Split a , to remove trailing page numbers
    if "," in outlet:
        outlet_splitted = outlet.split(",")
        if len(outlet_splitted) == 1:
            pass
        elif len(outlet_splitted) == 2:
            if "Tech. rep." in outlet_splitted[0]:
                outlet = outlet_splitted[1].strip()
            else:
                outlet = outlet_splitted[0].strip()
        else:
            # Delete everything before "eds."
            if outlet.find("eds.,") != -1:
                eds_i = outlet.find("eds.,")
                outlet = outlet[eds_i+5:].strip()

            # 
            outlet_point_split = outlet.split(". ")
            temp_outlet = ""
            for part in outlet_point_split:
                part = part.strip()
                if "ISSN" in part.upper() or "ISBN" in part.upper():
                    pass
                elif "event-place" in part.lower() or part.isnumeric():
                    pass
                else:
                 temp_outlet += " " + part
            temp_outlet = temp_outlet.strip()
            outlet_splitted = temp_outlet.split(",")
            outlet = ','.join(outlet_splitted[:-1])
        
    
    # Remove specific page references
    if "pp." in outlet:
        outlet = outlet.split("pp.")[0].strip()
    if "p." in outlet:
        outlet = outlet.split("p.")[0].strip()

    # Remove tailing issue references "XX(X)"
    if "(" in outlet and ")" in outlet:
        outlet_splitted = outlet.split(" ")
        if "(" in outlet_splitted[-1]:
            outlet = ' '.join(outlet_splitted[:-1])

    return outlet


def parse_reference(ref: str) -> dict:
    """
    parse_reference converts a list of reference strings into a list of dicts
    with the following keys:
    - 'full_reference', the full reference string before parsing
    - 'ref_id', a string as how the reference is referenced in-text
    - 'authors', a string containing all authors
    - 'title', a string containing the reference's title
    - 'year', an int containing the reference's year (otherwise it's 0)
    - 'abstract', is always None for now
    - 'outlet', a string containing the reference's outlet
    - 'link', a string containing the reference's link (otherwise it's '')
    - 'valid', is always None for now
    """

    global inferred_bib_template

    # Deepcopy the full reference before parsing
    reference = copy.deepcopy(ref)


    # ---------------------------------------------------------------
    # Get the reference's leading reference ID
    # ---------------------------------------------------------------

    reference = reference.strip()
    # Case of number being in square brackets
    # (10 chars should be more than enough for the ref. no.)
    if reference[0] == "[" and "]" in reference[0:11]:
        inferred_bib_template = ACM_BIB_STYLE
        if inferred_bib_template != given_bib_type:
            print(f"-> Warning: Bib template mismatch!")

        pattern = r"$$(.*?)$$"
        pattern_match = re.search(pattern, reference[0:11])
        if pattern_match:
            ref_id = str(pattern_match.group(1))
        
            # Cleanup reference string
            reference = reference[pattern_match.end():].strip().lstrip("]")
        else:
            # Example: "[13]"
            #      i =  0123
            no_length = 0
            for char in reference[1:11]:
                if char != "]":
                    no_length += 1
                else:
                    break
            ref_id = reference[1:no_length]
        
            # Cleanup reference string
            reference = reference[no_length+1:].strip()

    # Case of number being in no brackets
    # ref_id needs to be purly numerical for this
    elif reference[0].isdigit():
        inferred_bib_template = SPRINGER_BIB_STYLE
        if inferred_bib_template != given_bib_type:
            print(f"-> Warning: Bib template mismatch!")

        no_length = 0
        for char in reference:
            if char.isdigit():
                no_length += 1
            else:
                break
        ref_id = reference[0:no_length]
        
        # Cleanup reference string
        reference = reference[no_length+1:].strip()
    
    # Case of there being no number
    # NOTE: Currently we assume that the pattern is lastname, firstname
    #       -> Malterud, K.; Siersma, V. D.; and Guassora, A. D.
    #           -> Referenced as: (Malterud, Siersma, and Guassora 2016)
    #       -> Lins, S.; Pandl, K. D.; Teigeler, H.; Thiebes, S.; Bayer, C.; and Sunyaev, A. 2021.
    #           -> Referenced as: (Lins et al. 2021)
    # NOTE: We need to get rid of points behind "et al." so the parsing in the RefIntextChecker
    #       works
    else:
        inferred_bib_template = AAAIACM_BIB_STYLE
        if inferred_bib_template != given_bib_type:
            print(f"-> Warning: Bib template mismatch!")
        
        # To avoid mixups with potential editors, cut off reference after year!
        year = re.search(r'(?:^|[\s,.;:(])((?:18|19|20)\d{2})\b', reference)
        if year:
            first_ref_part = reference[:year.start()].strip()
        
            # Case single authors (only take lastname)
            if ";" not in first_ref_part:
                ref_id = first_ref_part.split(",")[0].strip()
                ref_id = ref_id.strip(".")
                ref_id = f"{ref_id} "
            # Case multiple authors
            else:
                authors_list = first_ref_part.split(";")
                if len(authors_list) == 2:
                    ref_id = authors_list[0].split(",")[0].strip()
                    if "et al" in authors_list[1] :
                        ref_id += " et al "
                    else:
                        if "and" in authors_list[1]:
                            ref_id += " "
                        else:
                            ref_id += " and "
                        ref_id += authors_list[1].split(",")[0].strip()
                        ref_id += " "
                elif len(authors_list) == 3:
                    ref_id = authors_list[0].split(",")[0].strip()
                    ref_id += ", "
                    ref_id += authors_list[1].split(",")[0].strip()
                    if "et al" in authors_list[2]:
                        ref_id += " et al "
                    else:
                        if "and" in authors_list[2]:
                            ref_id += ", "
                        else:
                            ref_id += ", and "
                        ref_id += authors_list[2].split(",")[0].strip()
                        ref_id += " "
                else:
                    parts = first_ref_part.split(",")
                    ref_id = f"{parts[0]} et al "
        else:
            print(f"-> Warning: No year recognized in reference '{reference}'")
            parts = reference.split(",")
            ref_id = f"{parts[0]} et al "


    # ---------------------------------------------------------------
    # Get the rest of the reference
    # ---------------------------------------------------------------

    # try to extract link (doi or http) at end
    link = ''
    m = re.search(r'(https?://\S+)', reference)
    if m:
        link = str(m.group(1))
        # Cleanup reference string (the link is usually the last part)
        reference = reference[: m.start()].strip()

    # year and authors
    year = 0
    authors = ''
    if inferred_bib_template == SPRINGER_BIB_STYLE:
        # E.g.: reference = "Meyer, C., Schneider, T.: Title. Journal of Synthetic Knowledge Studies 12(3), 145–162 (2024)."
        m = re.search(r'\((\d{4})\)', ref)
        if m:
            year = int(m.group(1))
            # Cleanup reference string (the year should be the last part)
            reference = reference[:m.start()-3].strip()
        else:
            m = re.search(r'\s(\d{4})\)', ref)
            if m:
                year = int(m.group(1))
                # Cleanup reference string (the year should be the last part)
                reference = reference[:m.start()-2].strip()
            else:
                print(f"-> Warning: Could not parse year in reference '{reference}'!")
        
        separator = springer_bib["authors_rest_separator"]
        if separator in reference:
            authors, rest = reference.split(separator, 1)
            authors = uc.replace_accent_marks(authors.strip())

            # Cleanup reference string
            reference = rest.strip()
            # E.g.: reference = "Title. Journal of Synthetic Knowledge Studies 12(3), 145–162"
        # TODO: What else?
    
    else:
        # E.g.: ACM-reference = "Virginia Braun and Victoria Clarke. 2006. Title. Qualitative Research in Psychology 3, 2 (Jan. 2006), 77–101."
        # E.g.: AAAI/ACM-reference = "Kim, D. J.; Yim, M.-S.; Sugumaran, V.; and Rao, H. R. 2016. Title. European Journal of Information Systems, 25(3): 252–273"
    
        m = re.search(r'(?:^|[\s,.;:(])((?:18|19|20)\d{2})\b', reference)
        if m:
            year = int(m.group(1))
            # In AAAI/ACM & ACM bib style, the year comes directly after the authors
            authors = reference[: m.start()].strip()
            authors = uc.replace_accent_marks(authors)

            # Cleanup reference string
            # E.g.: ACM-reference = ". Title. Qualitative Research in Psychology 3, 2 (Jan. 2006), 77–101."
            # E.g.: AAAI/ACM-reference = ". Title. European Journal of Information Systems, 25(3): 252–273"
            reference = reference[m.end():].strip().strip(".")
            reference = reference.strip()
            # E.g.: ACM-reference = "Title. Qualitative Research in Psychology 3, 2 (Jan. 2006), 77–101"
            # E.g.: AAAI/ACM-reference = "Title. European Journal of Information Systems, 25(3): 252–273"
        else:
            print(f"-> Warning: Could not parse year (and authors) in reference '{reference}'!")
            return {
                'full_reference': ref,
                'ref_id': "NOT PARSED",
                'authors': "NOT PARSED",
                'title': "NOT PARSED",
                'year': "NOT PARSED",
                'abstract': None,
                'outlet': "NOT PARSED",
                'link': link,
                'valid': None,
            }

    # Finish natural ref_id
    if inferred_bib_template == AAAIACM_BIB_STYLE:
        ref_id += str(year)


    # ---------------------------------------------------------------
    # Get the title and outlet
    # ---------------------------------------------------------------

    title = ''
    outlet = ''
    # E.g.: Springer-reference = "Title. Journal of Synthetic Knowledge Studies 12(3), 145–162"
    # E.g.: ACM-reference      = "Title. Qualitative Research in Psychology 3, 2 (Jan. 2006), 77–101"
    # E.g.: AAAI/ACM-reference = "Title. European Journal of Information Systems, 25(3): 252–273"

    # title ends with a period before the outlet (if present)
    if '. ' in reference:
        title, outlet = reference.split('. ', 1)
        if title and outlet:
            title = str(title.strip())
            # Check a last accessed date was parsed as outlet
            if "accessed:" in outlet.lower():
                outlet = ""
            else:
                outlet = str(outlet.strip().rstrip('.'))
                outlet = check_outlet(outlet)
        else:
            # fallback: try to split on period
            parts = reference.split('. ')
            if parts:
                title = str(parts[0].strip())
                outlet = str(' '.join(parts[1:]).strip().rstrip('.'))
                outlet = check_outlet(outlet)
    else:
        title = str(reference)


    return {
        'full_reference': ref,
        'ref_id': ref_id,
        'authors': authors,
        'title': title,
        'year': year,
        'abstract': None,
        'outlet': outlet,
        'link': link,
        'valid': None,
    }



###############################################################################
# Main code
###############################################################################

def main(doc, ref_starting_page):
    """
    The ReferenceChecker receives a document and the page number where the 
    reference section starts as input and
    1) extracts all references as separate strings,
    2) parses the reference strings to extract their components,
    3) checks if provided reference links are valid, and if not, 
       searches for the author and/or title on Scholar
    4) returns a dataframe with all found references and their 
       parsed information, as well as a dict of counters for statistics.

    ---

    The returned dataframe contains the following columns:
    - 'full_reference', the full reference string before parsing
    - 'ref_id', a string as how the reference is referenced in-text
    - 'authors', a string containing all authors
    - 'title', a string containing the reference's title
    - 'year', an int containing the reference's year (otherwise it's 0)
    - 'abstract', a String containing the found reference's abstract (otherwise it's None)
    - 'outlet', a string containing the reference's outlet
    - 'link', a string containing the reference's link (otherwise it's '')
    - 'valid', a string message indicating the results concering 
               the reference's validity check
    
    The returned dict of counters contains the following keys:
    - "total_no_of_references": the total number of found references
    - "no_link_provided": count of references for which no link was provided
    - "invalid_links": count of references with invalid links
    - "skipped_searches": count of references where search was skipped
    - "successful_searches": count of references where search was successful
    - "mismatching_infos": count of references with mismatching information
    - "no_entry_found": count of references for which no entry was found

    The returned list of entries contains three lists with the following entries:
    - [0]: invalid_link_entries - list of all references with invalid links
    - [1]: mismatching_entries - list of all references with mismatching information
    - [2]: unfound_entries - list of all references for which no entry was found
    """

    global no_link_provided_counter
    global link_not_checked_counter
    global valid_link_counter
    global invalid_link_counter
    global different_link_found_counter

    global skipped_searches_counter
    global successful_searches_counter
    global mismatching_infos_counter
    global no_entry_found_counter

    global invalid_link_entries
    global mismatching_entries
    global unfound_entries

    print("##########################################################")
    print("# Starting Literature Check")
    print("##########################################################")


    #==========================================================================
    # Get all references from the reference section as separate stings in the 
    # 'references' list
    #==========================================================================
    print(f"Checking references on pages: {ref_starting_page} -- {doc.page_count}")
    references = []
    ref_starting_index = 0

    # NOTE: doc[page_number] is 0-based
    page_text = doc[ref_starting_page-1].get_text()

    # Check if the page contains "References" or "Literature"
    if page_text.find("References") != -1 or page_text.find("Literature") != -1:

        # Find the starting index of the reference section
        if page_text.find("References") != -1:
            ref_starting_index = page_text.find("References")
        else:
            ref_starting_index = page_text.find("Literature")

    else:
        print(f"""Could not find 'References'/'Literature' on page {ref_starting_page}. 
                Please check the page number and try inputting it manually:""")
        
        # Loop to give user the chance to retry if they messed up the inputs
        while True:
            ref_starting_page = int(input(" -> Please enter the page number where the reference section starts: ").strip())
            ref_section_name = input(" -> Please enter the name of the reference section (e.g., 'Literature'): ").strip()

            # Find the starting index of the reference section and cut the text before
            if page_text.find(ref_section_name) != -1:
                ref_starting_index = page_text.find(ref_section_name)
                break
            else:
                print(f"Could not find '{ref_section_name}' on page {ref_starting_page}...")
                retry = input(" -> If you want to retry, enter 'y' or 'yes': ").strip()
                if not (retry.lower() == "y" or retry.lower() == "yes"):
                    # Since the references are essential, just quit the whole program
                    print("Ok, thanks for trying. Good luck on your own! :)")
                    sys.exit(0)

    # Cut the text before the reference section; we don't need it
    page_text = page_text[ref_starting_index:]

    # Extract the references from the first page of the reference section
    references = check_page_text([], page_text, 1)

    # Iterate over all remaining pages and check for remaining references
    for page_no in range(ref_starting_page, doc.page_count):
        page_text = doc[page_no].get_text()
        if given_bib_type == SPRINGER_BIB_STYLE:
            references = check_page_text(references, page_text, 2)
        else:
            references = check_page_text(references, page_text, 0)
        page_no += 1
    
    # Log the results
    TOTAL_NO_OF_REFERENCES = len(references)
    print(f"All found references: {TOTAL_NO_OF_REFERENCES}")
    

    #==========================================================================
    # Extract information from full reference strings
    #==========================================================================
    reference_components = [parse_reference(e) for e in references]
    # NOTE: The references_df contains the following columns: 
    #       'full_reference', 'ref_id', 'authors', 'title', 'year', 'abstract', 'outlet', 
    #       'link', and 'valid'
    references_df = pd.DataFrame(reference_components)
    
    print("-----------")
    print(" -> Parsed references DataFrame:")
    print(references_df.drop('full_reference', axis=1))


    #==========================================================================
    # Check if provided references are valid
    #==========================================================================
    skip_validation = input("=> To skip the validation (Scholar Search) and the abstract retrival, type 'skip': ").strip()
    if skip_validation.lower() != "skip":

        for index in range(len(references_df)):
            current_link = references_df.at[index, 'link']
            print(f"- Checking reference {index + 1}/{len(references_df)}:")

            # Check if a link is provided
            # NOTE: For now skip .pdf links
            if current_link and not current_link.endswith(".pdf"):
                print(f"  -> Checking provided link: {current_link}")
                # Try to send a HEAD request to the provided link
                try:
                    request = requests.head(current_link)
                # Catch invalid links and search for the reference on online
                except:
                    invalid_link_counter += 1
                    invalid_link_entries.append(f"{references_df.at[index, 'full_reference']}\n			-> Link caused an exception!")
                    local_references_df, local_stats, local_mismatching_entries, local_unfound_entries = bib_searcher.search_bib(references_df, index, None)
                    references_df = local_references_df
                # Otherwise, if the link is valid, check its status code after sleeping
                else:
                    # Sleep to avoid getting Bot blocked
                    sleep_time = float(f"0.{random.randint(1, 9)}")
                    time.sleep(sleep_time)
                    # Check if site is reachable and set 'valid' column accordingly
                    if request.status_code != 404:
                        local_references_df, local_stats, local_mismatching_entries, local_unfound_entries  = bib_searcher.search_bib(references_df, index, current_link)
                        references_df = local_references_df
                    # Otherwise, if the link is not valid, search for the reference on online
                    else:
                        invalid_link_counter += 1
                        invalid_link_entries.append(f"{references_df.at[index, 'full_reference']}\n			-> Returned with status code {request.status_code}!")
                        local_references_df, local_stats, local_mismatching_entries, local_unfound_entries  = bib_searcher.search_bib(references_df, index, None)
                        references_df = local_references_df
            elif current_link and current_link.endswith(".pdf"):
                print(f"  -> INFO: Skipping validity check of link ending with '.pdf': {current_link}")
                local_references_df, local_stats, local_mismatching_entries, local_unfound_entries  = bib_searcher.search_bib(references_df, index, None)
                references_df = local_references_df
            else:
                no_link_provided_counter += 1
                local_references_df, local_stats, local_mismatching_entries, local_unfound_entries  = bib_searcher.search_bib(references_df, index, None)
                references_df = local_references_df

            if bib_searcher.get_skip_all_remaining_validations():
                print(f" -> The remaining validation process was skipped!")
                search_sum = skipped_searches_counter + successful_searches_counter + mismatching_infos_counter + no_entry_found_counter
                skipped_searches = TOTAL_NO_OF_REFERENCES - search_sum
                skipped_searches_counter += skipped_searches
                break
            
            link_not_checked_counter += local_stats["unchecked_links"]
            valid_link_counter += local_stats["valid_links"]
            invalid_link_counter += local_stats["invalid_links"]
            different_link_found_counter += local_stats["different_links"]
            skipped_searches_counter += local_stats["skipped_searches"]
            successful_searches_counter += local_stats["successful_searches"]
            mismatching_infos_counter += local_stats["mismatching_infos"]
            no_entry_found_counter += local_stats["no_entry_found"]

            mismatching_entries += local_mismatching_entries
            unfound_entries += local_unfound_entries 
    else:
        print(f" -> The whole validation process was skipped!")
        

    #==========================================================================
    # Return the final dataframe and values
    #==========================================================================
    stats = {
        "total_no_of_references": TOTAL_NO_OF_REFERENCES,
        "no_link_provided": no_link_provided_counter,
        "unchecked_links": link_not_checked_counter,
        "valid_links": valid_link_counter,
        "invalid_links": invalid_link_counter,
        "different_links": different_link_found_counter,
        "skipped_searches": skipped_searches_counter,
        "successful_searches": successful_searches_counter,
        "mismatching_infos": mismatching_infos_counter,
        "no_entry_found": no_entry_found_counter
    }
    #print(stats["invalid_links"])

    entries = [invalid_link_entries, mismatching_entries, unfound_entries]
    return references_df, stats, entries