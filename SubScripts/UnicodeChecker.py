###############################################################################
# Imports
###############################################################################
from collections import Counter
from email.mime import text



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
# - -   U+002D  hyphen-minus
# - –   U+2013  en dash
# - —   U+2014  em dash
# - −   U+2212  minus sign

# Non-breaking Space
# -     U+00A0  non-breaking space



###############################################################################
# Gloal Variables
###############################################################################

unicode_aphostrophes = ['\u0027', '\u2018', '\u2019', '\u201B', '\u2032']
unicode_quotes = ['\u0022', '\u201C', '\u201D', '\u201E', '\u201F']
unicode_dashes = ['\u002D', '\u2013', '\u2014', '\u2212']
unicode_spaces = ['\u00A0']
unicode_characters = set().union(
    unicode_aphostrophes
    + unicode_quotes
    + unicode_dashes
    + unicode_spaces
)



###############################################################################
# Helper functions
###############################################################################

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
    # Check if its correctly used between a word and a reference
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
    if any(char in text for char in unicode_spaces):
        unicode_lines[3].append((text, page_no))

    return unicode_lines


def check_if_unicode_is_sus(unicode_lines: list):
    """
    """

    global unicode_aphostrophes
    global unicode_quotes
    global unicode_dashes
    global unicode_spaces

    print("###############################")
    print("# Starting Unicode Check")
    print("###############################")

    # NOTE: This needs to have the same format as the one used in PQC.py
    invalid_unicode_lines = [[], [], [], []]
    

    # TODO: Check lines with Unicode apostrophes
    # TODO: Check lines with Unicode quotes
    # TODO: Check lines with Unicode dashes

    #==========================================================================
    # Check validity of Unicode non-breaking spaces
    #==========================================================================
    valid_space_uses = 0
    invalid_space_uses = 0
    for line_pageno_tupel in unicode_lines[3]:
        line, page_no = line_pageno_tupel

        # Always find the fist occurence of the non-breaking space, check it,
        # and then remove it from the line and check for the next one
        line_contains_min_one_invalid_use = False
        while True:
            space_index = rest_line.find(unicode_spaces[0])
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
            invalid_unicode_lines[3].append((line, page_no))
    

    #==========================================================================
    # Create a dict of stats and return
    #==========================================================================
    stats = {
        "valid_nonbreaking_spaces": valid_space_uses,
        "invalid_nonbreaking_spaces": invalid_space_uses
    }
    
    return invalid_unicode_lines, stats
