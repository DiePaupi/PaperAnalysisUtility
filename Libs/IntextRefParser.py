###############################################################################
# Imports
###############################################################################
import copy
import pandas as pd
import re

import Libs.UnicodeChecker as uc



###############################################################################
# INFO
###############################################################################

# Numeric References
    # SINGLE
        # "Barredo Arrieta et al. [2]"
        # "[17]"
    # MULTIPLE
    #   "[11, 18, 29]"

# Authoryear References
    # SINGLE
        # "Piorkowski et al. (2021)"
        # "Pilanci and Ergen (2020)"
        # `Lelarge & Miolane (2019)`
        # "(Kaur et al. 2020)"
        # `(Wu et al., 2023)`
        # "[Arora et al., 2019a]"
    # MULTIPLE
        # "(Wischnewski et al. 2024; Scharowski et al. 2023)"
        # "(Candes and Tao (2005); Chartrand (2007); Chartrand and Staneva (2008))"
        # "Candès and Recht (2009); Candès and Tao (2010); Davenport and Romberg (2016)"
        # "(Parhi and Nowak (2021, 2022); Shenouda et al. (2024))"
        # `(Bartlett et al., 2006; Belkin et al., 2018; Montanari et al., 2019)`
        # "[Chowdhury and Gopalan (2019)]"
        # "[Lugosi and Mendelson (2019a); Catoni (2012)]"



###############################################################################
# Gloal Variables
###############################################################################

# NOTE: The numeric reference style is defined by being a number within square
#       brackets, e.g., "[1]" or "[245]"
#    -> Multiple numbers are separated by a comma, e.g., "[3,14,82]"
NUMERIC_REF_STYLE = "numeric"

# NOTE: The author-year reference style ...
AUTHOR_YEAR_REF_STYLE = "authoryear"


ref_style = ""
sentences_with_unfound_refs = []
sentences_and_ref_df_indexes = []



###############################################################################
# Helper functions
###############################################################################

def set_ref_style(given_ref_style: str):
    global ref_style
    ref_style = given_ref_style


def check_ref_against_references_df(bracket_split: list, bracket_content: str,
                                    sentence: str, page_no: int, 
                                    references_df: pd.DataFrame):
    """
    - bracket_split   = list of possible ref_ids
    - bracket_content = full bracket all possible (sub) ref_ids were found in
    - sentence        = sentence that contains the bracket
    """
    global sentences_with_unfound_refs
    global sentences_and_ref_df_indexes
    
    # If we're looking at a random bracket and not a set reference this check will
    # lead to false psoitives!
    # To reduce that risk, check for empty elements and those who don't contain any
    # digits (references always do)
    valid_element = False
    if len(bracket_split) == 0:
        print("-> Info: There is no bracket content??" \
                + " Skipping this sentence:")
        print(f"   -> {sentence}")
    else:
        for possible_ref in bracket_split:
            if not possible_ref:
                print("-> Info: The bracket content " \
                        + f"{bracket_split} is empty?? " \
                        + "Skipping this one.")
            elif isinstance(possible_ref, int):
                valid_element = True
                break
            else:
                if any(char.isdigit() for char in possible_ref):
                    valid_element = True
                    break
    
    # If at least one element in bracket_split seems valid: 
    # Check against the references_df
    if valid_element:
        refs_in_sentence = []
        for ref_index, ref_row in references_df.iterrows():
            
            # Check if the current ref_id (of the row we're looking at)
            # matches one of the bracket_split-items
            if any(str(item).lower().strip() == ref_row['ref_id'].lower().strip() for item in bracket_split):
                refs_in_sentence.append(ref_index)

                # No need to check the remaining references of the DF
                # when all are already matched
                if len(refs_in_sentence) == len(bracket_split):
                    break
        
        if len(refs_in_sentence) == 0:
            # If no reference was matched: add the sentence with the 
            # reference that could not be matched to the 
            # sentences_with_unfound_refs list
            if bracket_content:
                print(f"-> Warning: Bracket content '{bracket_content}' on" \
                        + f" p. {page_no+1} could not be matched to a reference.")
                print(f"   -> Sentence: {sentence}")
                sentences_with_unfound_refs.append(sentence)
        else:
            # If at least one match was found: add the sentence and the 
            # ref_indexes (corresponding to the references_df) to the
            # sentences_and_ref_df_indexes list
            sentence_indexes_tuple = (sentence, refs_in_sentence)
            sentences_and_ref_df_indexes.append(sentence_indexes_tuple)


