###############################################################################
# Imports
###############################################################################
from collections import Counter
import copy



###############################################################################
# INFO
###############################################################################

# Unicode Apostrophes / Single Quotes
# - '   U+0027  ASCII apostrophe
# - ‘   U+2018  left single quotation mark
# - ’   U+2019  right single quotation mark
# - ‛   U+201B  single high-reversed-9
# - ′   U+2032  prime

# Quotation Marks
# - "   U+0022  ASCII quote
# - “   U+201C  left double quotation
# - ”   U+201D  right double quotation
# - „   U+201E  low double quotation (German)
# - ‟   U+201F  double high-reversed-9

# Dashes
# See https://jakubmarian.com/hyphen-minus-en-dash-and-em-dash-difference-and-usage-in-english/
# - -   U+002D  hyphen-minus
# - ‐   U+2010  HYPHEN
# - ‑   U+2011  NON-BREAKING HYPHEN
# - –   U+2013  en dash
# - —   U+2014  em dash
# - −   U+2212  minus sign

# Non-breaking Space
# -     U+0020  normal space
# -     U+00A0  non-breaking space
# -     U+2009  thin space
# Other spaces u2002=en space, u2003=em space, u2004=three-per-em space, 
# u2005=four-per-em space, u2006=six-per-em space, u2007=figure space, 
# u2008=punctuation space, u200A=hair space, u205f=MMSP, u3000=ideographic space


###############################################################################
# Gloal Variables
###############################################################################

unicode_aphostrophes = ['\u0027', '\u2018', '\u2019', '\u201B', '\u2032']
unicode_quotes = ['\u0022', '\u201C', '\u201D', '\u201E', '\u201F']
unicode_dashes = ['\u002D', '\u2010', '\u2011', '\u2013', '\u2014', '\u2212']
dash_map = {
    "\u002D": "HYPHEN-MINUS",
    "\u2010": "HYPHEN",
    "\u2011": "NON-BREAKING HYPHEN",
    "\u2013": "EN DASH",
    "\u2014": "EM DASH",
    "\u2212": "MINUS SIGN",
}
unicode_spaces = ['\u0020', '\u00A0']
space_map = {
    "\u0020": "NORMAL SPACE",
    "\u00A0": "NON-BREAKING SPACE",
    "\u2009": "THIN SPACE"
}

unicode_characters = set().union(
    unicode_aphostrophes
    + unicode_quotes
    + unicode_dashes
    + unicode_spaces
)



###############################################################################
# Helper functions
###############################################################################

def replace_all_unicode(input: str) -> str:
    input_str = copy.deepcopy(input)

    for a in unicode_aphostrophes:
        input_str = input_str.replace(a, "'")
    for q in unicode_quotes:
        input_str = input_str.replace(q, '"')
    for d in unicode_dashes:
        input_str = input_str.replace(d, '-')
    for s in unicode_spaces:
        input_str = input_str.replace(s, ' ')

    return input_str


def replace_accent_marks(input: str) -> str:
    input_str = copy.deepcopy(input)

    # ¨a / ¨o / ¨u
    if "¨" in input_str:
        input_str = input_str.replace("¨a", 'ä')
        input_str = input_str.replace("¨A", 'Ä')
        input_str = input_str.replace("¨o", 'ö')
        input_str = input_str.replace("¨O", 'Ö')
        input_str = input_str.replace("¨u", 'ü')
        input_str = input_str.replace("¨U", 'Ü')
    # ˜n
    if "˜" in input_str:
        input_str = input_str.replace("˜n", 'ñ')
        input_str = input_str.replace("˜N", 'Ñ')
    # ´a / ´ı / ´o
    if "´" in input_str:
        input_str = input_str.replace("´a", 'á')
        input_str = input_str.replace("´A", 'Á')
        input_str = input_str.replace("´i", 'í')
        input_str = input_str.replace("´ı", 'í')
        input_str = input_str.replace("´I", 'Í')
        input_str = input_str.replace("´o", 'ó')
        input_str = input_str.replace("´O", 'Ó')
    # ò ?
    # TODO
    # °
    if "°" in input_str:
        input_str = input_str.replace("°a", 'å')
        input_str = input_str.replace("°A", 'Å')

    return input_str




