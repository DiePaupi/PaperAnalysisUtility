###############################################################################
# Imports
###############################################################################
import pandas as pd
from rich.progress import Progress
import random
from scholarly import scholarly
import time



###############################################################################
# INFO
###############################################################################

# Google Scholar API:
    # NOTE: Prefer DOIs and URLs over a google scholar search
    # https://stackoverflow.com/questions/62938110/does-google-scholar-have-an-api-available-that-we-can-use-in-our-research-applic
    # current_search_result['bib']['author']
    # current_search_result['author_id']
    # current_search_result['bib']['title']
    # current_search_result['bib']['pub_year']
    # current_search_result['bib']['abstract']
    # current_search_result['bib']['venue']
    # current_search_result['num_citations']
    # current_search_result['pub_url']
    # current_search_result['eprint_url']



###############################################################################
# Gloal Variables
###############################################################################

# NOTE: MAX_SCHOLAR_ENTRIES_TO_CHECK needs to be >= 11
MAX_SCHOLAR_ENTRIES_TO_CHECK = 25


###############################################################################
# Helper functions
###############################################################################

def activate_scholar_search(query, title, authors, year, entries_to_check):
    """
    activate_scholar_search takes:
       - A query (str) to be searched on Scholar
       - The expected title (str) of the paper to be found
       - The expected authors (str) of the paper to be found
       - The expected year (int) of the paper to be found
       - A number of entries to check (int) that defines how many of the 
         search results should be checked for a match
    The function searches the query on Scholar, checks max. entries_to_check 
      for a matching title, then for matching authors, and finally for a
      matching year.
    Returns:
       - A Bool indicating if the search was skipped by the user
       - A message to be logged in the 'valid' column of the reference's entry 
         in the dataframe
       - The abstract of the found paper (if any) to be logged in the
         'abstract' column of the reference's entry in the dataframe
    """
    
    # User must give permission to search the defined query on Scholar
    search_permission = input(f"   -> Permission to search for '{query}' on Scholar using scholarly? ").strip().strip('"')
    if search_permission.lower() == "yes" or search_permission.lower() == "y":
    
        # Get the search results and check if at least one result is found
        search_query = scholarly.search_pubs(query)
        print(f"   -> INFO: Found {search_query.total_results} results for '{query}'.")

        if search_query.total_results >= 1:
            
            no_of_results_to_check = min(search_query.total_results, entries_to_check)
            print(f"   -> INFO: Now checking {no_of_results_to_check} results for matching title: '{title}'")

            # Cool progress bar to look at while all results are being checked
            with Progress() as p:
                task = p.add_task("   -> Processing scholar search...", total=no_of_results_to_check)
                    
                # Loop over all results and check if the title (and year) matches
                for res_i in range(0, no_of_results_to_check):
                    try:
                        # Sleep to avoid getting Bot blocked
                        sleep_time = float(f"0.{random.randint(1, 9)}")
                        time.sleep(sleep_time)
                        current_search_result = next(search_query)
                    except Exception as e:
                        message = f"ERROR - Getting search results failed: {e}"
                        print(f"   -> {message}")
                        return False, message, None

                    # Compare titles
                    pub_title = current_search_result['bib']['title']
                    # NOTE: During parsing spaces may go missing, so we ignore them when comparing titles
                    if pub_title.replace(" ", "").lower() == title.replace(" ", "").lower():
                        print("   -> INFO: Titles matched!")

                        # Compare authors
                        # NOTE: current_search_result['bib']['author'] -> Each entry has the form "C Janiesch"
                        pub_bib_authors = current_search_result['bib']['author']
                        for pub_author in pub_bib_authors:
                            lastname = pub_author.split(" ")[1].strip().lower()
                            if not lastname in authors.lower():
                                print(f"     -> ERROR: Lastname ({lastname}) does not match any expected authors' ({authors.lower()})!")
                                print(f"        Manual check required: {current_search_result['pub_url']}")
                                p.stop()
                                return False, f"CHECK - Authors did not match: {current_search_result['pub_url']}", current_search_result['bib']['abstract']

                        # Compare years
                        pub_year = int(current_search_result['bib']['pub_year'].strip())
                        if pub_year == year:
                            print("   -> SUCCESS: Years mateched; reference checks out. :)")
                            p.stop()
                            # TODO: Outlet Quality Check
                            return False, f"Found: {current_search_result['pub_url']}", current_search_result['bib']['abstract']
                        else:
                            print(f"   -> ERROR: Year ({pub_year}) does not match expected year ({year})!")
                            print(f"      Manual check required: {current_search_result['pub_url']}")
                            p.stop()
                            return False, f"CHECK - Years did not match: {current_search_result['pub_url']}", current_search_result['bib']['abstract']
                        
                    #else:
                    #    print(f"   -> ERROR: Title does not match expected title! Trying next search result (if any).")
                    #    print(f"      Expected title: '{title}'")
                    #    print(f"      Current search result's title: '{pub_title}'")

                    p.update(task, advance=1)

                p.stop()

                # If none of them match, return False
                message = f"ERROR: None of the {no_of_results_to_check} searched Scholar-results matched the expected title!"
                print(f"   -> {message}")
                return False, message, None

        else:
            #message = f"ERROR: No results were found through the search on Scholar!"
            print(f"   -> {message}")
            return False, message, None
    else:
        message = "Search was skipped by the user."
        print(f"   -> {message}")
        return True, message, None



