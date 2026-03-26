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



###############################################################################
# Helper functions
###############################################################################

def extract_authors_springer(authors_str: str):
    """
    extract_authors_springer takes a string of authors in the format used by 
    Springer Nature and extracts a list of author names in the format 
    "Lastname F." (only the first letters of the first names are kept).
    """

    if not authors_str:
        return []
    
    # NOTE: In some cases removing training colons or similar might be necessary
    
    # Split auhtors_str by comma
    parts = [p.strip() for p in authors_str.split(",")]

    if len(parts) % 2 != 0:
        print("Warning: malformed author string:", authors_str)
    
    # Group into pairs: (Lastname, FirstInitial.)
    # and append as "Lastname F." to the authors list
    authors = []
    for i in range(0, len(parts), 2):
        if i + 1 < len(parts):
            last = parts[i]
            first_initials = parts[i + 1]
            authors.append(f"{last} {first_initials}")
    
    return authors


def extract_authors_acm(authors_str: str):
    """
    extract_authors_acm takes a string of authors in the format used by 
    ACM and extracts a list of author names in the format 
    "Lastname F." (only the first letters of the first names are kept).
    """

    if not authors_str:
        return []
    
    # TODO: Check if that is necessary
    authors_str = authors_str.strip().rstrip(".")
    
    # Handle "et al."
    if "et al" in authors_str:
        first_author = authors_str.split("et al")[0].strip()
        authors = [first_author]
    else:
        # Normalize separators
        authors_str = authors_str.replace(", and ", ", ")
        authors_str = authors_str.replace(" and ", ", ")
        authors = [a.strip() for a in authors_str.split(",")]
    
    normalized_authors = []
    
    # Split full auhtorname into: "Lastname F."
    for author in authors:
        parts = author.split()
        if len(parts) >= 2:
            first_initial = parts[0][0]
            last_name = parts[-1]
            normalized_authors.append(f"{last_name} {first_initial}.")
    
    return normalized_authors



###############################################################################
# Main code
###############################################################################

def main(references_df: pd.DataFrame, template: str):
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
        if template == "springer":
            author_counter.update(extract_authors_springer(authors_str))
        elif template == "acm":
            author_counter.update(extract_authors_acm(authors_str))
        else:
            print(f"Warning: Unknown template '{template}' for author extraction.")
            return {}

    # Get authors that are referenced more than MAX_AUTHOR_REFERENCES
    frequent_authors = {
        author: count
        for author, count in author_counter.items()
        if count > MAX_AUTHOR_REFERENCES
    }

    return frequent_authors