def check_hyphen_minus_validity(text: str, hyphen_minus_index: int, page_no: int):
    # TODO!
    return True


def check_hyphen_validity(text: str, hyphen_index: int, page_no: int):
    # TODO!
    return True


def check_en_dash_validity(text: str, en_dash_index: int, page_no: int):
    # TODO!
    return True


def check_em_dash_validity(text: str, em_dash_index: int, page_no: int):
    # TODO!
    return True


def check_minus_sign_validity(text: str, minus_sign_index: int, page_no: int):
    """
    As the name suggests, the minus sign is only used to mean the difference of 
    two mathematical objects, usually numbers, e.g. a − b, or as the unary minus 
    sign, e.g. −5. In practice, most computer users type the hyphen-minus in 
    place of the minus sign, compare −5 (minus sign) and -5 (hyphen-minus). 
    If the minus sign is not available, I recommend to use the en-dash instead, 
    compare “6 – 5” (en-dash) and “6 - 5” (hyphen-minus, too short).

    Note: Most programming languages require the user to use the hyphen-minus 
          sign in place of a minus.
    """

    # TODO
    # Check if the minus sign is used between two digits, e.g. '5−6' or '5 - 6'
    if minus_sign_index-1>=0 and minus_sign_index+1<len(text):
        # Case: 5−6; valid
        if text[minus_sign_index-1].isdigit() and text[minus_sign_index+1].isdigit():
            return True
        elif minus_sign_index-2>=0 and minus_sign_index+2<len(text):
            # Case: 5 − 6; valid
            if text[minus_sign_index-2].isdigit() and text[minus_sign_index+2].isdigit():
                if text[minus_sign_index-1] in unicode_spaces and text[minus_sign_index+1] in unicode_spaces:
                    return True
    return False


def check_nonbreaking_space_validity(text: str, space_index: int, page_no: int):
    """
    check_nonbreaking_space_validity takes a string, the index of a non-breaking space 
    in that string, and the page number of the line the string originates from.
    It checks if the non-breaking space is used correctly, which is, if:
    - It is used between "p." and a page number (e.g. "p. 23")
    - It is used between a word and a reference (e.g. "Smith (2020)")

    RETURN: True if the non-breaking space is used correctly, False otherwise.
    """

    # Check if its correctly used etween "p." and a number
    if space_index-2>=0 and text[space_index-2:space_index] == "p.":
        if space_index+1<len(text) and text[space_index+1].isdigit():
            print(f" -> INFO: Found a correctly used non-breaking space to connect 'p.' and the page number")
            print(f"      --> page {page_no}, line: {text}")
            return True
        else:
            print(f" -> WARNING: Found a non-breaking space between 'p.' and a non-digit in the line: {text} (page {page_no})")
            return False
    # Check if its correctly used between a word and a reference / bracket in general
    elif space_index+1<len(text):
        if text[space_index+1] == "(" or text[space_index+1] == "[":
            print(f" -> INFO: Found a correctly used non-breaking space to connect a word and a reference")
            print(f"      --> page {page_no}, line: {text}")
            return True
        else:
            print(f" -> WARNING: Found a non-breaking space that seems invalid.")
            return False
    else:
        print(f" -> WARNING: Found a non-breaking space at the end of a line??")
        return False




###############################################################################
# Main code
###############################################################################

def count_occurences(text: str):
    """
    count_occurences takes a string of text and checks for the presence of 
    Unicode characters that are commonly used in academic writing.
    
    RETURN: A counter object with the count of each Unicode character found in the text.
    """

    # Count occurrences of each Unicode character in the text
    found_characters = Counter(char for char in text if char in unicode_characters)

    return found_characters


