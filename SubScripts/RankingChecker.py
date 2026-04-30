###############################################################################
# Imports
###############################################################################
# NOTE: You will also need to install "openpyxl" and "xlrd"
import os
from pathlib import Path
from matplotlib.pyplot import title
import pandas as pd
from rich.progress import Progress
from openpyxl import load_workbook

from . import LLMCaller as ask_llm



###############################################################################
# INFO
###############################################################################



###############################################################################
# Gloal Variables
###############################################################################



###############################################################################
# Helper functions
###############################################################################

def check_file_accessibility(file_path: Path):
    """
    check_file_accessibility checks if the file at the given path exists and is accessible.
    RETURNS:
    - a Bool indicating if the file is accessible
    - a String message with more details on the result
    """

    # Check if the file exists
    if os.path.exists(file_path):
        return True, "File exists and is accessible."
    
    # The file does not exists but write privileges are given
    elif os.access(os.path.dirname(file_path), os.W_OK):
        return False, "The stated path does not seem to exist!"
    
    # Read/Write privileges are not given (e.g., in OneDrive folders)
    else:
        return False, "You do not have write privileges in the directory of the file!"


def check_ranking_for_outlets(ranking_df: pd.DataFrame, title_col: str, rating_col: str, \
                              outlets_df: pd.DataFrame, ranking_type: str) -> pd.DataFrame:
    """
    check_ranking_for_outlets takes 
     - a DF of the rankings, the according title column name, the according rating column name
     - the outlet DF and the corresponding column name of the rating to be stored under.
    The function iterates over the ranking_df (outer) and outlets_df (inner) trying to match
    the titles (parsed_name vs title as in the ranking_df).
    Returns:
    - an updated outlets_df
    """

    # Cool progress bar to look at while all results are being checked
    check_count = (ranking_df.shape[0] * outlets_df.shape[0])
    with Progress() as p:
        task = p.add_task(f"  -> Processing initial {ranking_type} check...", total=check_count)

        matches = 0

        # Iterate over the rankings_df, since it is very likly to be much larger
        # Note: since the exact layout of the ratings_df varies, we need to use iterrows
        for r_index, r_row in ranking_df.iterrows():
            r_title = str(r_row[title_col])

            # outlets_df layout: 0=index, 1=parsed_name, 2=outlet_name, 3=jq_ranking,
            #                    4=core_ranking, 5=impact_factor, 6=references_count
            # Note: To be able to easily add new ranking types, we're gonna use iterrows
            #       here to, so we can access the fields by column name
            for o_index, o_row in outlets_df.iterrows():
                o_title = str(o_row['parsed_name'])
                if o_title != 'nan' and o_title != 'NaN':
                    if o_title.strip().lower() in r_title.strip().lower():
                        matches += 1
                        if o_row[ranking_type] == 'unknown':
                            outlets_df.at[o_index, 'outlet_name'] = r_title
                            outlets_df.at[o_index, ranking_type] = r_row[rating_col].strip()
                        #else:
                            #print(f"  -> outlets_df['{ranking_type}'] already has an entry for {r_title}! Skipping!")
                else:
                    print(f"  -> WARNING: o_title (o_index = {o_index}) was parsed as 'not a number'! Skipping!")
                p.update(task, advance=1)

        p.stop()
        print(f"  -> Found {matches} matches in this ranking!")
    
    return outlets_df


