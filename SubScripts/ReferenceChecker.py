###############################################################################
# Imports
###############################################################################
import pandas as pd
from rich.progress import Progress
import pymupdf
import random
import re
import requests
from scholarly import scholarly
import time



###############################################################################
# INFO
###############################################################################

# NOTE: The references section needs to be named "References" or "Literature"

# Springer Nature (LaTeX) Template for references:
    # 1. Lastname, Firstname-FirstLetter.: Title. OutletName, PageRange (Year). URL/DOI

# Google Scholar API:
    # https://stackoverflow.com/questions/62938110/does-google-scholar-have-an-api-available-that-we-can-use-in-our-research-applic
    # NOTE: Prefer DOIs and URLs over a google scholar search



###############################################################################
# Gloal Variables
###############################################################################

no_link_provided_counter = 0
invalid_link_counter = 0
skipped_searches_counter = 0
mismatching_infos_counter = 0
no_entry_found_counter = 0
invalid_entries = []



###############################################################################
# Helper functions
###############################################################################

def check_page_text(page_references, page_text, line_skip):
    """
    check_page_text takes
        1) a list of already found references (empty for the first page),
        2) the text of the current page, and 
        3) the lines to skip (e.g., header lines; only 1 for the first page)
    and returns an updated list of all found references, where each reference
    is just one string parsed from the given file
    """

    # Replace "-\n" with nothing to remove obvious mid-sentence line breaks
    page_text = page_text.replace("-\n", "")

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
                if len(page_references) > 0:
                    page_references[len(page_references)-1] += ' ' + line.strip()
        else:
            if len(page_references) > 0:
                page_references[len(page_references)-1] += ' ' + line.strip()

    return page_references


def parse_reference(ref: str) -> dict:
    """
    parse_reference converts a list of reference strings into a list of dicts
    with the following keys:
    - 'full_reference', the full reference string before parsing
    - 'authors', a string containing all authors
    - 'title', a string containing the reference's title
    - 'year', an int containing the reference's year (otherwise it's 0)
    - 'outlet', a string containing the reference's outlet
    - 'link', a string containing the reference's link (otherwise it's '')
    - 'valid', is always None for now
    """

    # save the full reference before parsing, since we will be removing parts of it during parsing
    full_reference = ref

    # remove leading index and any surrounding whitespace
    ref = ref.strip()
    ref = re.sub(r'^\d+\.\s*', '', ref)

    # try to extract link (doi or http) at end
    link = ''
    m = re.search(r'(https?://\S+)', ref)
    if m:
        link = str(m.group(1))
        ref = ref[: m.start()].strip()

    # year in parentheses
    year = 0
    m = re.search(r'\((\d{4})\)', ref)
    if m:
        year = int(m.group(1))
        # optionally remove the year from ref so it doesn't pollute outlet
        ref = ref[: m.start()].strip()

    # authors and the rest are split by first colon
    authors = ''
    title = ''
    outlet = ''
    if ':' in ref:
        authors, rest = ref.split(':', 1)
        authors = str(authors.strip())
        rest = rest.strip()
        # title ends with a period before the outlet (if present)
        if '. ' in rest:
            title, outlet = rest.split('. ', 1)
            title = str(title.strip())
            outlet = str(outlet.strip().rstrip('.'))
        else:
            title = str(rest)
    else:
        # fallback: try to split on period
        parts = ref.split('. ')
        if parts:
            title = str(parts[0].strip())
            outlet = str(' '.join(parts[1:]).strip().rstrip('.'))

    return {
        'full_reference': full_reference,
        'authors': authors,
        'title': title,
        'year': year,
        'outlet': outlet,
        'link': link,
        'valid': None,
    }


