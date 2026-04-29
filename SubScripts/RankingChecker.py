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


def check_with_llm(outlet: str, ranking_df: pd.DataFrame, ranking_type: str, is_if: bool):
    """
    check_with_llm checks if the given outlet is in the given ranking dataframe by asking an LLM.
    Returns:
    - a DataFrame containing the outlet information or an empty dataframe
    """
    COLUMN_COUNT = 4

    if not is_if:
        prompt = f"""Are these outlets (names separated by commas) "{outlet}" in the following list of {ranking_type}?
                 If so, at which index and what are the corresponding ratings?
                 {ranking_df.to_string(index=True)}
                 Return ONLY a String of the form: "[['outlet name as given 1', 'title as in the rating 1', index1, 'rating1'], ['outlet name as given 2', 'title as in the rating 2', index2, 'rating2'], ...]"
                 EXAMPLE: "[['ICIS', 'International Conference on Information Systems', 0, 'A'], ['J. of IT', 'Journal of Information Technology', 5, 'B']]"
                 If the outlet is not in the list, return "None" for all {COLUMN_COUNT} fields."""
    else:
        prompt = f"""Are these outlets (names separated by commas) "{outlet}" in the following list of {ranking_type}?
                 If so, at which index and what are the corresponding 'JIF Without Self-Cites'?
                 {ranking_df.to_string(index=True)}
                 Return ONLY a String of the form: "[['outlet name as given 1', 'title as in the if table 1', index1, jif1], ['outlet name as given 2', 'title as in the if table 2', index2, jif2], ...]"
                 EXAMPLE: "[['Nature Rev. Mat.', 'Nature Reviews Materials', 7, 85.9], ['Science', 'SCIENCE', 37, 45.3]]"
                 If the outlet is not in the list, return "None" for all {COLUMN_COUNT} fields."""
    
    # Old Response example:
    # 'outlet=[title as given in the list], index=[index], {rating_or_jif}=[{third_var}]'
    # "outlet=International Conference on Information System..., index=0, rating=A"

    try:
        response = ask_llm.call_campuski(prompt)
    except Exception as e:
        print(f"=> Error calling LLM: {e}")
        return pd.DataFrame()

    # NOTE: The parsing of the LLM response happens using the eval method,
    #       which may be vulnerable to injections!
    try:
        if not is_if:
            df = pd.DataFrame(eval(response), columns=['og_name', 'outlet_name', 'ranking_index', 'ranking'])
        else:
            df = pd.DataFrame(eval(response), columns=['og_name', 'outlet_name', 'ranking_index', 'impact_factor'])
        print("  -> Automatic parsing of LLM DF worked!")
    except Exception as e:
        print(f"=> Error parsing LLM response: {e}")
        print(f"  -> Structurally parsing response as string: {response}")

        response = response.replace("[", "").replace("]", "").replace("\\", "")
        response_splitted = response.split(",")
        if len(response_splitted) % 4 != 0:
            print(f"  -> Warning: The LLM response has not {COLUMN_COUNT} values per outlet; \
                  len(response_splitted) % {COLUMN_COUNT} = {len(response_splitted) % COLUMN_COUNT}")
        
        og_names = []
        outlet_names = []
        ranking_indexes = []
        thirds = []
        for i in range(0, len(response_splitted)):
            element = response_splitted[i].strip()
            element = element.strip('"')
            element = element.strip("'")
            if i % COLUMN_COUNT == 0:
                og_names.append(element)
            elif i % COLUMN_COUNT == 1:
                outlet_names.append(element)
            elif i % COLUMN_COUNT == 2:
                ranking_indexes.append(element)
            else:
                thirds.append(element)

        if not is_if:
            df = pd.DataFrame({
                'og_name': og_names,
                'outlet_name': outlet_names,
                'ranking_index': ranking_indexes,
                'ranking': thirds
            })
        else:
            df = pd.DataFrame({
                'og_name': og_names,
                'outlet_name': outlet_names,
                'ranking_index': ranking_indexes,
                'impact_factor': thirds
            })

    print("  -> LLM DF extracted as follows:")
    print(df)
    return df


def update_outlet_dict_list(outlet_dict_list, unfound_outlets_indexes, og_name, title, ranking, is_jif):
    """
    update_outlet_dict_list iterates through the unfound_ranking_outlets_indexes 
    and tries to find a matching og_name in a dict of outlet_dict_list.
    """

    updated = False
    for index in unfound_outlets_indexes:
        if outlet_dict_list[index]['outlet_name'] == og_name:
            outlet_dict = outlet_dict_list[index]
            outlet_dict['outlet_name'] = title

            if is_jif:
                outlet_dict['impact_factor'] = float(ranking)
            else:
                outlet_dict['ranking'] = ranking

            # Update lists
            unfound_outlets_indexes.remove(index)
            outlet_dict_list[index] = outlet_dict
            updated = True
    
    if not updated:
        print(f"  -> Error while updating {title}'s dict entry with the LLM results: og_name = '{og_name}' didn't match anything!")
    
    return outlet_dict_list, unfound_outlets_indexes