def check_with_llm(outlets: str, ranking_df: pd.DataFrame, rating_col: str, ranking_type: str) \
    -> pd.DataFrame:
    """
    check_with_llm checks if the given outlets are in the given ranking dataframe by prompting
      an LLM to match the titles.
    Returns:
    - a DataFrame containing the outlet information or an empty dataframe
    """
    COLUMN_COUNT = 3

    prompt = f"""Are these outlets (names separated by commas) "{outlets}" in the list of rankings blow?
                If so, what are the corresponding {rating_col}?
                Return ONLY a String of the form: [["outlet name as given 1", "title as in the ranking 1", "ranking1"], ["outlet name as given 2", "title as in the ranking 2", "ranking2"], ...]
                EXAMPLE: [["ICIS", "International Conference on Information Systems", "A"], ["Nature Rev. Mat.", "Nature Reviews Materials", 85.9]]
                If the outlet is not in the list, return "unknown" for the "title as in the ranking 1" and "ranking1" fields.
                
                List of rankings:
                {ranking_df.to_string(index=True)}"""

    try:
        response = ask_llm.call_campuski(prompt)
    except Exception as e:
        print(f"  => ERROR calling LLM: {e}")
        return pd.DataFrame()
    
    if response == "[]":
        print(f"  => ERROR: LLM Response empty! Returning empty DataFrame...")
        return pd.DataFrame()
    
    # Prepare response
    response = response.replace("\'", '"')
    response = response.strip("'").strip('"')
    # -> '—' (U+2014) seems to be an invalid character
    response = response.replace('\u2014', '-')

    strcuture_parsing_necessary = False
    # NOTE: The parsing of the LLM response happens using the eval method,
    #       which may be vulnerable to injections!
    try:
        df = pd.DataFrame(eval(response), columns=['parsed_name', 'outlet_name', ranking_type])
        print("  -> Automatic parsing of LLM DF worked!")
        return df
    except ValueError as ev:
        print(f"  => WARNING: A Value Error occured during parsing: {ev}")
        print(f"     Structurally parsing response as string: {response}")
        strcuture_parsing_necessary = True
    except SyntaxError as es:
        print(f"  => WARNING: A Syntax Error occured during parsing: {es}")
        print(f"     Structurally parsing response as string: {response}")
        strcuture_parsing_necessary = True
    except Exception as ee:
        print(f"  => WARNING: Parsing LLM response failed: {ee}")
        print(f"     Structurally parsing response as string: {response}")
        strcuture_parsing_necessary = True

    if strcuture_parsing_necessary:
        # Clean up the response string
        response = response.replace("[", "").replace("]", "")
        response = response.replace("\\", "").replace("\'", "")
        response_splitted = response.split(",")

        # Sanity Check
        if len(response_splitted) % COLUMN_COUNT != 0:
            print(f"  -> Warning: The LLM response has not {COLUMN_COUNT} values per outlet; \
                  len(response_splitted) % {COLUMN_COUNT} = {len(response_splitted) % COLUMN_COUNT}")
        
        parsed_names = []
        outlet_names = []
        thirds = []
        for i in range(0, len(response_splitted)):
            element = response_splitted[i].strip()
            element = element.strip('"')
            element = element.strip("'")
            if i % COLUMN_COUNT == 0:
                parsed_names.append(element)
            elif i % COLUMN_COUNT == 1:
                outlet_names.append(element)
            else:
                thirds.append(element)

        df = pd.DataFrame({
            'parsed_name': parsed_names,
            'outlet_name': outlet_names,
            ranking_type: thirds
        })

    #print("  -> LLM DF extracted as follows:")
    #print(df)
    return df


def fallback_check_ranking(ranking_df: pd.DataFrame, rating_col: str, \
                           outlets_df: pd.DataFrame, ranking_type: str) -> pd.DataFrame:
    """
    fallback_check_ranking takes a ranking_df and a corresponding column name for the Rating-title,
      the outlet_df and the corresponding name of the ranking entry in it.
    The function checks which outlets in the outlet_df still have no entry in the ranking column,
      and prompts an LLM to check the originally parsed outlet names against the ranking_df titles.
      Thereafter, it iterates through the outlet_df (outer loop) and the DF generated through the
      LLM response (inner loop) and tries to match the titles. When they match, the outlet_name
      and the reating are updated in the outlet_df.
    Returns:
      - the updated outlet_df
    """

    # Get all entries that are still missing a ranking entry 
    #     (i.e., that couldn't be matched so far)
    unfound_outlet_df = outlets_df[outlets_df[ranking_type] == 'unknown']

    if unfound_outlet_df.shape[0] == 0:
        print("  -> No unfound outlets, so fallback is not needed!")
        return outlets_df
    
    # Cool progress bar to look at while all results are being checked
    check_count = 1 + unfound_outlet_df.shape[0] + (outlets_df.shape[0] * unfound_outlet_df.shape[0])
    with Progress() as p:
        task = p.add_task(f"  -> Processing LLM {ranking_type} check...", total=check_count)

        # Get all names of the unfound outlets in one string and 
        outlet_names_to_search = ""
        for i, row in unfound_outlet_df.iterrows():
            if i > 0:
                outlet_names_to_search += ", "
            outlet_names_to_search += unfound_outlet_df.at[i,'parsed_name']
        
            p.update(task, advance=1)

        # Prompt an LLM to match the missing entries against the rankings
        # Example row of the llm_check_df = [0, 'ICIS', 'International Conference on Information Systems', 0, 'A']
        llm_check_df = check_with_llm(outlet_names_to_search, ranking_df, rating_col, ranking_type)
        p.update(task, advance=1)

        # Iterate over the outlets_df, trying to match the originally parsed name, and update 
        # the outlet_name and ranking accordingly
        for o_index, o_row in outlets_df.iterrows():

            # llm_check_df layout: 0=index, 1='parsed_name', 2='outlet_name', 3=ranking_type
            for llm_index, llm_row in llm_check_df.iterrows():

                if o_row['parsed_name'] == llm_row['parsed_name']:
                    title = llm_row['outlet_name']
                    ranking = llm_row[ranking_type]

                    if title and 'unknown' not in title and ranking and 'unknown' not in ranking:
                        outlets_df.at[o_index, 'outlet_name'] = title
                        outlets_df.at[o_index, ranking_type] = ranking
                    
                p.update(task, advance=1)
        
        p.stop()
    
    #print("  -> Updated outlets_df:")
    #print(outlets_df)
    return outlets_df



