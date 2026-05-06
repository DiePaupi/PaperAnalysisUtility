###############################################################################
# Imports
###############################################################################
import pandas as pd
from rich.progress import Progress

from . import LLMCaller as ask_llm



###############################################################################
# INFO
###############################################################################

# Numeric References
    #   citet = "Barredo Arrieta et al. [2]"
    #   citep = multiple "[11, 18, 29]"
    #   citep = single "[17]"
    # => Check number

# Authoryear References
    #   citet = "Piorkowski et al. (2021)"
    #   citep = multiple "(Wischnewski et al. 2024; Scharowski et al. 2023)"
    #   citep = single "(Kaur et al. 2020)"
    # => Check for first author name and year



###############################################################################
# Gloal Variables
###############################################################################

EDUCATED_GUESS_ON_SENTENCES_PER_PAGE = 27

# Referencing Style Specifics
NUMERIC_REF_STYLE = "numeric"
numeric_referencing = {
    "name": NUMERIC_REF_STYLE,
    "opening_bracket": "[",
    "closing_bracket": "]",
    "separator": ","
}
AUTHORYEAR_REF_STYLE = "authoryear"
authoryear_referencing = {
    "name": AUTHORYEAR_REF_STYLE,
    "opening_bracket": "(",
    "closing_bracket": ")",
    "separator": ";"
}
supported_ref_templates = [numeric_referencing, authoryear_referencing]


###############################################################################
# Helper functions
###############################################################################

def get_supported_ref_templates():
    return supported_ref_templates


def check_with_llm(abstract: str, p_sentences: list) -> list:
    """
    TODO
    """

    COLUMN_COUNT = 3
    prompt = "I will give you an abstract of a paper and a list of tuples, " \
             "where the first element is a sentence, " \
             "the second is a Bool indicating if the abstract is thematically " \
             "related/relevant to the sentence (default is False), and " \
             "the third element indicates the stance, i.e., if the abstract " \
             "supports or refutes the statement made in the sentence " \
             "(default 'unkown').-nl-" \
             "Please check each sentence and assess if the abstract is thematically " \
             "related/relevant to the sentence and if the paper (based on the abstract) " \
             "supports the sentence's statement, refutes the sentence's statement, " \
             "or if the abstract doesn't provide enough information to clearly say " \
             "it supports or refutes the sentence's statement.-nl- " \
             "Please return the input list of tuples with the default values overwritten " \
             "by your assessment. " \
             "So the sentence stays the same, the Bool is either True or False, and the " \
             "third element is either 'supports', 'refutes', or " \
             "'not enough information'.-nl- " \
             "--- -nl- " \
             "This is the abstrackt of a paper:-nl- " \
             f"{abstract}-nl- " \
             "--- -nl- " \
             "This is the list of (sentence, Bool, stance)-tuples:-nl- " \
             f"{p_sentences} "
    
    prompt = prompt.replace("-nl-", "\n")

    try:
        response = ask_llm.call_llm(prompt)
    except Exception as e:
        print(f"  => ERROR calling LLM: {e}")
        return []
    
    if len(response) <= 4:
        print(f"  => ERROR: LLM Response empty! Returning empty DataFrame...")
        return []
    
    # Prepare response
    response = response.replace("\'", '"')
    response = response.strip("'").strip('"')
    # -> '—' (U+2014) seems to be an invalid character
    response = response.replace('\u2014', '-')

    # NOTE: The parsing of the LLM response happens using the eval method,
    #       which may be vulnerable to injections!
    try:
        llm_list = eval(response)
        print("  -> Automatic parsing of LLM list worked!")
        return llm_list
    except ValueError as ev:
        print(f"  => WARNING: A Value Error occured during parsing: {ev}")
        print(f"     Structurally parsing response as string: {response}")
    except SyntaxError as es:
        print(f"  => WARNING: A Syntax Error occured during parsing: {es}")
        print(f"     Structurally parsing response as string: {response}")
    except Exception as ee:
        print(f"  => WARNING: Parsing LLM response failed: {ee}")
        print(f"     Structurally parsing response as string: {response}")
    
    # Clean up the response string
    response = response.replace("[", "").replace("]", "")
    response = response.replace("\\", "").replace("\'", "")
    # TODO: This may break if the sentence contains a , ???
    response_splitted = response.split(",")

    # Sanity Check
    if len(response_splitted) % COLUMN_COUNT != 0:
        print(f"  -> Warning: The LLM response has not {COLUMN_COUNT} values per sentence; \
                len(response_splitted) % {COLUMN_COUNT} = {len(response_splitted) % COLUMN_COUNT}")
    
    llm_list = []
    sentence_tuple = ("", False, "unknown")
    for i in range(0, len(response_splitted)):
        element = response_splitted[i].strip()
        element = element.strip('"')
        element = element.strip("'")
        if i % COLUMN_COUNT == 0:
            sentence_tuple[0] = element
        elif i % COLUMN_COUNT == 1:
            sentence_tuple[1] = element
        else:
            sentence_tuple[2] = element
            llm_list.append(sentence_tuple)

    print("  -> LLM list extracted as follows:")
    print(llm_list)
    return llm_list