# -------


def check_full_sentence_for_numeric_ref(sentence: str, references_df: pd.DataFrame,
                                   page_no: int):
    """
    This function takes a (full) sentence as string and checks it iteratively \
    for numeric references.
    Multiple separate references are parsed into one list which is then given \
    to check_ref_against_references_df(...), where they are compared against \
    the references_df.
    
    As a result, unfound references will be added to the global 
    sentences_with_unfound_refs list and matches will be stored in the global
    sentences_and_ref_df_indexes list.
    """
    
    sentence_part = copy.deepcopy(sentence)
    while len(sentence_part) > 0:

        # Check if both an opening and a closing ref bracket are in the sentence
        opening_found_at = sentence_part.find('[')
        closing_found_at = sentence_part.find(']')

        if opening_found_at != -1 and closing_found_at != -1:
            # If the opening bracket is behind the closing bracket, the split(".")
            #   probably cought something like "[...] Some citation [...]"
            # -> Skip to the part after the found closing bracket
            if opening_found_at > closing_found_at:
                sentence_part = sentence_part[closing_found_at+1:]
                continue
            else:
                # Get what's inside the bracket
                bracket_content = sentence_part[opening_found_at+1:closing_found_at]
                bracket_content = bracket_content.lstrip('[').rstrip(']')

                # Split content by reference separatot to get single references in a
                # list
                bracket_split = bracket_content.split(',')

                # Loop over each element and, if its a range, get each number within
                # this range
                replaced_bracket_split = []
                for element in bracket_split:
                    if "-" in uc.replace_all_unicode(element):
                        # ref_range should be a two-item-list where:
                        # [0] = lower ref no, and [1] = upper ref no
                        ref_range = uc.replace_all_unicode(element).split("-")
                        if len(ref_range) == 2:
                            try:
                                first_ref_no = int(ref_range[0].strip())
                                second_ref_no = int(ref_range[1].strip())
                                ref_range_list = list(range(first_ref_no, 
                                                            second_ref_no+1))
                                replaced_bracket_split += ref_range_list
                            except:
                                print("-> Warning: Numeric reference range " \
                                      + "couldn't be parsed as Integers: " \
                                      + f"{bracket_split}")
                                replaced_bracket_split.append(element)
                        else:
                            print("-> Warning: Numeric reference range was " \
                                  + f"split into != 2 parts: {bracket_split}")
                            replaced_bracket_split.append(element)
                    else:
                        # If the element is not a range, just use the element itself
                        replaced_bracket_split.append(element)
                
                # Update the bracket split after range replacement
                bracket_split = replaced_bracket_split

                # Check the references against the references_df
                check_ref_against_references_df(bracket_split, bracket_content, 
                                                sentence, page_no, references_df)
                
                # Look at the part after the found reference to catch more
                sentence_part = sentence_part[closing_found_at+1:]

        else:
            # If not both an opening and a closing square bracket are found in
            # the sentence, break the loop and return
            break


# -------


def get_outer_bracket_content(input_str: str):
    """
    This function checks a given string for a the outermost matching brackets \
    (square or round) and returns the opening and closing brackets index as \
    well as the opening and closing bracket chars.
    If no match was found or the given string empty, -1 for both indices and \
    an empty string for the bracket chars is returned.
    """

    if not input_str:
        return -1, -1, '', ''
    
    opening_square_bracket_index = -1
    opening_round_bracket_index = -1
    closing_bracket_index = -1

    # If there are nested brackets, we want to find a match for the brackets on
    # the same depth level
    square_depth_counter = 0
    round_depth_counter = 0

    # Check each char in the input_str to find the outer bracket match
    for i in range(0, len(input_str)):

        if input_str[i] == '[':
            square_depth_counter += 1
            # If this is the first opening bracket, save the index
            if opening_square_bracket_index == -1 \
                and opening_round_bracket_index == -1:
                opening_square_bracket_index = i
        elif input_str[i] == '(':
            round_depth_counter += 1
            # If this is the first opening bracket, save the index
            if opening_square_bracket_index == -1 \
                and opening_round_bracket_index == -1:
                opening_round_bracket_index = i

        elif input_str[i] == ']':
            square_depth_counter -= 1
            if closing_bracket_index == -1 and square_depth_counter == 0:
                closing_bracket_index = i
                break
        elif input_str[i] == ')':
            round_depth_counter -= 1
            if closing_bracket_index == -1 and round_depth_counter == 0:
                closing_bracket_index = i
                break
    
    # If an outer bracket match for square brackets was found
    if opening_square_bracket_index != -1 and closing_bracket_index != -1:
        return opening_square_bracket_index, closing_bracket_index, '[', ']'
    # If an outer bracket match for round brackets was found
    elif opening_round_bracket_index != -1 and closing_bracket_index != -1:
        return opening_round_bracket_index, closing_bracket_index, '(', ')'
    # If no bracket match was found, return default
    else:
        return -1, -1, '', '' 