def get_unicode_line_lists(text: str, page_no: int):
    """
    get_unicode_line_lists takes a page line (text) and its page number and checks 
    for the presence of specific Unicode characters as definied in the global lists.
    -> unicode_aphostrophes, unicode_quotes, unicode_dashes, unicode_spaces

    If any of these characters are found in the text, the line along with its page 
    number is added to the respective list in 'unicode_lines'.

    RETURN: A list of four lists, where each inner list contains tuples of 
       (line: str, page_no: int) of their respective occurences:
       [0] lines with Unicode apostrophes, 
       [1] lines with Unicode quotes,
       [2] lines with Unicode dashes,
       [3] lines with Unicode non-breakingspaces
    """

    global unicode_aphostrophes
    global unicode_quotes
    global unicode_dashes
    global unicode_spaces

    # NOTE: This needs to have the same format as the one used in PQC.py
    unicode_lines = [[], [], [], []]

    if any(char in text for char in unicode_aphostrophes):
        unicode_lines[0].append((text, page_no))
    if any(char in text for char in unicode_quotes):
        unicode_lines[1].append((text, page_no))
    if any(char in text for char in unicode_dashes):
        unicode_lines[2].append((text, page_no))
    # The first entry of unicode_spaces is the normal space, which we want to ignore here
    if any(char in text for char in unicode_spaces[1:]):
        unicode_lines[3].append((text, page_no))

    return unicode_lines