def get_statement_relevance_dicts(ref_and_sentences_df, references_df):
    """
    """
    related_supported_statements = []
    related_refuted_statements = []
    related_unknown_statements = []
    related_not_enough_evidence_statements = []

    unrelated_supported_statements = []
    unrelated_refuted_statements = []
    unrelated_unknown_statements = []
    unrelated_not_enough_evidence_statements = []

    for row_i, row in ref_and_sentences_df.iterrows():
        statement_tuple_list = ref_and_sentences_df.at[row_i, 'sentences']
        reference_index = ref_and_sentences_df.at[row_i, 'index_in_refdf']
        reference_id = references_df.at[reference_index, 'ref_id']

        # statement_tuple_list[i][0] = sentence: str
        # statement_tuple_list[i][1] = thematically related/relevant: bool
        # statement_tuple_list[i][2] = stance: str
        for tuple in statement_tuple_list:
            updated_tuple = tuple + (reference_id,)
            # statement_tuple_list[i][3] = reference_id: str

            # If the paper is thematically related/relevant
            if updated_tuple[1]:
                if updated_tuple[2].strip().lower() == "supports":
                    related_supported_statements.append(updated_tuple)
                elif updated_tuple[2].strip().lower() == "refutes":
                    related_refuted_statements.append(updated_tuple)
                elif updated_tuple[2].strip().lower() == "unknown":
                    related_unknown_statements.append(updated_tuple)
                else:
                    related_not_enough_evidence_statements.append(updated_tuple)
            else:
                if updated_tuple[2].strip().lower() == "supports":
                    unrelated_supported_statements.append(updated_tuple)
                elif updated_tuple[2].strip().lower() == "refutes":
                    unrelated_refuted_statements.append(updated_tuple)
                elif updated_tuple[2].strip().lower() == "unknown":
                    unrelated_unknown_statements.append(updated_tuple)
                else:
                    unrelated_not_enough_evidence_statements.append(updated_tuple)
    
    related_statements = {
        'supported': related_supported_statements,
        'refuted': related_refuted_statements,
        'unknown': related_unknown_statements,
        'not_enough_info': related_not_enough_evidence_statements
    }
    unrelated_statements = {
        'supported': unrelated_supported_statements,
        'refuted': unrelated_refuted_statements,
        'unknown': unrelated_unknown_statements,
        'not_enough_info': unrelated_not_enough_evidence_statements
    }

    return related_statements, unrelated_statements




###############################################################################
# Main code
###############################################################################