def activate_title_scholar_search(author_search_yielded_results, author, title, year):
    query = f"{title}"
    # Get the search results and check if at least one result is found
    search_query = scholarly.search_pubs(query)
    print(f"   => INFO: Found {search_query.total_results} results for '{query}'.")

    if search_query.total_results >= 1:
        no_of_results_to_check = min(search_query.total_results, 15)

        # Cool progress bar to look at while all results are being checked
        with Progress() as p:
            task = p.add_task("Processing title search...", total=no_of_results_to_check)

            # Loop over all results and check if the title (and year) matches
            print(f"     -> INFO: Now checking {no_of_results_to_check} results for matching title and authors")
            for res_i in range(1, no_of_results_to_check):
                try:
                    # Sleep to avoid getting Bot blocked
                    sleep_time = float(f"0.{random.randint(1, 9)}")
                    time.sleep(sleep_time)
                    current_search_result = next(search_query)
                except Exception as e:
                    print(f"     -> ERROR - Iterating search results failed: {e}")
                    p.stop()
                    break

                pub_title = current_search_result['bib']['title']

                # During parsing spaces may go missing, so we ignore them when comparing titles
                if pub_title.replace(" ", "").lower() == title.replace(" ", "").lower():
                    print("     -> INFO: Titles matched!")

                    # NOTE: current_search_result['author_id'] is a list of Google Scholar IDs
                    #pub_authors = current_search_result['author_id']
                    # NOTE: current_search_result['author_id'] is a list where each entry has the form "C Janiesch"
                    pub_bib_authors = current_search_result['bib']['author']
                    for pub_author in pub_bib_authors:
                        lastname = pub_author.split(" ")[1].strip().lower()
                        if not lastname in author.lower():
                            print(f"     -> ERROR: Lastname ({lastname}) does not match any expected authors' ({author.lower()})!")
                            break

                    pub_year = int(current_search_result['bib']['pub_year'])
                    if pub_year == year:
                        print("     -> SUCCESS: Title, authors, and year matched; reference checks out. :)")
                        p.stop()
                        return f"Found: {current_search_result['pub_url']}"
                    else:
                        print(f"     -> ERROR: Year ({pub_year}) does not match expected year ({year})!")
                        print(f"        Manual check required: {current_search_result['pub_url']}")
                        p.stop()
                        return f"CHECK - Year did not match: {current_search_result['pub_url']}"
            
            p.update(task, advance=1)

        p.stop()
            
        # If none of them match, do an alternative search with the title
        print(f"     -> ERROR: None of the {no_of_results_to_check} searched title-search-results on Scholar matched!")
        return "NO match found; Both the author and the title search query on Scholar did not yield any match!"

    else:
        if not author_search_yielded_results:
            return "NO results found; Both the author and the title search query on Scholar did not yield any results"
        else:
            return "No title search results found; Author search didn't yield a positive match and title search didn't yield any results"


def activate_author_scholar_search(author, title, year):
    # NOTE: https://scholarly.readthedocs.io/en/stable/quickstart.html#search-for-articles-publications-and-return-generator-of-publication-objects

    # User must give permission to search the defined query on Scholar
    query = f"{author}"
    search_permission = input(f"Permission to search for '{query}' on Scholar using scholarly? ").strip().strip('"')
    if search_permission.lower() == "yes" or search_permission.lower() == "y":
    
        # Get the search results and check if at least one result is found
        search_query = scholarly.search_pubs(query)
        print(f"INFO: Found {search_query.total_results} results for '{query}'.")

        if search_query.total_results >= 1:
            
            no_of_results_to_check = min(search_query.total_results, 25)

            # Cool progress bar to look at while all results are being checked
            with Progress() as p:
                task = p.add_task("Processing author search...", total=no_of_results_to_check)
                    
                # Loop over all results and check if the title (and year) matches
                print(f"   -> INFO: Now checking {no_of_results_to_check} results for matching title: '{title}'")
                for res_i in range(1, no_of_results_to_check):
                    try:
                        # Sleep to avoid getting Bot blocked
                        sleep_time = float(f"0.{random.randint(1, 9)}")
                        time.sleep(sleep_time)
                        current_search_result = next(search_query)
                    except Exception as e:
                        print(f"   -> ERROR - Iterating search results failed: {e}")
                        break

                    pub_title = current_search_result['bib']['title']

                    # During parsing spaces may go missing, so we ignore them when comparing titles
                    if pub_title.replace(" ", "").lower() == title.replace(" ", "").lower():
                        print("   -> INFO: Titles matched!")

                        pub_year = int(current_search_result['bib']['pub_year'].strip())
                        if pub_year == year:
                            print("   -> SUCCESS: Years mateched; reference checks out. :)")
                            p.stop()
                            return False, f"Found: {current_search_result['pub_url']}"
                        else:
                            print(f"   -> ERROR: Year ({pub_year}) does not match expected year ({year})!")
                            print(f"      Manual check required: {current_search_result['pub_url']}")
                            p.stop()
                            return False, f"CHECK - Year did not match: {current_search_result['pub_url']}"
                        
                    #else:
                    #    print(f"   -> ERROR: Title does not match expected title! Trying next search result (if any).")
                    #    print(f"      Expected title: '{title}'")
                    #    print(f"      Current search result's title: '{pub_title}'")

                    p.update(task, advance=1)

                p.stop()

                # If none of them match, do an alternative search with the title
                print(f"   -> ERROR: None of the {no_of_results_to_check} searched author-search-results on Scholar matched the expected title!")
                print(f"   -> Trying a title search now...")
                return False, activate_title_scholar_search(True, author, title, year)

        else:
            print(f"   -> ERROR: Non results were found through the author-search on Scholar; now trying title search instead.")
            return False, activate_title_scholar_search(False, author, title, year)
    else:
        print("Search skipped by user.")
        return True, "Not searched; skipped by user"
    