###############################################################################
# Main code
###############################################################################

def main(references_df: pd.DataFrame):
    """
    TODO
    """

    print("###############################")
    print("# Starting Ranking Check")
    print("###############################")
    
    skip_llm_fallbback = input("=> To skip the LLM Ranking Fallback Check, type 'skip': ").strip()
    if skip_llm_fallbback.lower() == "skip":
        fallback = False
    else:
        fallback = True


    #==========================================================================
    # Get all Excel Ranking Files
    #==========================================================================
    # Your current directory (including python script & all excel files)

    current_dir = Path((os.getcwd()).replace('\\','/'))
    print(f"- Current directory: {current_dir}")
    sup_dir = os.path.split(current_dir)[0]
    rankings_dir = os.path.join(sup_dir, 'Rankings')
    print(f"  Rankings directory: {rankings_dir}")

    # Define all excel ranking file paths

    # NOTE: VHB Publication Media Rating 2024 Section Wirtschaftsinformatik / Information Systems from VHB
    # https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik
    jq_journal_path = os.path.join(rankings_dir, 'JQ4_WI_journal.xlsx')
    jq_proceedings_path = os.path.join(rankings_dir, 'JQ4_WI_proceedings.xlsx')

    # NOTE: CORE Conference Rankings 2026 from ICORE
    # https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1
    core_AB_ranking_path = os.path.join(rankings_dir, 'CORE_ranking_AtoB.xlsx')
    core_C_ranking_path = os.path.join(rankings_dir, 'CORE_ranking_C.xlsx')
    core_rest_ranking_path = os.path.join(rankings_dir, 'CORE_ranking_Rest.xlsx')

    # NOTE: Journal Impact Factors 2025 from Clarivate
    # https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/
    impact_factors_path = os.path.join(rankings_dir, 'impact_factors-2025.xlsx')


    #==========================================================================
    # Check all ranking files are accessible
    #==========================================================================
    jq_jounral_accessibility, e = check_file_accessibility(jq_journal_path)
    if not jq_jounral_accessibility:
        print(f"-> ERROR: The JQ journal ranking file is not accessible! {e}")
        return []
    jq_proceedings_accessibility, e = check_file_accessibility(jq_proceedings_path)
    if not jq_proceedings_accessibility:
        print(f"-> ERROR: The JQ proceedings ranking file is not accessible! {e}")
        return []
    core_AB_accessibility, e = check_file_accessibility(core_AB_ranking_path)
    if not core_AB_accessibility:
        print(f"-> ERROR: The CORE_AB ranking file is not accessible! {e}")
        return []
    core_C_accessibility, e = check_file_accessibility(core_C_ranking_path)
    if not core_C_accessibility:
        print(f"-> ERROR: The CORE_C ranking file is not accessible! {e}")
        return []
    core_rest_accessibility, e = check_file_accessibility(core_rest_ranking_path)
    if not core_rest_accessibility:
        print(f"-> ERROR: The CORE_Rest ranking file is not accessible! {e}")
        return []
    impact_factors_accessibility, e = check_file_accessibility(impact_factors_path)
    if not impact_factors_accessibility:
        print(f"-> ERROR: The impact factor ranking file is not accessible! {e}")
        return []


    #==========================================================================
    # Convert the rankings into dataframes
    #==========================================================================
    print("-> Loading rankings and iterating them; please wait, this might take a minute!")
    jq_journal_df = pd.read_excel(jq_journal_path)
    jq_proceedings_df = pd.read_excel(jq_proceedings_path)
    core_ab_df = pd.read_excel(core_AB_ranking_path)
    core_c_df = pd.read_excel(core_C_ranking_path)
    core_rest_df = pd.read_excel(core_rest_ranking_path)
    impact_factors_df = pd.read_excel(impact_factors_path)


    #==========================================================================
    # Check outlets in the rankings
    #==========================================================================
    # Get all unique outlets from the references_df 
    unique_outlets = references_df['outlet'].value_counts()
    #print(unique_outlets)
    
    # -> For the JQ Rankings:
    #   - 'Title' contains the journal/conference name
    #   - 'Rating' contains the ranking
    # -> For the CORE Rankings the column headers are self set to:
    #   - 'Title' contains the journal/conference name
    #   - 'Acronym' contains the journal/conference abbriviation (in upparcase)
    #   - 'Rating' contains the ranking
    # -> For the Imact Factor Rankings:
    #   - 'Journal Name' contains the journal name
    #   - 'Abbreviated Journal' the Jounral abbriviation (in upparcase)
    #   - 'JIF Without Self-Cites' contains the journal impact factor without self-cites


    #--------------------------------------------------------------------------
    # Create initial outlet dicts
    #--------------------------------------------------------------------------
    outlet_dict_list = []
    for outlet in unique_outlets.index:
        if not outlet or outlet.strip() == '':
            print(f"  -> Warning: A parsed outlet title is empty. Skipping this one.")
        else:
            outlet_dict = {
                'parsed_name': outlet,
                'outlet_name': 'unknown',
                'jq_ranking': 'unknown',
                'core_ranking': 'unknown',
                'impact_factor': 'unknown',
                'references_count': unique_outlets[outlet],
            }
            outlet_dict_list.append(outlet_dict)
    outlets_df = pd.DataFrame(outlet_dict_list)


    #--------------------------------------------------------------------------
    # Check ranking_df(s)
    #--------------------------------------------------------------------------
    print(f"-> Now checking the JQ proceedings:")
    outlets_df = check_ranking_for_outlets(jq_proceedings_df, 'Title', 'Rating', \
                                           outlets_df, 'jq_ranking')
    
    print(f"-> Now checking the JQ jounrals:")
    outlets_df = check_ranking_for_outlets(jq_journal_df, 'Title', 'Rating', \
                                           outlets_df, 'jq_ranking')
    
    print(f"-> Now checking the CORE A+ - B rankings:")
    outlets_df = check_ranking_for_outlets(core_ab_df, 'Title', 'Rating', \
                                           outlets_df, 'core_ranking')
    
    print(f"-> Now checking the CORE C rankings:")
    outlets_df = check_ranking_for_outlets(core_c_df, 'Title', 'Rating', \
                                           outlets_df, 'core_ranking')
    
    print(f"-> Now checking the remaining CORE rankings:")
    outlets_df = check_ranking_for_outlets(core_rest_df, 'Title', 'Rating', \
                                           outlets_df, 'core_ranking')
    
    print(f"-> Now checking the journal impact factors:")
    outlets_df = check_ranking_for_outlets(impact_factors_df, 'Journal Name', \
                                           'JIF Without Self-Cites', \
                                           outlets_df, 'impact_factor')


    #==========================================================================
    # Fallback: Check yet unmatched outlets with an LLM against the sources
    #==========================================================================
    if fallback:

        print(f"-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:")
        outlets_df = fallback_check_ranking(jq_proceedings_df, 'Rating', outlets_df, 'jq_ranking')

        print(f"-> Now matching the JQ jounrals and the parsed outlets using an LLM:")
        outlets_df = fallback_check_ranking(jq_journal_df, 'Rating', outlets_df, 'jq_ranking')
        
        print(f"-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:")
        outlets_df = fallback_check_ranking(core_ab_df, 'Rating', outlets_df, 'core_ranking')
        
        print(f"-> Now matching the CORE C rankings and the parsed outlets using an LLM:")
        outlets_df = fallback_check_ranking(core_c_df, 'Rating', outlets_df, 'core_ranking')
        
        print(f"-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:")
        outlets_df = fallback_check_ranking(core_rest_df, 'Rating', outlets_df, 'core_ranking')
        
        # TODO: The impact_factor-2025 Excel seems to large to be processed by the LLM!
        print(f"-> Now matching the journal impact factors and the parsed outlets using an LLM:")
        outlets_df = fallback_check_ranking(impact_factors_df, 'JIF Without Self-Cites', outlets_df, 'impact_factor')
            

    #print("---")
    #print(outlets_df)
    return outlets_df
    

    