def compare_intext_references_to_bib(doc, ref_starting_page: int, \
                                     references_df: pd.DataFrame, ref_style: str):
    """
    compare_intext_references_to_bib iterates through the given doc's text and
      searches every reference (set in the text) in the bibliography 
      (as extracted in the references_df).
    Returns:
      - a list of tuples, where each tuple has two elements:
         1) a str = a sentence containing references
         2) a list of Integers containing the indexes (for the reference_df)
            of the references in the sentence
      - a list of Strings containing all sentences that have a reference but
        the reference could not be found in the reference_df
    """
    
    print("##########################################################")
    print("# Starting Reference-Bibliography-Comparision")
    print("##########################################################")

    if ref_style == NUMERIC_REF_STYLE:
        opening_bracket = numeric_referencing["opening_bracket"]
        closing_bracket = numeric_referencing["closing_bracket"]
        separator = numeric_referencing["separator"]
    elif ref_style == AUTHORYEAR_REF_STYLE:
        opening_bracket = authoryear_referencing["opening_bracket"]
        closing_bracket = authoryear_referencing["closing_bracket"]
        separator = authoryear_referencing["separator"]
    else:
        print(f"-> ERROR: Referencing style '{ref_style}' not supported.")
        print("   Skipping text reference checking...")
        return []
    
    sum_of_sentences_checked = 0

    # Cool progress bar to look at while all results are being checked
    estimated_sentence_count = ref_starting_page * EDUCATED_GUESS_ON_SENTENCES_PER_PAGE
    with Progress() as p:
        task = p.add_task(f"-> Processing set references on set in the doc's text...", total=estimated_sentence_count)

        # List that will contain two-item-tuples
        # sentences_and_ref_df_indexes[x][0] = sentence
        # sentences_and_ref_df_indexes[x][1] = list of indexes of references 
        #   in the references_df, where these refs are said in the sentence
        sentences_and_ref_df_indexes = []
        sentences_with_unfound_refs = []

        # NOTE: doc[page_number] is 0-based
        #       we want to iterate till doc[ref_starting_page-1] (inclusive)
        for page_index in range(0, ref_starting_page):
            page_text = doc[page_index].get_text()
            page_text = page_text.replace("-\n", "")
            page_text = page_text.replace("\n", " ")

            # If this is the first page, skip to the abstract
            if page_index == 0:
                # Find the starting index of the reference section
                if page_text.find("Abstract") != -1:
                    ref_starting_index = page_text.find("Abstract")
                elif page_text.find("Introduction") != -1:
                    ref_starting_index = page_text.find("Introduction")
                else:
                    print(f"-> ERROR: No abstract or introduction found on the first page!!")
                    ref_starting_index = len(page_text)

                page_text = page_text[ref_starting_index:]

            # If this is the last text page (where the reference section starts)
            # only take the text before the section start into account
            elif page_index == ref_starting_page-1:
                # Find the starting index of the reference section
                if page_text.find("References") != -1:
                    ref_starting_index = page_text.find("References")
                else:
                    ref_starting_index = page_text.find("Literature")

                page_text = page_text[0:ref_starting_index]

            # Clean page_text from unnecessary points so the parsing works better
            page_text = page_text.replace("et al.", "et al")
            # Note: Ignoring ! and ? as they are uncommon in academia
            sentences = page_text.split(".")
            sum_of_sentences_checked += len(sentences)

            for sentence in sentences:
                sentence_part = sentence
                while len(sentence_part) > 0:

                    # NOTE: Citet references like "Lastname et al. <Ref>" are currently
                    #       not taken into account
                    # Check if both an opening and a closing ref bracket are in the
                    # sentence
                    ob_found_at = sentence_part.find(opening_bracket)
                    cb_found_at = sentence_part.find(closing_bracket)
                    if ob_found_at != -1 and cb_found_at != -1:

                        # If the opening bracket is behind the closing bracket, the split(".")
                        #   probably cought something like "[...] Some citation [...]"
                        # -> We'll ignore it
                        if ob_found_at > cb_found_at:
                            # Look at the part after the found closing bracket
                            sentence_part = sentence_part[cb_found_at+1:]
                            continue
                        
                        # Look for a match of the bracket's content in the references_df
                        bracket_content = sentence_part[ob_found_at+1:cb_found_at]
                        bracket_content = bracket_content.lstrip(opening_bracket).rstrip(closing_bracket)
                        bracket_content = bracket_content.split(separator)

                        # If this is a random bracket and not a set reference this check 
                        #   will lead to false psoitives!
                        # To reduce that risk, check for empty elements and bracket_content
                        #   that doesn't contain any digits (references always do)
                        valid_bracket_content = False
                        if len(bracket_content) == 0:
                            print("-> Info: There is no bracket content?? Skipping this sentence:")
                            print(f"   -> {sentence}")
                        else:
                            for possible_ref in bracket_content:
                                if not possible_ref:
                                    print(f"-> Info: The bracket content {bracket_content} is empty?? Skipping this one.")
                                else:
                                    for char in bracket_content[0]:
                                        if char.isdigit():
                                            valid_bracket_content = True
                                            break

                            if valid_bracket_content:
                                refs_in_sentence = []
                                for ref_index, ref_row in references_df.iterrows():
                                    
                                    if any(item.lower() == ref_row['ref_id'].lower() for item in bracket_content):
                                        refs_in_sentence.append(ref_index)

                                        # No need to check the remaining references of the DF
                                        #   when all are already matched
                                        if len(refs_in_sentence) == len(bracket_content):
                                            break

                                # If at least one match was found add the sentence and the 
                                #   ref_indexes (corresponding to the references_df) to the
                                #   sentences_and_ref_df_indexes list
                                #   (-> ELSE)
                                # Otherwise add the sentence with the reference, that could
                                #   not be matched to the sentences_with_unfound_refs list 
                                #   (-> IF)
                                if len(refs_in_sentence) == 0:
                                    print(f"-> Warning: Bracket content {bracket_content} on p. {page_index+1} could not be matched to a reference.")
                                    print(f"   -> Sentence: {sentence}")
                                    sentences_with_unfound_refs.append(sentence)
                                else:
                                    sentence_indexes_tuple = (sentence, refs_in_sentence)
                                    sentences_and_ref_df_indexes.append(sentence_indexes_tuple)
                            
                        # Look at the part after the found reference to catch more
                        sentence_part = sentence_part[cb_found_at+1:]
                    
                    # If no bracket content was found, break the sentence loop
                    else:
                        break

                p.update(task, advance=1)

    print(f"-> Processed {sum_of_sentences_checked} sentences on {page_index+1} pages -> Avg. of {sum_of_sentences_checked / page_index+1} sentences per page")
    return sentences_and_ref_df_indexes, sentences_with_unfound_refs