def search_on_scholar(references_df, index):
    global mismatching_infos_counter
    global skipped_searches_counter
    global no_entry_found_counter
    global invalid_entries

    search_skipped, search_result = activate_author_scholar_search(references_df['authors'].iloc[index], 
                                                                   references_df['title'].iloc[index], 
                                                                   references_df['year'].iloc[index])
    
    # Check return message and set 'valid' column accordingly
    if search_skipped:
        skipped_searches_counter += 1
        references_df.loc[index, 'valid'] = "NOT SEARCHED"
    else:
        if search_result == "Not searched" or search_result.startswith("Found: "):
            references_df.loc[index, 'valid'] = search_result
        elif search_result.startswith("CHECK -"):
            mismatching_infos_counter += 1
            references_df.loc[index, 'valid'] = search_result
            invalid_entries.append(f"{references_df['full_reference'].iloc[index]}; {search_result}")
        else:
            no_entry_found_counter += 1
            references_df.loc[index, 'valid'] = "NOT FOUND"
            invalid_entries.append(references_df['full_reference'].iloc[index])
    
    return references_df



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
       parsed information, as well as some counters for statistics.

    The returned dataframe contains the following columns:
    - 'full_reference', the full reference string before parsing
    - 'authors', a string containing all authors
    - 'title', a string containing the reference's title
    - 'year', an int containing the reference's year (otherwise it's 0)
    - 'outlet', a string containing the reference's outlet
    - 'link', a string containing the reference's link (otherwise it's '')
    - 'valid', a string message indicating the results concering 
               the reference's validity check
    """

    global no_link_provided_counter
    global invalid_link_counter
    global skipped_searches_counter
    global mismatching_infos_counter
    global no_entry_found_counter
    global invalid_entries


    #==========================================================================
    # Get all references from the reference section as separate stings in the 
    # 'references' list
    #==========================================================================
    print(f"Checking references on pages: {ref_starting_page} -- {doc.page_count}")
    references = []

    # NOTE: doc[page_number] is 0-based
    page_text = doc[ref_starting_page-1].get_text()

    # Check if the page contains "References" or "Literature"
    if page_text.find("References") != -1 or page_text.find("Literature") != -1:

        # Find the starting index of the reference section and cut the text before
        if page_text.find("References") != -1:
            ref_starting_index = page_text.find("References")
        else:
            ref_starting_index = page_text.find("Literature")
        page_text = page_text[ref_starting_index:]

        # Extract the references from the first page of the reference section
        references = check_page_text([], page_text, 1)

        # Iterate over all remaining pages and check for remaining references
        for page_no in range(ref_starting_page, doc.page_count):
            page_text = doc[page_no].get_text()
            references = check_page_text(references, page_text, 2)
            page_no += 1

    else:
        print(f"""Could not find 'References'/'Literature' on page {ref_starting_page}. 
                Please check the page number and try again.""")
        # TODO: Maybe ask the user as a fallback for a page number and the header name 
        #       indicating the reference section
    
    # Log the results
    TOTAL_NO_OF_REFERENCES = len(references)
    print(f"All found references: {TOTAL_NO_OF_REFERENCES}")
    

    #==========================================================================
    # Extract information from full reference strings
    #==========================================================================
    reference_components = [parse_reference(e) for e in references]
    # NOTE: The references_df contains the following columns: 
    #       'full_reference', 'authors', 'title', 'year', 'outlet', 'link', 
    #       and 'valid'
    references_df = pd.DataFrame(reference_components)


    #==========================================================================
    # Check if provided links are valid
    #==========================================================================
    for index in range(len(references_df)):
        current_link = references_df['link'].iloc[index]

        # Check if a link is provided; if not, search on Scholar
        if current_link != '':
            # Try to send a HEAD request to the provided link
            try:
                request = requests.head(current_link)
            # Catch invalid links and search for the reference on Scholar instead
            except:
                invalid_link_counter += 1
                local_references_df = search_on_scholar(references_df, index)
                references_df = local_references_df
            # Otherwise, if the link is valid, check its status code after sleeping
            else:
                # Sleep to avoid getting Bot blocked
                sleep_time = float(f"0.{random.randint(1, 9)}")
                time.sleep(sleep_time)
                # Check if site is reachable and set 'valid' column accordingly
                if request.status_code != 404:
                    references_df.loc[index, 'valid'] = f"Link return code = {request.status_code}"
                # Otherwise, if the link is not valid, search for the reference on Scholar instead
                else:
                    invalid_link_counter += 1
                    local_references_df = search_on_scholar(references_df, index)
                    references_df = local_references_df
        else:
            no_link_provided_counter += 1
            local_references_df = search_on_scholar(references_df, index)
            references_df = local_references_df
    

    #==========================================================================
    # Return the final dataframe and values
    #==========================================================================
    return references_df, TOTAL_NO_OF_REFERENCES, no_link_provided_counter, invalid_link_counter, skipped_searches_counter, mismatching_infos_counter, no_entry_found_counter, invalid_entries