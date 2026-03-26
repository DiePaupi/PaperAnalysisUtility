###############################################################################
# Imports
###############################################################################
import os
import plotly.graph_objects as go
import pymupdf
import re
import sys

import SubScripts.ReferenceChecker as rc
import SubScripts.AuthorsChecker as ac



###############################################################################
# INFO
###############################################################################

# NOTE: To save the results as .md file you'll need to habe the 'tabulate' 
#       package installed

# TODOs:
# - Paper Quality:
#    + Check the uniformity of used chars like apostrophes, quotes, and dashes
#    + Check if references match the statement they are supposed to support
#        (e.g., by checking the abstract on Scholar)
#    + Sind alle Referenzen im Text auch im Literaturverzeichnis hinterlegt??
#        + Ist die Referenzierung sinnvoll (zB nur a und b hinter einem Jahr, 
#          wenn auch zwei Paper vom Auhtor aus dem, selben jahr zitiert werden)?
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

# Template to use for references
# NOTE: Currently only "springer" is supported
template = "springer"

# Paper template - formatting specifications
springer_template = {
    # Always skip first two lines in the springer template as they are: 
    #   page_lines[0] = Shortitle/Author; page_lines[1] = page number
    "header_lines": 2, 
}




###############################################################################
# Helper functions
###############################################################################

def check_document_structure(doc, template_name):
    global headings
    global references_starting_page_no

    if template_name == "springer":
        global springer_template
        lineskip = springer_template["header_lines"]
    else:
        print(f"ERROR: Template '{template_name}' not supported yet!")
        print(" -> The programm will exit now. :)")
        sys.exit(0)

    # NOTE: doc[page_number] is 0-based
    for page_no in range(0, doc.page_count):
        page_text = doc[page_no].get_text()

        # Replace "-\n" with nothing to remove obvious mid-sentence line breaks
        page_text = page_text.replace("-\n", "")

        # Iterate over all page lines to check headings and find the refrences
        page_lines = page_text.split("\n")

        # NOTE: Lineskip for headers is template-specific
        for line_index in range(lineskip, len(page_lines)):
            line = page_lines[line_index].strip()

            # Springer headings are parsed as a single number in one line
            #   and the heading in the next
            heading_match = re.match(r'^(?:[1-9]|[1-9]\d)$', line)
            if heading_match:
                number = heading_match.group(0)

                # Check if the current line is not the last
                if line_index + 1 < len(page_lines):
                    if len(headings) > 0:
                        last_index = len(headings) - 1
                        last_heading_no = int(headings[last_index][0].strip())
                        if int(number.strip())-1 == last_heading_no:
                            text = page_lines[line_index + 1].strip()
                            print(f"Found following heading '{number} - {text}' on page {page_no + 1}")
                            headings.append((number, text, page_no + 1))
                    else:
                        text = page_lines[line_index + 1].strip()
                        print(f"Found first heading '{number} - {text}' on page {page_no + 1}")
                        headings.append((number, text, page_no + 1))
                
            # Check for "References" or "Literature" (case-insensitive)
            elif line.lower() in ["references", "literature"]:
                print(f"Found references/literature section on page {page_no + 1}")
                headings.append(('R', line, page_no + 1))
                references_starting_page_no = page_no + 1
                return

        page_no += 1



###############################################################################
# Main code
###############################################################################

def main():
    """
    x
    """
    global headings
    global references_starting_page_no


    #==========================================================================
    # Read input PDF
    #==========================================================================
    path_to_pdf = input("Enter the path to the PDF file: ").strip().strip('"')
    doc = pymupdf.open(path_to_pdf, filetype="txt")

    # TODO: Make multiple templates possible
    check_document_structure(doc, template)


    #==========================================================================
    # Check paper quality:
    #==========================================================================
    # TODO: Check the uniformity of used chars like apostrophes, quotes, and dashes


    #==========================================================================
    # Extract and check references
    #==========================================================================
    # NOTE: Check out rc.main() doc. for details on the dict's ('stats') keys
    stats = {}
    # NOTE: 'entries' is a list of three lists: 
    #       [invalid_link_entries, mismatching_entries, unfound_entries]
    entries = [[], [], []]

    if references_starting_page_no <= 0:
        print("ERROR: No references section found in the document.")
        print(" -> The programm will exit now. :)")
        sys.exit(0)
    else:
        global references_df
        references_df, stats, entries = rc.main(doc, references_starting_page_no)
    
    extracted_references = references_df.drop('full_reference', axis=1)

    TOTAL_NO_OF_REFERENCES = stats["total_no_of_references"]
    no_link_provided_counter = stats["no_link_provided"]
    invalid_link_counter = stats["invalid_links"]
    skipped_searches_counter = stats["skipped_searches"]
    mismatching_infos_counter = stats["mismatching_infos"]
    no_entry_found_counter = stats["no_entry_found"]

    invalid_entries = entries[0]
    mismatching_entries = entries[1]
    unfound_entries = entries[2]


    #==========================================================================
    # Check how often an author appears in the references
    #==========================================================================
    # TODO: Ask user if author references should be counted?

    # NOTE: This dict is unsorted
    frequent_authors = ac.main(references_df, template)



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
            f.write(f"- No link provided: {no_link_provided_counter}/{TOTAL_NO_OF_REFERENCES}={no_link_provided_counter/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            f.write(f"- Invalid link: {invalid_link_counter}/{TOTAL_NO_OF_REFERENCES}={invalid_link_counter/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            if invalid_entries:
                f.write("  - Invalid entries:\n")
                for entry in invalid_entries:
                    f.write(f"    - {entry}\n")
            f.write(f"- Skipped searches: {skipped_searches_counter}/{TOTAL_NO_OF_REFERENCES}={skipped_searches_counter/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            f.write(f"- Mismatching infos: {mismatching_infos_counter}/{TOTAL_NO_OF_REFERENCES}={mismatching_infos_counter/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            if mismatching_entries:
                f.write("  - Mismatching entries:\n")
                for entry in mismatching_entries:
                    f.write(f"    - {entry}\n")
            f.write(f"- No entry found: {no_entry_found_counter}/{TOTAL_NO_OF_REFERENCES}={no_entry_found_counter/TOTAL_NO_OF_REFERENCES*100:.2f}%\n")
            if unfound_entries:
                f.write("  - Unfound entries:\n")
                for entry in unfound_entries:
                    f.write(f"    - {entry}\n")
        
        # Print frequently referenced authors sorted by value (count) descending
        f.write("\n## Frequently Referenced Authors\n\n")
        for author, count in sorted(
            frequent_authors.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            f.write(f"- {author}: {count}\n")

        # Print the references DF using df.to_markdown(tablefmt="grid")
        f.write("\n## Extracted References\n\n")
        f.write(extracted_references.to_markdown())
    
    print("---")
    print("FINISHED!")
    print(f" -> Results saved to {results_path}")


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