def validate_sentence_references(references_df, sentences_and_ref_df_indexes):
    """
    TODO
    """
    
    skip_llm_validation = input("=> To skip the LLM Reference Validation, type 'skip': ").strip()
    if skip_llm_validation.lower() == "skip":
        return pd.DataFrame()


    # 1) Restructure the sentences_and_ref_df_indexes so that we have 
    #    one ref pointing to a list of sentences this ref is used in
    list_of_all_references = []
    list_of_allabstracts = references_df['abstract'].tolist()
    list_of_empty_lists = []
    for i in range(0, len(references_df)):
        list_of_all_references.append(i)
        list_of_empty_lists.append([])

    ref_and_sentences_df = pd.DataFrame({
            'index_in_refdf': list_of_all_references,
            'abstract': list_of_allabstracts,
            'sentences': list_of_empty_lists
        })

    for tuple in sentences_and_ref_df_indexes:
        sentence = tuple[0]
        ref_indexes = tuple[1]

        for ref_i in ref_indexes:
            new_sentence_tuple = (sentence, False, "unknown")
            sentence_tuple_list = ref_and_sentences_df.at[ref_i, 'sentences']
            sentence_tuple_list.append(new_sentence_tuple)
            ref_and_sentences_df.at[ref_i, 'sentences'] = sentence_tuple_list


    # 2) Retrive the ref's abstract and formulate the prompt asking the LLM 
    #    to check wheter the ref (based on its abstract) is thematically 
    #    relevant to each of the statements made in the sentence and 
    #    if it can generally infer if the ref supports or refutes the 
    #    statement (or if there are not enough information)
    #    -> LLM response should be something like this (for each sentence!)
    #       "(sentence, True, "supports")"
    # Note: This of course only works when abstracts were retrieved previously
    for row_index, row in ref_and_sentences_df.iterrows():
        abstract = row['abstract']
        if abstract and abstract != "unknown":
            sentences = row['sentences']

            # Skip the check if the reference is not associated with any sentence
            if sentences:
                llm_answer_list = check_with_llm(abstract, sentences)
                ref_and_sentences_df.at[row_index, 'sentences'] = llm_answer_list
            else:
                print(f"-> WARNING: Reference with index {row['index_in_refdf']} ({references_df.at[row['index_in_refdf'], 'ref_id']}) has no associated sentence!")
        else:
            print(f"-> Missing an abstract for reference with index {row['index_in_refdf']} (Ref. ID = {references_df.at[row['index_in_refdf'], 'ref_id']}); Skipping LLM check...")


    # 3) Extend sentences_and_ref_df_indexes to include the results
    #    given by the LLM's response
    #    -> so for each sentence there should be a list that contains tuples
    #       and each tuple should be the ref_id, thematically_relevant, and stance


    # 4) return
    return ref_and_sentences_df