def check_if_unicode_is_sus(unicode_lines: list):
    """
    """

    global unicode_aphostrophes
    global unicode_quotes
    global unicode_dashes
    global dash_map
    global unicode_spaces

    print("##########################################################")
    print("# Starting Unicode Check")
    print("##########################################################")

    # NOTE: This needs to have the same format as the one used in PQC.py
    invalid_unicode_lines = [[], [], [], []]
    

    # TODO: Check lines with Unicode apostrophes
    # TODO: Check lines with Unicode quotes


    #==========================================================================
    # Check validity of Unicode dashes spaces
    #==========================================================================
    valid_hyphen_uses = 0
    invalid_hyphen_uses = 0
    valid_nonbreaking_hyphen_uses = 0
    invalid_nonbreaking_hyphen_uses = 0
    valid_hyphen_minus_uses = 0
    invalid_hyphen_minus_uses = 0
    valid_en_dash_uses = 0
    invalid_en_dash_uses = 0
    valid_em_dash_uses = 0
    invalid_em_dash_uses = 0
    valid_minus_sign_uses = 0
    invalid_minus_sign_uses = 0

    valid_space_uses = 0
    invalid_space_uses = 0
    
    skip_validation = input("=> To skip the unicode check, type 'skip': ").strip()
    if skip_validation.lower() == "skip":
        stats = {
            "valid_hyphen_uses": valid_hyphen_uses,
            "invalid_hyphen_uses": invalid_hyphen_uses,
            "valid_nonbreaking_hyphen_uses": valid_nonbreaking_hyphen_uses,
            "invalid_nonbreaking_hyphen_uses": invalid_nonbreaking_hyphen_uses,
            "valid_hyphen_minus_uses": valid_hyphen_minus_uses,
            "invalid_hyphen_minus_uses": invalid_hyphen_minus_uses,
            "valid_en_dash_uses": valid_en_dash_uses,
            "invalid_en_dash_uses": invalid_en_dash_uses,
            "valid_em_dash_uses": valid_em_dash_uses,
            "invalid_em_dash_uses": invalid_em_dash_uses,
            "valid_minus_sign_uses": valid_minus_sign_uses,
            "invalid_minus_sign_uses": invalid_minus_sign_uses,
            "valid_nonbreaking_spaces": valid_space_uses,
            "invalid_nonbreaking_spaces": invalid_space_uses
        }
        return invalid_unicode_lines, stats
    
    for line_pageno_tupel in unicode_lines[2]:
        line, page_no = line_pageno_tupel

        # Always find the fist occurence of the dash, check it,
        # and then remove it from the line and check for the next one
        line_contains_min_one_invalid_use = False
        rest_line = copy.deepcopy(line)
        while True:

            # Check if any of the dashes are in the line and sort them ascending by their 
            # index in the line, so we can check the first one
            found_dash = {}
            for index, char in enumerate(rest_line):
                if char in dash_map:
                    found_dash = {
                        "name": dash_map[char],
                        "char": char,
                        "index": index
                    }
            # If a dash-char was found, check its validity and remove it from the line, 
            # otherwise break the loop
            if found_dash:
                match found_dash["name"]:
                    case "HYPHEN-MINUS":
                        if check_hyphen_minus_validity(rest_line, found_dash['index'], page_no):
                            valid_hyphen_minus_uses += 1
                        else:
                            line_contains_min_one_invalid_use = True
                            invalid_hyphen_minus_uses += 1
                    case "HYPHEN":
                        if check_hyphen_validity(rest_line, found_dash['index'], page_no):
                            valid_hyphen_uses += 1
                        else:
                            line_contains_min_one_invalid_use = True
                            invalid_hyphen_uses += 1
                    case "NON-BREAKING HYPHEN":
                        if check_hyphen_validity(rest_line, found_dash['index'], page_no):
                            valid_nonbreaking_hyphen_uses += 1
                        else:
                            line_contains_min_one_invalid_use = True
                            invalid_nonbreaking_hyphen_uses += 1
                    case "EN DASH":
                        if check_en_dash_validity(rest_line, found_dash['index'], page_no):
                            valid_en_dash_uses += 1
                        else:
                            line_contains_min_one_invalid_use = True
                            invalid_en_dash_uses += 1
                    case "EM DASH":
                        if check_em_dash_validity(rest_line, found_dash['index'], page_no):
                            valid_em_dash_uses += 1
                        else:
                            line_contains_min_one_invalid_use = True
                            invalid_em_dash_uses += 1
                    case "MINUS SIGN":
                        if check_minus_sign_validity(rest_line, found_dash['index'], page_no):
                            valid_minus_sign_uses += 1
                        else:
                            line_contains_min_one_invalid_use = True
                            invalid_minus_sign_uses += 1

                    case _:
                        print(f"Something's wrong with the dash matching in rest-line {rest_line} on p. {page_no}!")
                    
                rest_line = rest_line[found_dash['index']+1:]
            else:
                break
        
        # A line needs only to be added once
        if line_contains_min_one_invalid_use:
            invalid_unicode_lines[2].append((line, page_no))
            print(f"-> Invalid unicode use found on p. {page_no}: {line}")


    #==========================================================================
    # Check validity of Unicode non-breaking spaces
    #==========================================================================
    #valid_space_uses = 0
    #invalid_space_uses = 0
    for line_pageno_tupel in unicode_lines[3]:
        line, page_no = line_pageno_tupel

        # Always find the fist occurence of the non-breaking space, check it,
        # and then remove it from the line and check for the next one
        line_contains_min_one_invalid_use = False
        rest_line = copy.deepcopy(line)
        while True:
            space_index = rest_line.find(unicode_spaces[1])
            if space_index != -1:
                if check_nonbreaking_space_validity(rest_line, space_index, page_no):
                    valid_space_uses += 1
                else:
                    line_contains_min_one_invalid_use = True
                    invalid_space_uses += 1
                rest_line = rest_line[space_index+1:]
            else:
                break
        
        # A line needs only to be added once
        if line_contains_min_one_invalid_use:
            # TODO: Maybe replace the invisible non-breaking space with a °
            invalid_unicode_lines[3].append((line, page_no))
    

    #==========================================================================
    # Create a dict of stats and return
    #==========================================================================
    stats = {
        "valid_hyphen_uses": valid_hyphen_uses,
        "invalid_hyphen_uses": invalid_hyphen_uses,
        "valid_nonbreaking_hyphen_uses": valid_nonbreaking_hyphen_uses,
        "invalid_nonbreaking_hyphen_uses": invalid_nonbreaking_hyphen_uses,
        "valid_hyphen_minus_uses": valid_hyphen_minus_uses,
        "invalid_hyphen_minus_uses": invalid_hyphen_minus_uses,
        "valid_en_dash_uses": valid_en_dash_uses,
        "invalid_en_dash_uses": invalid_en_dash_uses,
        "valid_em_dash_uses": valid_em_dash_uses,
        "invalid_em_dash_uses": invalid_em_dash_uses,
        "valid_minus_sign_uses": valid_minus_sign_uses,
        "invalid_minus_sign_uses": invalid_minus_sign_uses,
        "valid_nonbreaking_spaces": valid_space_uses,
        "invalid_nonbreaking_spaces": invalid_space_uses
    }
    
    return invalid_unicode_lines, stats