###############################################################################
# Main code
###############################################################################

def search_on_scholar(p_references_df, index, link):
    """
    search_on_scholar takes the dataframe containing the reference information 
    and the index of the current reference as input and calls 
    activate_scholar_search with the reference's query, title, authors, year, 
    and number of entries to check.
    After the search, it checks the returned message and updates the 'valid' 
    column of the reference accordingly, as well as the global counters and 
    lists of entries for the final log.
    The updated dataframe is returned.
    """

    global MAX_SCHOLAR_ENTRIES_TO_CHECK

    no_link_provided_counter = 0
    valid_link_counter = 0
    invalid_link_counter = 0

    skipped_searches_counter = 0
    successful_searches_counter = 0
    mismatching_infos_counter = 0
    no_entry_found_counter = 0

    mismatching_entries = []
    unfound_entries = []

    title_to_find = p_references_df.at[index, 'title']
    authors_to_find = p_references_df.at[index, 'authors']
    year_to_find = int(p_references_df.at[index, 'year'])

    # If a link is given, we want to search for it first, otherwise we search for the author and year
    if link:
        query = f'pub_url:"{link}"'
        entries_to_check = 1
    else:
        # If no link is provided, the counter is already set in the calling function
        query = f'{authors_to_find} {year_to_find}'
        entries_to_check = MAX_SCHOLAR_ENTRIES_TO_CHECK

    # Execute the link or author+year Scholar search
    search_skipped, search_message, abstract = activate_scholar_search(query,
                                                                      title_to_find,
                                                                      authors_to_find,
                                                                      year_to_find,
                                                                      entries_to_check)

    # Check if the search was skipped by the user, otherwise, check the search results
    if search_skipped:
        skipped_searches_counter += 1
        p_references_df.at[index, 'valid'] = "NOT SEARCHED"
    else:
        # If the search was successful:
        if search_message.startswith("Found: "):
            if link:
                valid_link_counter += 1
            
            successful_searches_counter += 1
            p_references_df.at[index, 'valid'] = search_message
            p_references_df.at[index, 'abstract'] = abstract
        # If the search revealed mismatching entries:
        elif search_message.startswith("CHECK -"):
            if link:
                valid_link_counter += 1

            mismatching_infos_counter += 1
            p_references_df.at[index, 'valid'] = search_message
            p_references_df.at[index, 'abstract'] = abstract
            mismatching_entries.append(f"{p_references_df.at[index, 'full_reference']}\n      -> {search_message}")
        # If an error occured or no results were found:
        else:

            # If a link was searched first, now do the author+year search
            if link:
                invalid_link_counter += 1
                query = f'{authors_to_find} {year_to_find}'
                entries_to_check = MAX_SCHOLAR_ENTRIES_TO_CHECK
                snd_skipped_message = "The authors+year search was skipped"
            # Otherwise do a title search
            else:
                query = f'{title_to_find}'
                entries_to_check = MAX_SCHOLAR_ENTRIES_TO_CHECK-10
                snd_skipped_message = "The title search was skipped"

            # Execute the auhtors+year or title Scholar search
            snd_search_skipped, snd_search_message, snd_abstract = activate_scholar_search(query,
                                                                                           title_to_find,
                                                                                           authors_to_find,
                                                                                           year_to_find,
                                                                                           entries_to_check)

            # Check if the search was skipped by the user, otherwise, check the search results
            if snd_search_skipped:
                skipped_searches_counter += 1
                p_references_df.at[index, 'valid'] = f"{snd_skipped_message}; the previous did not yield any results"
            else:
                # If the 2nd search was successful:
                if snd_search_message.startswith("Found: "):
                    successful_searches_counter += 1
                    p_references_df.at[index, 'valid'] = snd_search_message
                    p_references_df.at[index, 'abstract'] = snd_abstract
                # If the search revealed mismatching entries:
                elif snd_search_message.startswith("CHECK -"):
                    mismatching_infos_counter += 1
                    p_references_df.at[index, 'valid'] = snd_search_message
                    p_references_df.at[index, 'abstract'] = snd_abstract
                    mismatching_entries.append(f"{p_references_df.at[index, 'full_reference']}\n      -> {snd_search_message}")
                # If an error occured or no results were found:
                else:

                    # If a link was searched first, finally do the title search
                    if link:
                        query = f'{title_to_find}'
                        entries_to_check = MAX_SCHOLAR_ENTRIES_TO_CHECK-10
                        trd_skipped_message = "The title search was skipped"

                        # Execute the title Scholar search
                        trd_search_skipped, trd_search_message, trd_abstract = activate_scholar_search(query,
                                                                                                    title_to_find,
                                                                                                    authors_to_find,
                                                                                                    year_to_find,
                                                                                                    entries_to_check)

                        # Check if the search was skipped by the user, otherwise, check the search results
                        if trd_search_skipped:
                            skipped_searches_counter += 1
                            p_references_df.at[index, 'valid'] = f"{trd_skipped_message}; the previous did not yield any results"
                        else:
                            # If the 3rd search was successful:
                            if trd_search_message.startswith("Found: "):
                                successful_searches_counter += 1
                                p_references_df.at[index, 'valid'] = trd_search_message
                                p_references_df.at[index, 'abstract'] = trd_abstract
                            # If the search revealed mismatching entries:
                            elif trd_search_message.startswith("CHECK -"):
                                mismatching_infos_counter += 1
                                p_references_df.at[index, 'valid'] = trd_search_message
                                p_references_df.at[index, 'abstract'] = trd_abstract
                                mismatching_entries.append(f"{p_references_df.at[index, 'full_reference']}\n      -> {trd_search_message}")
                            # If an error occured or no results were found:
                            else:
                                no_entry_found_counter += 1
                                p_references_df.at[index, 'valid'] = trd_search_message
                                unfound_entries.append(f"{p_references_df.at[index, 'full_reference']}\n      -> {trd_search_message}")
                    
                    # This is if the 2nd search (no link provided) did not yield any results
                    else:
                        no_entry_found_counter += 1
                        p_references_df.at[index, 'valid'] = snd_search_message
                        mismatching_entries.append(f"{p_references_df.at[index, 'full_reference']}\n      -> {snd_search_message}")

    stats = {
        'valid_links': valid_link_counter,
        "invalid_links": invalid_link_counter,
        "skipped_searches": skipped_searches_counter,
        "successful_searches": successful_searches_counter,
        "mismatching_infos": mismatching_infos_counter,
        "no_entry_found": no_entry_found_counter
    }
    return p_references_df, stats