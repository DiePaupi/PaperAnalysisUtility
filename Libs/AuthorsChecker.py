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
KNOWN_LASTNAME_PREFIXES = {"van", "van der", "von", "vom", "de", "del", "di", "da", "le", "du", "la", "el", "al"}

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

def get_known_lastname_prefixes():
    return KNOWN_LASTNAME_PREFIXES


def normalize_authors_str(authors_str: str):
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
    authors = authors.replace(f" and", ",")

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

    return parts, contains_et_al


def extract_authors_commasep(authors_str: str):
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

    # parts = [L1, F1, L2, F2, ...]
    parts, contains_et_al = normalize_authors_str(authors_str)
    is_firstname_first = given_bib_type["is_firstname_first"]

    if len(parts) % 2 != 0:
        print("-> Warning: Malformed author string:", parts)
    
    # Group into pairs: (Lastname, FirstInitial.)
    # and append as "Lastname F." to the authors list
    authors_list = []
    for i in range(0, len(parts), 2):
        if i + 1 < len(parts):
            if is_firstname_first:
                first_initial = parts[i].strip()[0]
                last = parts[i + 1]
            else:
                last = parts[i]
                first_initial = parts[i + 1].strip()[0]
            authors_list.append(f"{last} {first_initial}.")
        # Company names (e.g., "GPTZero") can be just appended
        else:
            authors_list.append(parts[i].strip())
    
    return authors_list, contains_et_al


def extract_authors_spacesep(authors_str: str):
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

    # authors_list = [F1 L1, F2 L2, ...]
    authors_list, contains_et_al = normalize_authors_str(authors_str)
    is_firstname_first = given_bib_type["is_firstname_first"]
    
    # Split full author name into: "Lastname F."
    normalized_authors = []
    for author in authors_list:
        # parts = [F1, (p1,) (p2,) L1], where p1 and p2 are possible lastname prefixes
        parts = author.split()

        # Normal case: [Firstname, Lastname] or [Lastname, Firstname]
        if len(parts) == 2:
            if is_firstname_first:
                first_initial = parts[0].strip()[0]
                last_name = parts[-1].strip()
            else:
                first_initial = parts[-1].strip()[0]
                last_name = parts[0].strip()
            normalized_authors.append(f"{last_name} {first_initial}.")

        # Could be either a name with a lastname preffix or a second first name
        elif len(parts) == 3:
            # Example: [Jan, vom, Brocke] or [vom, Brocke, Jan]
            if parts[1].strip().lower() in KNOWN_LASTNAME_PREFIXES or parts[0].strip().lower() in KNOWN_LASTNAME_PREFIXES:
                if is_firstname_first:
                    first_initial = parts[0].strip()[0]
                    last_name = f"{parts[1].strip()} {parts[2].strip()}"
                else:
                    first_initial = parts[2].strip()[0]
                    last_name = f"{parts[0].strip()} {parts[1].strip()}"
            # Example: [Anthony, J., Crowley] or [Crowley, Anthony, J.]
            else:
                if is_firstname_first:
                    first_initial = parts[0].strip()[0]
                    last_name = parts[-1].strip()
                else:
                    first_initial = parts[1].strip()[0]
                    last_name = parts[0].strip()
            normalized_authors.append(f"{last_name} {first_initial}.")

        # Could be 1) a name with two lastname preffixes,
        #          2) a name with two first names and a lastname prefix,
        #          3) a name with three firstnames
        elif len(parts) == 4:
            # Example: [Renate, van, der, Molen] or [van, der, Molen, Renate]
            if f"{parts[1].strip()} {parts[2].strip()}".lower() in KNOWN_LASTNAME_PREFIXES \
                or f"{parts[0].strip()} {parts[1].strip()}".lower() in KNOWN_LASTNAME_PREFIXES:
                if is_firstname_first:
                    first_initial = parts[0].strip()[0]
                    last_name = f"{parts[1].strip()} {parts[2].strip()} {parts[3].strip()}"
                else:
                    first_initial = parts[3].strip()[0]
                    last_name = f"{parts[0].strip()} {parts[1].strip()} {parts[2].strip()}"
            # Example: [Christoph, C., von, Egedy] or [von, Egedy, Christoph, C.]
            elif parts[2].strip().lower() in KNOWN_LASTNAME_PREFIXES or parts[0].strip().lower() in KNOWN_LASTNAME_PREFIXES:
                if is_firstname_first:
                    first_initial = parts[0].strip()[0]
                    last_name = f"{parts[2].strip()} {parts[3].strip()}"
                else:
                    first_initial = parts[2].strip()[0]
                    last_name = f"{parts[0].strip()} {parts[1].strip()}"
            # Example: [Thi, T., G., Tran] or [Tran, Thi, T., G.]
            else:
                if is_firstname_first:
                    first_initial = parts[0].strip()[0]
                    last_name = parts[3].strip()
                else:
                    first_initial = parts[1].strip()[0]
                    last_name = parts[0].strip()

            normalized_authors.append(f"{last_name} {first_initial}.")

        # Extreme Example: "Willibrodus Martinus Pankratius 'Wil' van der Aalst" aka. "W. M. P. van der Aalst"
        else:
            print(f"-> Warning: Malformed author string: '{author}'")
            normalized_authors.append(author.strip())
    
    return normalized_authors, contains_et_al



###############################################################################
# Main code
###############################################################################

def get_normalized_authors(authors_str: str) -> list:
    if (not authors_str) or (authors_str == "NOT PARSED"):
        return [], False

    is_comma_separated = given_bib_type["is_comma_sep"]

    if is_comma_separated:
        normalized_authors, contains_et_al = extract_authors_commasep(authors_str)
    else:
        normalized_authors, contains_et_al =  extract_authors_spacesep(authors_str)

    return normalized_authors, contains_et_al


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
        if isinstance(authors_list, list):
            author_counter.update(authors_list)

    # Get authors that are referenced more than MAX_AUTHOR_REFERENCES
    frequent_authors = {
        author: count
        for author, count in author_counter.items()
        if count > MAX_AUTHOR_REFERENCES
    }

    return frequent_authors