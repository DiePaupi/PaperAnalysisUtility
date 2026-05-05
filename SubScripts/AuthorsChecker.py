###############################################################################
# Imports
###############################################################################
from collections import Counter
import pandas as pd



###############################################################################
# INFO
###############################################################################

# APA Style
# - Springer Nature (LaTeX) Template for references
    # Lastname, Firstname-FirstLetter.:

    # Examples:
    # Raczyńska, M.:
    # Uren, V., Edwards, J.S.:
    # van der Staay, A., Markic, M., Nebel, M., Poeppelbuss, J., Janiesch, C.:

# ACM Template for references:
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

given_bib_type = ""



###############################################################################
# Helper functions
###############################################################################

def set_given_bib_type(bib_type):
    global given_bib_type
    given_bib_type = bib_type


def extract_authors_springer(authors_str: str):
    """
    extract_authors_springer takes a string of authors in the format used by 
    Springer Nature:
        1 Author:     <Lastname>, <Firstname-FirstLetter>.
        >= 2 Authors: <Lastname1>, <Firstname-FirstLetter1>., <Lastname2>, <Firstname-FirstLetter2>.
    
    It extracts a list of author names in the format "Lastname F."
    (only the first letters of the first names are kept).
    """

    if not authors_str:
        return []
    
    # In some cases removing trailing colons might be necessary
    authors = authors_str.strip().rstrip(":")
    
    # Split authors by comma
    parts = [p.strip() for p in authors.split(",")]

    if len(parts) % 2 != 0:
        print("-> Warning: Malformed author string:", authors)
    
    # Group into pairs: (Lastname, FirstInitial.)
    # and append as "Lastname F." to the authors list
    authors_list = []
    for i in range(0, len(parts), 2):
        if i + 1 < len(parts):
            last = parts[i]
            first_initials = parts[i + 1]
            authors_list.append(f"{last} {first_initials}")
    
    return authors_list


def extract_authors_aaai_acm(authors_str: str):
    """
    extract_authors_acm takes a string of authors in the format used by 
    AAAI/ACM:
        1 Author:     <Lastname>, <Firstname-FirstLetter>.
        2 Authors:    <Lastname1>, <Firstname-FirstLetter1>.; and <Lastname2>, <Firstname-FirstLetter2>.
        >= 3 Authors: <Lastname1>, <Firstname-FirstLetter1>.; <Lastname2>, <Firstname-FirstLetter2>.; and <Lastname3>, <Firstname-FirstLetter3>.
     
    It extracts a list of author names in the format "Lastname F."
    (only the first letters of the first names are kept).
    """

    if not authors_str:
        return []
    
    authors = authors_str.strip().rstrip(".")
    
    handle_multiple_authors = False

    # Cases of "et al" being in authors
    if "et al" in authors and not ";" in authors:
        first_author = authors.split("et al")[0].strip()
        authors_list = [first_author]
    elif "et al" in authors and ";" in authors:
        # Example: "Chatila, R.; Dignum, V.; Fisher, M.; Giannotti, F.; Morik, K.; et al."
        handle_multiple_authors = True

        # Handle "et al"
        et_al_split = authors.split("; et al")
        if len(et_al_split) == 1:
            authors = authors.split("; and et al")[0].strip()
        else:
            authors = et_al_split[0].strip()
    
    # Cases of "et al" not being in authors
    elif "et al" not in authors and not ";" in authors:
        # Example: "Dignum, V."
        authors_list = [authors]
    else:
        # Example: "Duran, P.; Castano, J.; Gómez, C.; and Martínez-Fernández, S."
        handle_multiple_authors = True

        # Normalize separators
        authors = authors.replace("; and ", "; ")
        authors = authors.replace(" and ", "; ")
    
    if handle_multiple_authors:
        authors_list = [a.strip() for a in authors.split(";")]
    
    normalized_authors = []
    
    # Split full authorname into: "Lastname F."
    for author in authors_list:
        parts = author.split(",")
        if len(parts) >= 2:
            last_name = parts[0].strip()
            first_initial = parts[1].strip()
            first_initial = first_initial[0]
            normalized_authors.append(f"{last_name} {first_initial}.")
        else:
            print(f"-> Warning: Author '{author}' has no firstname?")
            normalized_authors.append(author.strip())
    
    return normalized_authors


def extract_authors_acm(authors_str: str):
    """
    extract_authors_acm takes a string of authors in the format used by 
    ACM:
        1 Author:     <Firstname> <Lastname>
        2 Authors:    <Firstname1> <Lastname2> and <Firstname2> <Lastname2>
        >= 3 Authors: <Firstname1> <Lastname2>, <Firstname2> <Lastname2>,  and <Firstname3> <Lastname3>
     
    It extracts a list of author names in the format "Lastname F."
    (only the first letters of the first names are kept).
    """

    if not authors_str:
        return []
    
    authors = authors_str.strip().rstrip(".")
    
    # Handle "et al."
    if "et al" in authors:
        first_author = authors.split("et al")[0].strip()
        # TODO: Handle a possible , before "et al"
        authors_list = [first_author]
    else:
        # Example: "Ma Thi Chau."
        # Example: "Andrea Stevenson Won and Shuo Zhou."
        # Example: "Thomas Schubert, Frank Friedmann, and Holger Regenbrecht."

        # Normalize separators
        authors = authors.replace(", and ", ", ")
        authors = authors.replace(" and ", ", ")
        authors_list = [a.strip() for a in authors.split(",")]
    
    normalized_authors = []
    
    # Split full authorname into: "Lastname F."
    for author in authors_list:
        parts = author.split()
        if len(parts) >= 2:
            first_initial = parts[0][0]
            last_name = parts[-1]
            normalized_authors.append(f"{last_name} {first_initial}.")
        else:
            print(f"-> Warning: Author '{author}' has no firstname?")
            normalized_authors.append(author.strip())
    
    return normalized_authors



###############################################################################
# Main code
###############################################################################

def get_normalized_authors(authors_str: str) -> list:
    if given_bib_type == "springer":
        return extract_authors_springer(authors_str)
    elif given_bib_type == "aaai_acm":
        return extract_authors_aaai_acm(authors_str)
    elif given_bib_type == "acm":
        return extract_authors_acm(authors_str)
    else:
        print(f"Warning: Unknown template '{given_bib_type}' for author extraction.")
        return []


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
    for authors_str in references_df["authors"]:
        if given_bib_type == "springer":
            author_counter.update(extract_authors_springer(authors_str))
        elif given_bib_type == "aaai_acm":
            author_counter.update(extract_authors_aaai_acm(authors_str))
        elif given_bib_type == "acm":
            author_counter.update(extract_authors_acm(authors_str))
        else:
            print(f"Warning: Unknown template '{given_bib_type}' for author extraction.")
            return {}

    # Get authors that are referenced more than MAX_AUTHOR_REFERENCES
    frequent_authors = {
        author: count
        for author, count in author_counter.items()
        if count > MAX_AUTHOR_REFERENCES
    }

    return frequent_authors