def check_for_citet_ref(sentence_part_before_bracket: str, bracket_content: str):
    """
    This function is called when a single year (with or without suffixing letter) \
    was found as bracket content to check for a in text (citet) reference
    -> e.g., 'Su and Yang [2019]'
    """

    if len(sentence_part_before_bracket) < 2:
        return ""
    
    # Split the sentence (part) into single words
    words = sentence_part_before_bracket.split()

    # Iterate backwords through the chars of the sentence (part), starting at
    # the opening bracket
    # Example split: [..., 'as', 'shown', 'by', 'Su', 'and', 'Yang']
    word_index = len(words)-1
    possible_ref_id_parts = []
    while word_index >= 0:
        if words[word_index][0].isupper() \
            or words[word_index] == "and" or words[word_index] == "&" \
            or words[word_index] == "al" or words[word_index] == "et":
            possible_ref_id_parts.append(words[word_index])
            word_index -= 1
        else:
            break

    if len(possible_ref_id_parts) > 1:
        # Reverse possible_ref_id_parts into string
        possible_ref_id = ""
        word_index = len(possible_ref_id_parts)-1
        while word_index >= 0:
            possible_ref_id += possible_ref_id_parts[word_index] + " "
            word_index -= 1
        
        possible_ref_id = possible_ref_id.strip()
        possible_ref_id += " " + bracket_content
        possible_ref_id = possible_ref_id.replace("&", "and")
        possible_ref_id = possible_ref_id.lstrip("and ")
        return possible_ref_id
    elif len(possible_ref_id_parts) == 1:
        possible_ref_id = possible_ref_id_parts[0].strip() + " " + bracket_content
        return possible_ref_id
    else:
        return ""
    

