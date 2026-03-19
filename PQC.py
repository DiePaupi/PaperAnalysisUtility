###############################################################################
# Imports
###############################################################################
import os
import plotly.graph_objects as go
import pymupdf
import re

import SubScripts.ReferenceChecker as rc



###############################################################################
# INFO
###############################################################################

# TODOs:
# - Paper Quality:
#    + Check the uniformity of used chars like apostrophes, quotes, and dashes
#    + Check if references match the statement they are supposed to support
#        (e.g., by checking the abstract on Scholar)
# - Literature:
#    + Check if an author is refereced with multiple papers (>=5?)



###############################################################################
# Gloal Variables
###############################################################################

# 'headings' contains thruples of (number, text, page_no) for each heading 
#    found in the document; the number is 'R' for the references section
headings = []
# 'references_starting_page_no' is the page number where the references section
#    starts; it is 0 if no references section was found
references_starting_page_no = 0

# Counters delivered by the ReferenceChecker
no_link_provided_counter = 0
invalid_link_counter = 0
skipped_searches_counter = 0
mismatching_infos_counter = 0
no_entry_found_counter = 0
invalid_entries = []




###############################################################################
# Helper functions
###############################################################################

def check_document_structure(doc):
    global headings
    global references_starting_page_no

    # NOTE: doc[page_number] is 0-based
    for page_no in range(0, doc.page_count):
        page_text = doc[page_no].get_text()

        # Replace "-\n" with nothing to remove obvious mid-sentence line breaks
        page_text = page_text.replace("-\n", "")

        # Iterate over all page lines to check headings and find the refrences
        page_lines = page_text.split("\n")
        for line in page_lines:
            line = line.strip()
    
            # Check for heading pattern with capturing groups: (number) and (text)
            heading_match = re.match(r'^(\d)\s+([a-zA-Z0-9\s]+)$', line)
            if heading_match:
                number = heading_match.group(1)
                text = heading_match.group(2).strip()
                print(f"Found heading '{number} - {text}' on page {page_no + 1}")
                headings.append((number, text, page_no + 1))
            
            # Check for "References" or "Literature" (case-insensitive)
            elif line.lower() in ["references", "literature"]:
                print(f"Found references/literature section on page {page_no + 1}")
                headings.append(('R', line, page_no + 1))
                references_starting_page_no = page_no + 1
                break

        page_no += 1



###############################################################################
# Main code
###############################################################################

def main():
    """
    x
    """
    
    global no_link_provided_counter
    global invalid_link_counter
    global skipped_searches_counter
    global mismatching_infos_counter
    global no_entry_found_counter
    global invalid_entries


    #==========================================================================
    # Read input PDF
    #==========================================================================
    path_to_pdf = input("Enter the path to the PDF file: ").strip().strip('"')
    doc = pymupdf.open(path_to_pdf, filetype="txt")

    check_document_structure(doc)


    #==========================================================================
    # Check paper quality:
    #==========================================================================
    # TODO: Check the uniformity of used chars like apostrophes, quotes, and dashes


    #==========================================================================
    # Extract and check references
    #==========================================================================
    if references_starting_page_no <= 0:
        print("ERROR: No references section found in the document.")
    else:
        global references_df
        references_df, total_no_of_references, no_link_provided_counter, invalid_link_counter, skipped_searches_counter, mismatching_infos_counter, no_entry_found_counter, invalid_entries = rc.main(doc, references_starting_page_no)


    #==========================================================================
    # Check how often an author appears in the references
    #==========================================================================
    # TODO: Ask user if author references should be counted
    # TODO: Count how often an auhtor appears in the references


    #==========================================================================
    # Log results into a markdown file
    #==========================================================================
    # NOTE: Results will be saved in the same folder as the input PDF
    #       with the name "PQC_results.md"
    results_folder_dir = os.path.dirname(path_to_pdf)
    results_path = os.path.join(results_folder_dir, "PQC_results.md")

    with open(results_path, "x", encoding="utf-8") as f:
        f.write("# Paper Quality Check Results\n\n")
        f.write("## Document Structure\n\n")
        if not headings:
            f.write("No headings found in the document.\n\n")
        else:
            for number, text, page_no in headings:
                f.write(f"{number}) '{text}' -- p. {page_no}\n")
        
        f.write("\n## Reference Checker Results\n\n")
        if references_starting_page_no <= 0:
            f.write("No references section found in the document.\n")
        else:
            f.write(f"References section starts on page {references_starting_page_no}.\n\n")
            f.write(f"- No link provided: {no_link_provided_counter}/{total_no_of_references}={no_link_provided_counter/total_no_of_references*100:.2f}%\n")
            f.write(f"- Invalid link: {invalid_link_counter}/{total_no_of_references}={invalid_link_counter/total_no_of_references*100:.2f}%\n")
            f.write(f"- Skipped searches: {skipped_searches_counter}/{total_no_of_references}={skipped_searches_counter/total_no_of_references*100:.2f}%\n")
            f.write(f"- Mismatching infos: {mismatching_infos_counter}/{total_no_of_references}={mismatching_infos_counter/total_no_of_references*100:.2f}%\n")
            f.write(f"- No entry found: {no_entry_found_counter}/{total_no_of_references}={no_entry_found_counter/total_no_of_references*100:.2f}%\n")
            if invalid_entries:
                f.write("- Invalid entries:\n")
                for entry in invalid_entries:
                    f.write(f"  - {entry}\n")


    #==========================================================================
    # Create Pie Chart, 'cause Pie Charts are cool
    #==========================================================================
    labels = ['No link provided','Invalid link','Skipped searches',
              'Mismatching infos', 'NO ENTRY FOUND']
    values = [no_link_provided_counter, invalid_link_counter, skipped_searches_counter, 
              mismatching_infos_counter, no_entry_found_counter]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.show()



###############################################################################
# Run Main
###############################################################################
if __name__ == "__main__":
    main()