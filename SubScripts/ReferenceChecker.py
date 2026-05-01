###############################################################################
# Imports
###############################################################################
import pandas as pd
import random
import re
import requests
import sys
import time

import SubScripts.ScholarSearcher as scholar_searcher



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
inferred_bib_template = SPRINGER_BIB_STYLE

# Counters
no_link_provided_counter = 0
valid_link_counter = 0
invalid_link_counter = 0

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

    page_references = p_page_references

    # Replace "-\n" with nothing to remove obvious mid-sentence line breaks
    page_text = p_page_text.replace("-\n", "")

    page_lines = page_text.split("\n")

    # Skip first (and second) line, since this is the header, PDF author, or PDF page number
    for line in page_lines[line_skip:]:
        # Ensure that the line is long enough to check for the reference schema, 
        # otherwise append it to the last reference if it exists
        if len(line) > 4:
            # Matches the Springer Nature Template for references, where
            # each reference starts with, e.g., "1. " or "12. "
            if line[0].isdigit() and line[1] == "." and line[2] == " ":
                page_references.append(line.strip())
            elif line[0].isdigit() and line[1].isdigit() and line[2] == "." and line[3] == " ":
                page_references.append(line.strip())
            # If this schema is not found, but we already have at least one reference,
            # append the line to the last reference
            else:
                page_references[len(page_references)-1] += append_line_to_references(page_references, line)
        else:
            page_references[len(page_references)-1] += append_line_to_references(page_references, line)

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
        if "Tech. rep." in outlet_splitted[0]:
            outlet = outlet_splitted[1].strip()
        else:
            outlet = outlet_splitted[0].strip()
    
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

    # Save the full reference before parsing
    full_reference = ref
    reference = ref


    # ---------------------------------------------------------------
    # Get the reference's leading reference ID
    # ---------------------------------------------------------------

    reference = reference.strip()
    # Case of number being in square brackets
    # (10 chars should be more than enough for the ref. no.)
    if reference[0] == "[" and "]" in reference[0:11]:
        inferred_bib_template = ACM_BIB_STYLE

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
            ref_id = reference[1:no_length+1]
        
            # Cleanup reference string
            reference = reference[no_length+2:].strip()

    # Case of number being in no brackets
    # ref_id needs to be purly numerical for this
    elif reference[0].isdigit():
        inferred_bib_template = SPRINGER_BIB_STYLE

        no_length = 0
        for char in reference:
            if char.isdigit():
                no_length += 1
            else:
                break
        ref_id = reference[0:no_length+1]
        
        # Cleanup reference string
        reference = reference[no_length+2:].strip()
    
    # Case of there being no number
    # NOTE: Currently we assume that the pattern is lastname, firstname
    #       -> Malterud, K.; Siersma, V. D.; and Guassora, A. D.
    #           -> Referenced as: (Malterud, Siersma, and Guassora 2016)
    #       -> Lins, S.; Pandl, K. D.; Teigeler, H.; Thiebes, S.; Bayer, C.; and Sunyaev, A. 2021.
    #           -> Referenced as: (Lins et al. 2021)
    else:
        inferred_bib_template = AAAIACM_BIB_STYLE
        
        if ";" not in reference:
            ref_id = reference.split(",")[0].strip()
            ref_id = f"{ref_id} "
        else:
            authors = reference.split(";")
            if len(authors) <= 3:
                ref_id = ""
                for i in range(0, len(authors)):
                    ref_id += authors[i].split(",")[0].strip()
                    if i <= len(authors)-2:
                        ref_id += ", "
                    else:
                        ref_id += ", and "
            else:
                parts = reference.split(",")
                ref_id = f"{parts[0]} et al. "


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
            reference = reference[: m.start()].strip()
        else:
            print(f"-> Warning: Could not parse year in reference '{reference}'!")
        
        separator = springer_bib["authors_rest_separator"]
        if separator in reference:
            authors, rest = reference.split(separator, 1)
            authors = str(authors.strip())

            # Cleanup reference string
            reference = rest.strip()
            # E.g.: reference = "Title. Journal of Synthetic Knowledge Studies 12(3), 145–162"
    
    else:
        # E.g.: ACM-reference = "Virginia Braun and Victoria Clarke. 2006. Title. Qualitative Research in Psychology 3, 2 (Jan. 2006), 77–101."
        # E.g.: AAAI/ACM-reference = "Kim, D. J.; Yim, M.-S.; Sugumaran, V.; and Rao, H. R. 2016. Title. European Journal of Information Systems, 25(3): 252–273"
    
        m = re.search(r'(?:^|[\s,.;:(])((?:18|19|20)\d{2})\b', reference)
        if m:
            year = int(m.group(1))
            # In AAAI/ACM & ACM bib style, the year comes directly after the authors
            authors = reference[: m.start()].strip()

            # Cleanup reference string
            # E.g.: ACM-reference = ". Title. Qualitative Research in Psychology 3, 2 (Jan. 2006), 77–101."
            # E.g.: AAAI/ACM-reference = ". Title. European Journal of Information Systems, 25(3): 252–273"
            reference = reference[m.end():].strip().strip(".")
            reference = reference.strip()
            # E.g.: ACM-reference = "Title. Qualitative Research in Psychology 3, 2 (Jan. 2006), 77–101"
            # E.g.: AAAI/ACM-reference = "Title. European Journal of Information Systems, 25(3): 252–273"
        else:
            print(f"-> Warning: Could not parse year (and authors) in reference '{reference}'!")
            # TODO: Handle this case

    # Finish natural ref_id
    if inferred_bib_template == AAAIACM_BIB_STYLE:
        ref_id += year


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
        title = str(rest)


    return {
        'full_reference': full_reference,
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
    global valid_link_counter
    global invalid_link_counter
    global skipped_searches_counter
    global successful_searches_counter
    global mismatching_infos_counter
    global no_entry_found_counter

    global invalid_link_entries
    global mismatching_entries
    global unfound_entries

    print("###############################")
    print("# Starting Literature Check")
    print("###############################")


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
        references = check_page_text(references, page_text, 2)
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

            # Check if a link is provided; if not, search on Scholar
            # NOTE: For now skip .pdf links
            if current_link and not current_link.endswith(".pdf"):
                print(f"  -> Checking provided link: {current_link}")
                # Try to send a HEAD request to the provided link
                try:
                    request = requests.head(current_link)
                # Catch invalid links and search for the reference on Scholar instead
                except:
                    invalid_link_counter += 1
                    invalid_link_entries.append(f"{references_df.at[index, 'full_reference']}\n      -> Link caused an exception!")
                    local_references_df, local_stats = scholar_searcher.search_on_scholar(references_df, index, None)
                    references_df = local_references_df
                # Otherwise, if the link is valid, check its status code after sleeping
                else:
                    # Sleep to avoid getting Bot blocked
                    sleep_time = float(f"0.{random.randint(1, 9)}")
                    time.sleep(sleep_time)
                    # Check if site is reachable and set 'valid' column accordingly
                    if request.status_code != 404:
                        local_references_df, local_stats = scholar_searcher.search_on_scholar(references_df, index, current_link)
                        references_df = local_references_df
                    # Otherwise, if the link is not valid, search for the reference on Scholar instead
                    else:
                        invalid_link_counter += 1
                        invalid_link_entries.append(f"{references_df.at[index, 'full_reference']}\n      -> Returned with status code {request.status_code}!")
                        local_references_df, local_stats = scholar_searcher.search_on_scholar(references_df, index, None)
                        references_df = local_references_df
            elif current_link and current_link.endswith(".pdf"):
                print(f"  -> INFO: Skipping validity check of link ending with '.pdf': {current_link}")
                local_references_df, local_stats = scholar_searcher.search_on_scholar(references_df, index, None)
                references_df = local_references_df
            else:
                no_link_provided_counter += 1
                local_references_df, local_stats = scholar_searcher.search_on_scholar(references_df, index, None)
                references_df = local_references_df
            
            valid_link_counter += local_stats["valid_links"]
            invalid_link_counter += local_stats["invalid_links"]
            skipped_searches_counter += local_stats["skipped_searches"]
            successful_searches_counter += local_stats["successful_searches"]
            mismatching_infos_counter += local_stats["mismatching_infos"]
            no_entry_found_counter += local_stats["no_entry_found"]
    else:
        print(f" -> The whole validation process was skipped!")
        

    #==========================================================================
    # Return the final dataframe and values
    #==========================================================================
    stats = {
        "total_no_of_references": TOTAL_NO_OF_REFERENCES,
        "no_link_provided": no_link_provided_counter,
        'valid_links': valid_link_counter,
        "invalid_links": invalid_link_counter,
        "skipped_searches": skipped_searches_counter,
        "successful_searches": successful_searches_counter,
        "mismatching_infos": mismatching_infos_counter,
        "no_entry_found": no_entry_found_counter
    }
    #print(stats["invalid_links"])

    entries = [invalid_link_entries, mismatching_entries, unfound_entries]
    return references_df, stats, entries