def check_sentence_part_for_author_year_ref(sentence_part: str, references_df: pd.DataFrame,
                                            page_no: int, this_is_the_second_call: bool):
    """
    """
    # Examples for author-year-references (where the curved bracket can either
    # be a round or square bracket):
    # -> Chen et al. {2020}
    #       -> or nested as    {Chen et al. {2020}}
    #       -> or for multiple {Candes and Tao {2005}; Chartrand {2007}}
    # -> {Arora et al., 2019a}
    #       -> or for multiple with comma     {Wang & Thrampoulidis, 2022; Deng et al., 2022}
    #       -> or for multiple with semicolon {Wang & Thrampoulidis, 2022, Deng et al., 2022}

    # NOTE: If the year is not in separat brackets, the separator between
    #       author names and year is either a comma (',') or nothing ('')
    # NOTE: Multiple references are either separated by a comma (',') or 
    #       a semicolon (';')

    opening_index, closing_index, opening_bracket, closing_bracket = get_outer_bracket_content(sentence_part)
    if opening_index != -1 and closing_index != -1:
        bracket_content = sentence_part[opening_index+1:closing_index]

        # Check if the content is a year (4 digits or 4 digits + one letter)
        if (len(bracket_content) == 4 and bracket_content.isdigit()) \
            or (len(bracket_content) == 5 and bracket_content[0:5].isdigit() \
                and (not bracket_content[5].isdigit())):
            sentence_part_before_bracket = sentence_part[0:opening_index].strip()
            possible_ref_id = check_for_citet_ref(sentence_part_before_bracket, bracket_content)
            if possible_ref_id:
                return [possible_ref_id], closing_index, bracket_content
            else:
                return [], closing_index, bracket_content

        # If there is more content inside the brackets and this is the first go
        # -> This is a cutoff for nested brackets
        elif not this_is_the_second_call:

            # If there is a semicolon in it, this is probably a separator for
            # MULTIPLE references
            #  -> Case A: {Candes and Tao {2005}; Chartrand {2007}}
            #  -> Case B: {Wang & Thrampoulidis, 2022; Deng et al., 2022}
            if ';' in bracket_content:
                bracket_split = bracket_content.split(';')

                possible_ref_id_list = []
                for possible_ref_id in bracket_split:

                    # Case A:
                    if ('[' in possible_ref_id and ']' in possible_ref_id) \
                        or ('(' in possible_ref_id and ')' in possible_ref_id):
                        sub_ref_ids, ci, bc = check_sentence_part_for_author_year_ref(possible_ref_id, references_df, page_no, True)
                        possible_ref_id_list += sub_ref_ids
                    
                    # Case B:
                    else:
                        sub_bracket_split = possible_ref_id.split(',')
                        if len(sub_bracket_split) == 2:
                            sub_ref_id = sub_bracket_split[0].strip() + " " \
                                + sub_bracket_split[1].strip()
                            possible_ref_id_list += [sub_ref_id]
                        else:
                            # If there is no comma but still a year in the bracket 
                            # content, add as one thing
                            year_match = re.search(r'(?:^|[\s,.;:(])((?:18|19|20)\d{2})\b', bracket_content)
                            if year_match:
                                possible_ref_id_list += [sub_bracket_split]
                            else:
                                year_match = re.findall(r'\s(\d{4}).', bracket_content)
                                if year_match:
                                    possible_ref_id_list += [sub_bracket_split]
                                else:
                                    print("-> Couldn't parse in-text (sub) reference " \
                                        + f"'({possible_ref_id})' in bracket " \
                                        + f"'{bracket_content}' on p. {page_no}!")
                                    continue

                # Return the found possible_ref_id_list
                return possible_ref_id_list, closing_index, bracket_content

            # If there is a comma in it, this can either just be a seperator
            # between author and year or also between references
            #  -> Case A: {Arora et al., 2019a}
            #  -> Case B: {Wang & Thrampoulidis, 2022, Deng et al., 2022}
            elif ',' in bracket_content:
                bracket_split = bracket_content.split(',')

                # Case A
                if len(bracket_split) == 2:
                    possible_ref_id = bracket_split[0].strip() + " " \
                        + bracket_split[1].strip()
                    return [possible_ref_id], closing_index, bracket_content
                
                # Case B
                else:
                    # If there are pairwise elements in the bracket_split:
                    # Put two of them together and add them as sub_ref_id to the
                    # possible_ref_id_list
                    if len(bracket_split) % 2 == 0:
                        possible_ref_id_list = []
                        current_sub_ref_id = ""
                        for sub_ref_id_part_index in range(0, len(bracket_split)):
                            if sub_ref_id_part_index % 2 == 0:
                                current_sub_ref_id = bracket_split[sub_ref_id_part_index].strip()
                            else:
                                # TODO: Do a sanity check and see if this is a year?
                                current_sub_ref_id += " " + bracket_split[sub_ref_id_part_index].strip()
                                possible_ref_id_list.append(current_sub_ref_id)
                        return possible_ref_id_list, closing_index, bracket_content
                    else:
                        # TODO: Add parsing for doube year references, e.g., "(Hollmann et al, 2022, 2025)"
                        # -> bracket_split = ['Hollmann et al', ' 2022', ' 2025']
                        #   -> and for 'Zhang et al (2023, 2024)'
                        print("-> Couldn't parse in-text references " \
                                  + f"'({bracket_split})' in bracket " \
                                  + f"on p. {page_no}!")
                        return [], closing_index, bracket_content
            
            # If there are neither ; nor , in the bracket:
            # Check if there is a year in the brackets content and if that's 
            # the case, return as one ref_id
            # TODO: No I need to normalize this here??
            else:
                year_match = re.search(r'(?:^|[\s,.;:(])((?:18|19|20)\d{2})\b', bracket_content)
                if year_match:
                    # If there is a citet ref in a sentence in brackets, the whole sentence is given here
                    #  -> "(viewable as iterative pseudo-labeling Fan et al (2023))"
                    #  -> bracket_content = "viewable as iterative pseudo-labeling Fan et al (2023)"
                    if ('[' in bracket_content and ']' in bracket_content) \
                        or ('(' in bracket_content and ')' in bracket_content):
                        sub_ref_ids, ci, bc = check_sentence_part_for_author_year_ref(bracket_content, references_df, page_no, True)
                        return sub_ref_ids, closing_index, bracket_content
                    else:
                        bracket_content = bracket_content.replace('(', '').replace('[', '')
                        return [bracket_content], closing_index, bracket_content
                else:
                    year_match = re.findall(r'\s(\d{4}).', bracket_content)
                    if year_match:
                        return [bracket_content], closing_index, bracket_content
                    else:
                        #print("-> Couldn't parse bracket " \
                        #          + f"'({bracket_content})' to reference " \
                        #          + f"on p. {page_no}")
                        return [], closing_index, bracket_content

        
        # If this is already the second call
        else:
            return [], -1, bracket_content
    
    # If no bracket was found
    else:
        round_opening_index = sentence_part.find('(')
        square_opening_index = sentence_part.find('[')
        if round_opening_index != -1 and square_opening_index != -1:
            first_opening_index = min(round_opening_index, square_opening_index)
            return [], first_opening_index, ""
        elif round_opening_index != -1:
            return [], round_opening_index, ""
        elif square_opening_index != -1:
            return [], square_opening_index, ""
        else:
            return [], 0, ""