###############################################################################
# Main code
###############################################################################

def main(references_df: pd.DataFrame):
    """
    TODO
    """

    # NOTE: You may disable the fallback of asking an LLM for matching outlets
    #       by setting 'fallback = False'
    fallback = True
    
    print("===============================")
    print("# Starting Ranking Check")
    print("================================")

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
    jq_journal_path = os.path.join(rankings_dir, 'JQ4_WI_journal.xlsx')
    jq_proceedings_path = os.path.join(rankings_dir, 'JQ4_WI_proceedings.xlsx')
    impact_factors_path = os.path.join(rankings_dir, 'impact_factors-2025.xlsx')


    #==========================================================================
    # Check all ranking files are accessible
    #==========================================================================
    jq_jounral_accessibility, e1 = check_file_accessibility(jq_journal_path)
    if not jq_jounral_accessibility:
        print(f"-> ERROR: The journal ranking file is not accessible! {e1}")
        return []
    jq_proceedings_accessibility, e2 = check_file_accessibility(jq_proceedings_path)
    if not jq_proceedings_accessibility:
        print(f"-> ERROR: The proceedings ranking file is not accessible! {e2}")
        return []
    impact_factors_accessibility, e3 = check_file_accessibility(impact_factors_path)
    if not impact_factors_accessibility:
        print(f"-> ERROR: The impact factor ranking file is not accessible! {e3}")
        return []


    #==========================================================================
    # Convert the rankings into dataframes
    #==========================================================================
    jq_journal_df = pd.read_excel(jq_journal_path)
    jq_proceedings_df = pd.read_excel(jq_proceedings_path)
    impact_factors_df = pd.read_excel(impact_factors_path)


    #==========================================================================
    # Check outlets in the rankings
    #==========================================================================
    # Get all unique outlets from the references_df 
    unique_outlets = references_df['outlet'].value_counts()
    print(unique_outlets)
    
    # -> For the JQ Rankings:
    #   - 'Title' contains the journal/conference name
    #   - 'Rating' contains the ranking
    # -> For the Imact Factor Rankings:
    #   - 'Journal Name' contains the journal name
    #   - 'Abbreviated Journal' the Jounral abbriviation (in upparcase)
    #   - 'JIF Without Self-Cites' contains the journal impact factor without self-cites

    # Cool progress bar to look at while all results are being checked
    no_of_results_to_check = len(unique_outlets.index) * \
        (jq_journal_df.shape[0] + jq_proceedings_df.shape[0] + impact_factors_df.shape[0])
    with Progress() as p:
        task = p.add_task("-> Processing initial ranking check...", total=no_of_results_to_check)
                    
        outlet_dict_list = []
        unfound_ranking_outlets_indexes = []
        unfound_jif_outlets_indexes = []
        for outlet in unique_outlets.index:

            outlet_dict = {
                'outlet_name': outlet,
                'ranking': None,
                'impact_factor': None,
                'references': unique_outlets[outlet],
            }
            outlet_found = False
            
            # Search in the JQ Jounral Rankings
            for index, row in jq_journal_df.iterrows():
                if outlet.strip().lower() in row['Title'].strip().lower():
                    outlet_found = True
                    outlet_dict['outlet_name'] = row['Title']
                    outlet_dict['ranking'] = row['Rating']

                    p.update(task, advance=jq_journal_df.shape[0]-index)
                    break
                p.update(task, advance=1)
            
            # Search in the JQ Proceedings Rankings
            for index, row in jq_proceedings_df.iterrows():
                if outlet.strip().lower() in row['Title'].strip().lower():
                    outlet_found = True
                    outlet_dict['outlet_name'] = row['Title']
                    outlet_dict['ranking'] = row['Rating']

                    p.update(task, advance=jq_proceedings_df.shape[0]-index)
                    break
                p.update(task, advance=1)
            
            # If the outlet was not found in any of the rankings, add to unfound 
            # list to check later (given fallback is True)
            if fallback and not outlet_found:
                unfound_ranking_outlets_indexes.append(len(outlet_dict_list)-1)
            
            # Reset outlet_found for the jif search
            outlet_found = False

            # Search in the Journal Impact Factor Rankings
            for index, row in impact_factors_df.iterrows():
                if outlet.strip().lower() in row['Journal Name'].strip().lower():
                    outlet_found = True
                    outlet_dict['outlet_name'] = row['Journal Name']
                    outlet_dict['impact_factor'] = float(row['JIF Without Self-Cites'])

                    p.update(task, advance=impact_factors_df.shape[0]-index)
                    break
                p.update(task, advance=1)

            if fallback and not outlet_found:
                unfound_jif_outlets_indexes.append(len(outlet_dict_list)-1)

            outlet_dict_list.append(outlet_dict)
            print(f"  -> Intial check: {outlet_dict['outlet_name']} -- {outlet_dict['ranking']} -- {outlet_dict['impact_factor']}")
    
        p.stop()

    # Fallback LLM check
    if fallback:

        # Cool progress bar to look at while all results are being checked
        no_of_results_to_check = 3 + 2 * len(unfound_ranking_outlets_indexes) + len(unfound_jif_outlets_indexes)
        with Progress() as p:
            task = p.add_task("-> Processing LLM ranking check...", total=no_of_results_to_check)
                 
            # Get all names of the unfound outlets in one string
            outlet_names_to_search = ""
            for i in range(0, len(unfound_ranking_outlets_indexes)):
                if i > 0:
                    outlet_names_to_search += ", "
                outlet_dict = outlet_dict_list[unfound_ranking_outlets_indexes[i]]
                outlet_names_to_search += str(outlet_dict['outlet_name'])
            
            p.update(task, advance=1)

            # First, check for the outlets in the JQ proceedings ranking
            # Example row of the llm_check_df = [0, 'ICIS', 'International Conference on Information Systems', 0, 'A']
            llm_check_df = check_with_llm(outlet_names_to_search, jq_proceedings_df, "proceedings rankings", False)
            for row in llm_check_df.itertuples():
                og_name = row[1]
                title = row[2]
                ranking = row[3]

                if og_name and "None" not in og_name and ranking and "None" not in ranking:
                    outlet_dict_list, unfound_ranking_outlets_indexes = update_outlet_dict_list(outlet_dict_list, unfound_ranking_outlets_indexes, og_name, title, ranking, False)
                p.update(task, advance=1)

            # Update the still unfound outlets string
            outlet_names_to_search = ""
            for i in range(0, len(unfound_ranking_outlets_indexes)):
                if i > 0:
                    outlet_names_to_search += ", "
                outlet_dict = outlet_dict_list[unfound_ranking_outlets_indexes[i]]
                outlet_names_to_search += str(outlet_dict['outlet_name'])
            
            p.update(task, advance=1)

            # Second, check for the outlets in the JQ journal ranking
            # -> Now that proceedings are already done, the reamining unfound outlets should be journals
            #    where we want to check the ranking and the journal impact factor
            llm_check_df = check_with_llm(outlet_names_to_search, jq_journal_df, "journal rankings", False)
            for row in llm_check_df.itertuples():
                og_name = row[1]
                title = row[2]
                ranking = row[4]

                if og_name and "None" not in og_name and ranking and "None" not in ranking:
                    outlet_dict_list, unfound_ranking_outlets_indexes = update_outlet_dict_list(outlet_dict_list, unfound_ranking_outlets_indexes, og_name, title, ranking, False)
                p.update(task, advance=1)

            # Get the unfound jif outlets string
            outlet_names_to_search = ""
            for i in range(0, len(unfound_jif_outlets_indexes)):
                if i > 0:
                    outlet_names_to_search += ", "
                outlet_dict = outlet_dict_list[unfound_jif_outlets_indexes[i]]
                outlet_names_to_search += str(outlet_dict['outlet_name'])

            p.update(task, advance=1)

            # Third, check for the outlets in the journal impact factor ranking
            # TODO: The impact_factor-2025 Excel seems to large to be processed by the LLM!
            # Example row of the llm_check_df = [0, 'Nat. Rev. Mat.', 'Nature Reviews Materials', 7, 85.9]
            llm_check_df = check_with_llm(outlet_names_to_search, impact_factors_df, "journal impact factors", True)
            for row in llm_check_df.itertuples():
                og_name = row[1]
                title = row[2]
                jif = row[4]

                if og_name and "None" not in og_name and jif and "None" not in jif:
                    outlet_dict_list, unfound_jif_outlets_indexes = update_outlet_dict_list(outlet_dict_list, unfound_jif_outlets_indexes, og_name, title, jif, True)
                p.update(task, advance=1)

            p.stop()

    print("---")
    print(outlet_dict_list)
    return outlet_dict_list
    

    


