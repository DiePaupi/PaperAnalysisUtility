###############################################################################
# Imports
###############################################################################
from collections import Counter
import pandas as pd



###############################################################################
# INFO
###############################################################################

# LFfl (APA Style)
# - Springer Nature (LaTeX) Template for references
    # Lastname, Firstname-FirstLetter.:

    # Examples:
    # Raczyńska, M.:
    # Uren, V., Edwards, J.S.:
    # van der Staay, A., Markic, M., Nebel, M., Poeppelbuss, J., Janiesch, C.:

# FL
# - ACM Template for references:
    # Firstname Lastname.

    # Examples:
    # Boris A Galitsky.
    # Raja Parasuraman and Victor Riley.
    # Greg Brockman, Mira Murati, Peter Welinder, and OpenAI.
    # Steve Cohen et al.



###############################################################################
# Gloal Variables
###############################################################################

# Constants:
MAX_AUTHOR_REFERENCES = 2

given_bib_type = {}



###############################################################################
# Helper functions
###############################################################################

# Note: The given bib style name is given by the user (in PQC.py) and then
#       set in the ReferenceChecker, which matches the name to the style dict
#       and sets the dict here
def set_given_bib_type(bib_type: dict):
    global given_bib_type
    given_bib_type = bib_type

def get_frequent_author_threshold():
    return MAX_AUTHOR_REFERENCES


def normalize_authors_str(authors_str: str) -> list[str]:
    if not authors_str:
        return []
    
    separator = given_bib_type["author_separator"]
    ending = given_bib_type["authors_rest_separator"]
    
    # Handle possible ending char (between the authors and the rest)
    authors = authors_str.strip().rstrip(ending)

    if separator != ",":
        authors = authors.replace(separator, ",")

    # Handle possible "and"
    authors = authors.replace(f", and", ",")
    authors = authors.replace(f" and ", ",")

    # Handle possible "et al"
    contains_et_al = False
    if ", et al." in authors:
        contains_et_al = True
        authors = authors.replace(f", et al.", "")
    if ", et al" in authors:
        contains_et_al = True
        authors = authors.replace(f", et al", "")
    if " et al." in authors:
        contains_et_al = True
        authors = authors.replace(f" et al.", "")
    if " et al" in authors:
        contains_et_al = True
        authors = authors.replace(f" et al", "")
    
    # Split authors by separator
    parts = [p.strip() for p in authors.split(",")]

    if contains_et_al:
        parts.append("et al")

    return parts


def extract_authors_commasep(authors_str: str) -> list[str]:
    """
    extract_authors_commasep takes a string of authors in the following format:

    A) E.g., as used by Springer Nature (is_firstname_first = False):
        1 Author:     <Lastname>, <Firstname>
        >= 2 Authors: <Lastname1>, <Firstname>, <Lastname2>, <Firstname2>

    B) E.g., as used by AAAI/ACM (is_firstname_first = True):
        1 Author:     <Lastname>, <Firstname-FirstLetter>.
        2 Authors:    <Lastname1>, <Firstname-FirstLetter1>.; and <Lastname2>, <Firstname-FirstLetter2>.
        >= 3 Authors: <Lastname1>, <Firstname-FirstLetter1>.; <Lastname2>, <Firstname-FirstLetter2>.; and <Lastname3>, <Firstname-FirstLetter3>.
     
    NOTE: Assuption is that a name (last and first) is always separated by ,
    
    It extracts a list of author names in the format "Lastname F."
    (only the first letters of the first names are kept).
    """

    parts = normalize_authors_str(authors_str)
    is_firstname_first = given_bib_type["is_firstname_first"]

    if len(parts) % 2 != 0:
        print("-> Warning: Malformed author string:", parts)
    
    # Group into pairs: (Lastname, FirstInitial.)
    # and append as "Lastname F." to the authors list
    authors_list = []
    for i in range(0, len(parts), 2):
        if i + 1 < len(parts):
            if is_firstname_first:
                first_initial = parts[i]
                last = parts[i + 1]
            else:
                last = parts[i]
                first_initial = parts[i + 1]
            authors_list.append(f"{last} {first_initial}")
    
    return authors_list


def extract_authors_spacesep(authors_str: str) -> list[str]:
    """
    extract_authors_spacesep takes a string of authors in the following format:

    E.g., as used by ACM (is_firstname_first = True):
        1 Author:     <Firstname> <Lastname>
        2 Authors:    <Firstname1> <Lastname2> and <Firstname2> <Lastname2>
        >= 3 Authors: <Firstname1> <Lastname2>, <Firstname2> <Lastname2>,  and <Firstname3> <Lastname3>
    
    NOTE: Assuption is that a name (last and first) is always separated by a space

    It extracts a list of author names in the format "Lastname F."
    (only the first letters of the first names are kept).
    """

    authors_list = normalize_authors_str(authors_str)
    is_firstname_first = given_bib_type["is_firstname_first"]
    
    # Split full author name into: "Lastname F."
    normalized_authors = []
    for author in authors_list:
        parts = author.split()
        if len(parts) >= 2:
            if is_firstname_first:
                first_initial = parts[0][0]
                last_name = parts[-1]
            else:
                first_initial = parts[-1][0]
                last_name = parts[0]
            normalized_authors.append(f"{last_name} {first_initial}.")
        else:
            print(f"-> Warning: Malformed author string: '{author}'")
            normalized_authors.append(author.strip())
    
    return normalized_authors



###############################################################################
# Main code
###############################################################################

def get_normalized_authors(authors_str: str) -> list:
    if authors_str == "NOT PARSED":
        return []

    is_comma_separated = given_bib_type["is_comma_sep"]

    if is_comma_separated:
        return extract_authors_commasep(authors_str)
    else:
        return extract_authors_spacesep(authors_str)


def get_frequent_authors(references_df: pd.DataFrame):
    """
    The AuthorsChecker module takes a dataframe containing the references
    as input and counts how often each author appears in the references.
    It then identifies authors that are referenced more than a specified 
    threshold (MAX_AUTHOR_REFERENCES).
    
    RETURN: a dictionary of these authors along with their reference counts.
    """

    print("###############################")
    print("# Starting Author Check")
    print("###############################")

    author_counter = Counter()

    # Extract authors from each reference and count their occurrences
    for authors_list in references_df["normalized_authors"]:
        author_counter.update(authors_list)

    # Get authors that are referenced more than MAX_AUTHOR_REFERENCES
    frequent_authors = {
        author: count
        for author, count in author_counter.items()
        if count > MAX_AUTHOR_REFERENCES
    }

    return frequent_authors