def check_full_sentence_for_author_year_ref(sentence: str, references_df: pd.DataFrame,
                                            page_no: int):
    """
    """

    sentence_part = copy.deepcopy(sentence)
    possible_ref_ids_list = []
    while len(sentence_part) > 0:
        if ('[' in sentence_part and ']' in sentence_part) \
            or ('(' in sentence_part and ')' in sentence_part):
            # check_sentence_part_for_author_year_ref() returns [possible_ref_id], closing_index
            possible_ref_ids, closing_index, bracket_content = check_sentence_part_for_author_year_ref(sentence_part, references_df, page_no, False)

            # Add found ref_ids to the list for the full sentence
            for possible_ref_id in possible_ref_ids:
                # An author-year reference should be at least 6 chars long (e.g., "Wu 2025")
                if len(possible_ref_id) >= 6 \
                    and (possible_ref_id[-4:].isdigit() or possible_ref_id[-5:-1].isdigit()):
                    possible_ref_ids_list.append( possible_ref_id)
                else:
                    print(f"-> Skipping possible_ref_id '{possible_ref_id}' since " \
                          + "it's shorter than 6 chars and/or the last four chars " \
                          + "are not all digits (missing year).")

            # Look at the part after the found reference to catch more
            sentence_part = sentence_part[closing_index+1:]

        else:
            # If not both an opening and a closing square bracket are found in
            # the sentence, break the loop and return
            break

    # Check the references against the references_df
    if possible_ref_ids_list:
        check_ref_against_references_df(possible_ref_ids_list, bracket_content, sentence,
                                        page_no, references_df)
    




###############################################################################
# Main code
###############################################################################

def check_sentence_for_ref(sentence: str, page_no: int, 
                           references_df: pd.DataFrame):
    """
    This function is called to check for references in a single (full) sentence.
    Depending on the referencing style, it calls the respective method and \
    returns:
    [0] = sentences_with_unfound_refs,
    [1] = sentences_and_ref_df_indexes
    """

    # Reset the lists
    global sentences_with_unfound_refs
    global sentences_and_ref_df_indexes
    sentences_with_unfound_refs = []
    sentences_and_ref_df_indexes = []

    if sentence:
        if ref_style == NUMERIC_REF_STYLE:
            check_full_sentence_for_numeric_ref(sentence, references_df, page_no)
            return sentences_with_unfound_refs, sentences_and_ref_df_indexes
        elif ref_style.startswith(AUTHOR_YEAR_REF_STYLE):
            check_full_sentence_for_author_year_ref(sentence, references_df, page_no)
            return sentences_with_unfound_refs, sentences_and_ref_df_indexes
        else:
            print(f"-> ERROR: Referencing style '{ref_style}' not supported.")
            print("   Skipping text reference checking...")
            return sentences_with_unfound_refs, sentences_and_ref_df_indexes
    
    else:
        return sentences_with_unfound_refs, sentences_and_ref_df_indexes
    