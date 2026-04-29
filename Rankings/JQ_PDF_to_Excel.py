"""
FÜR DIE JOURNAL TABELLEN:
---

line_index 0-6 = heading; kann weg
line_index 7-12 = table header
line_index 13-18 = erster Eintrag; Zeile 1
line_index 19-24 = zweiter Eintrag; Zeile 2
line_index 25-30 = dritter Eintrag; Zeile 3
...
=> Jede neue Tabellenzeile startet ab 13+6*n

Seite 2 (page_no = 1): Nach dem letzten "Link" Eintrag der Tabelle:
284 -> 1. Zeile p1 der linkesten Tabellenspalte ("Wirtschaftsinformatik or")
285 -> 1. Zeile p2 der linkesten Tabellenspalte ("Information Systems Journal")
286 -> 2. Zeile p1 der linkesten Tabellenspalte ("Journals with or at the interface to")
287 -> 2. Zeile p2 der linkesten Tabellenspalte ("Wirtschaftsinformatik or")
288 -> 2. Zeile p3 der linkesten Tabellenspalte ("Information Systems")

Seite 3 (page_no = 2): Nach dem letzten "Link" Eintrag der Tabelle:
284 -> 2. Zeile p1 der linkesten Tabellenspalte ("Business and Management")
285 -> 2. Zeile p2 der linkesten Tabellenspalte ("Journals (without explicit interface")
286 -> 2. Zeile p3 der linkesten Tabellenspalte ("to WInf/IS)")
287 -> 1. Zeile p1 der linkesten Tabellenspalte ("Journals with or at the interface to")
288 -> 1. Zeile p2 der linkesten Tabellenspalte ("Wirtschaftsinformatik or")
289 -> 1. Zeile p3 der linkesten Tabellenspalte ("Information Systems")

Seite 4 (page_no = 3): Nach dem letzten "Link" Eintrag der Tabelle:
236 -> "A+ outstanding and world-leading journals"
237 -> "A  leading journals"
238 -> "B  important and respected journals"
239 -> "C  recognized journals"
240 -> "D  other academic journals"
241 -> 1. Zeile p1 der linkesten Tabellenspalte ("Business and Management")
242 -> 1. Zeile p2 der linkesten Tabellenspalte ("Journals (without explicit interface")
243 -> 1. Zeile p3 der linkesten Tabellenspalte ("to WInf/IS)")
244 -> 4. Zeile p1 der linkesten Tabellenspalte ("Discipline-independent Journals")
245 -> 4. Zeile p2 der linkesten Tabellenspalte ("(without explicit interface to")
246 -> 4. Zeile p3 der linkesten Tabellenspalte ("WInf/IS, transdisciplinary,")
247 -> 4. Zeile p4 der linkesten Tabellenspalte ("interdisciplinary)")
248 -> Überschrift "Categories" für die Rankings (siehe Zeile 236-240)
249 -> 3. Zeile p1 der linkesten Tabellenspalte ("Discipline-specific Journals (without")
250 -> 3. Zeile p2 der linkesten Tabellenspalte ("explicit interface to WInf/IS, not")
251 -> 3. Zeile p3 der linkesten Tabellenspalte ("Business/Management, not Computer")
252 -> 3. Zeile p4 der linkesten Tabellenspalte ("Science)")
253 -> 2. Zeile p1 der linkesten Tabellenspalte ("Computer Science Journals")
254 -> 2. Zeile p2 der linkesten Tabellenspalte ("(without explicit interface to")
255 -> 2. Zeile p3 der linkesten Tabellenspalte ("WInf/IS)")

---
---

FÜR DIE PROCEEDINGS TABELLEN:
---

line_index 0-6 = heading; kann weg
line_index 7-11 = table header (im Vergleich zu Journals fehlt die ISSN Spalte!)
line_index 12-16 = erster Eintrag; Zeile 1
line_index 17-21 = zweiter Eintrag; Zeile 2
line_index 22-26 = dritter Eintrag; Zeile 3
...
=> Jede neue Tabellenzeile startet ab 12+5*n

Seite 5 (page_no = 4): Nach dem letzten "Link" Eintrag der Tabelle:
164 -> Header der Seite??? ("VHB Publication Media Rating 2024")
165 -> p1 der linkesten Tabellenspalte ("Wirtschaftsinformatik or Information")
166 -> p2 der linkesten Tabellenspalte ("Systems conference proceedings")

Seite 6 (page_no = 5): Nach dem letzten "Link" Eintrag der Tabelle:
12 -> Ist hier der Header der Seite??? ("VHB Publication Media Rating 2024")
ALSO hier gilt 13+5*n
119 -> "Categories"
120 -> "A+ Proceedings of outstanding and world-leading conferences"
121 -> "A  Proceedings of leading conferences"
122 -> "B  Proceedings of important and respected conferences"
123 -> "C  Proceedings of recognized conferences or recognized workshops/forums etc. at conferences"
124 -> "D  Proceedings of other academic conferences, workshops/forums"
125 ->  p1 der linkesten Tabellenspalte ("Proceedings of conferences with or at the")
126 ->  p2 der linkesten Tabellenspalte ("interface to Wirtschaftsinformatik or")
127 ->  p3 der linkesten Tabellenspalte ("Information Systems")

---
---

Die letzten 4 Zeilen sind immer der Footer:
len(page_lines)-4 -> Footer 1 ("© Verband der Hochschullehrerinnen und Hochschullehrer für Betriebswirtschaft e.V.")
len(page_lines)-3 -> Footer 2 ("Version: 04/18/2024")
len(page_lines)-2 -> Footer 3 ("Page 2 / 6")
len(page_lines)-1 -> Leerzeile
"""

import pandas as pd
import pymupdf
import sys



path_to_pdf = input("Enter the path to the PDF file: ").strip().strip('"')
doc = pymupdf.open(path_to_pdf, filetype="txt")

# NOTE: Journal table has 6 columns: Title, ISSN, Rating, Votes ≥ rating [%], Publisher, Link
journal_table = [[],[],[],[],[],[]]

# NOTE: Proceedings table has 5 columns: Title, Rating, Votes ≥ rating [%], Publisher, Link
proceedings_table = [[],[],[],[],[]]

# Iterate through all pages of the PDF document
for page_no in range(0, doc.page_count):
    print(f"--> Starting page {page_no}")

    table_content_line_column_index = 0
    reached_journal_table = False
    reached_proceedings_table = False

    page_text = doc[page_no].get_text()
    page_lines = page_text.split("\n")

    # Iterate through all lines of the page (minus the last footer lines)
    line_index = 0
    while line_index < len(page_lines) - 2:
        line = page_lines[line_index].strip()

        # Check if we reached the footer
        if line.startswith("©") and line_index == len(page_lines)-4:
            print(f"   > Expected footer reached on line {line_index}; breaking the line loop for page {page_no}")
            break
        elif line.startswith("©"):
            print(f"   > WARNING: Unexpected footer reached on line {line_index}; continuing...")
            break
        elif line_index >= len(page_lines)-4:
            print(f"   > WARNING: Expected footer not reached on line {line_index}; breaking the line loop for page {page_no}")
            break

        # Check if we reached the journal table header
        if line.lower() == "title" and page_lines[line_index+1].strip().upper() == "ISSN":

            if page_lines[line_index+2].strip().lower() == "rating" and page_lines[line_index+4].strip().lower() == "publisher" and page_lines[line_index+5].strip().lower() == "link":
                print(f"   > Table header for journals starting on line {line_index} and ending on line {line_index+5}")
                reached_journal_table = True
                reached_proceedings_table = False

                # Skip to the table content lines
                line_index += 6
                continue
            else:
                print(f"   > ERROR on p. {page_no}: Invalid parsing of the journal table header starting on {line_index}")
                print("==> The programm will exit now., sorry. :)")
                sys.exit(0)

        # Check if we reached the prceedings table header
        if line.lower() == "title" and page_lines[line_index+1].strip().lower() == "rating":

            if page_lines[line_index+3].strip().lower() == "publisher" and page_lines[line_index+4].strip().lower() == "link":
                print(f"   > Table header for proceedings starting on line {line_index} and ending on line {line_index+5}")
                reached_proceedings_table = True
                reached_journal_table = False
                
                # Skip to the table content lines
                line_index += 5
                continue
            else:
                print(f"   > ERROR on p. {page_no}: Invalid parsing of the proceedings table header starting on {line_index}")
                print(f"     -> The programm will skip the rest of page {page_no} and continue with the next page...")
                break

        # Ignore random heading parsing
        if line.startswith("VHB Publication Media Rating"):
            line_index += 1
            continue

        # Add normal lines to the respective list
        if reached_journal_table and not reached_proceedings_table:
            column_index = table_content_line_column_index % 6

            # Sanity Check for the ISSN column
            if column_index == 1:
                if line[0].isnumeric() and line[1].isnumeric() and line[2].isnumeric() and line[3].isnumeric() and line[4] == "-":
                    # Sanity Check passed; do nothing
                    pass
                else:
                    print(f"  >> WARNING on p. {page_no}: Expected ISSN entry reached on line {line_index}, but got '{line}' instead")
                    print(f"     -> Assuming this line belong to the title and continuing...")
                    journal_table[column_index-1][-1] += " " + line
                    line_index += 1
                    continue
                
            # Sanity Check for the Link column
            if column_index == 5:
                if line.lower() != "link":
                    print(f"  >> ERROR on p. {page_no}: Expected 'Link' entry reached on line {line_index}, but got '{line}' instead")
                    print(f"     -> The programm will skip the rest of page {page_no} and continue with the next page...")
                    break

            journal_table[column_index].append(line)
            table_content_line_column_index += 1

        elif reached_proceedings_table and not reached_journal_table:
            column_index = table_content_line_column_index % 5

            # Sanity Check for the Rating column
            if column_index == 1:
                if len(line) <= 2:
                    # Sanity Check passed; do nothing
                    pass
                else:
                    print(f"  >> WARNING on p. {page_no}: Expected Rating entry reached on line {line_index}, but got '{line}' instead")
                    print(f"     -> Assuming this line belong to the title and continuing...")
                    proceedings_table[column_index-1][-1] += " " + line
                    line_index += 1
                    continue

            # Sanity Check for the Link column
            if column_index == 4:
                if line.lower() != "link":
                    print(f"  >> ERROR on p. {page_no}: Expected 'Link' entry reached on line {line_index}, but got '{line}' instead")
                    print(f"     -> The programm will skip the rest of page {page_no} and continue with the next page...")
                    break

            proceedings_table[column_index].append(line)
            table_content_line_column_index += 1
        
        # End of while loop for the current line; increase the line_index
        line_index += 1

    print(f"--> Finished page {page_no}")


print(f"==> Finished parsing!")
print(f"----")
print(f"----")

# Build Path to save Excel
path_to_journal_excel = path_to_pdf[:-4] + "_journal.xlsx"
path_to_proceedings_excel = path_to_pdf[:-4] + "_proceedings.xlsx"

# Create the pandas DataFrames
print(f"JOURNAL TABLE:")
if len(journal_table[0]) > len(journal_table[1]):
    print(f"  >> WARNING: The number of entries in the 'Title' column is higher than in the 'ISSN' column")
    print(f"     -> Trying to cut the last entry of the title column...")

    journal_df = pd.DataFrame({
        'Title': journal_table[0][:len(journal_table[1])],
        'ISSN': journal_table[1],
        'Rating': journal_table[2],
        'Votes ≥ rating [%]': journal_table[3],
        'Publisher': journal_table[4],
        'Link': journal_table[5]
    })
else:
    journal_df = pd.DataFrame({
        'Title': journal_table[0],
        'ISSN': journal_table[1],
        'Rating': journal_table[2],
        'Votes ≥ rating [%]': journal_table[3],
        'Publisher': journal_table[4],
        'Link': journal_table[5]
    })
print(journal_df)
print(f"----")
journal_df.to_excel(path_to_journal_excel)
print(f"==> Saving the parsed data to Excel at the following path: {path_to_journal_excel}")
print(f"----")

print(f"PROCEEDINGS TABLE:")
if len(proceedings_table[0]) > len(proceedings_table[1]):
    print(f"  >> WARNING: The number of entries in the 'Title' column is higher than in the 'Rating' column")
    print(f"     -> Trying to cut the last entry of the title column...")

    proceedings_df = pd.DataFrame({
        'Title': proceedings_table[0][:len(proceedings_table[1])],
        'Rating': proceedings_table[1],
        'Votes ≥ rating [%]': proceedings_table[2],
        'Publisher': proceedings_table[3],
        'Link': proceedings_table[4]
    })
else:
    proceedings_df = pd.DataFrame({
        'Title': proceedings_table[0],
        'Rating': proceedings_table[1],
        'Votes ≥ rating [%]': proceedings_table[2],
        'Publisher': proceedings_table[3],
        'Link': proceedings_table[4]
    })
print(proceedings_df)
print(f"----")
proceedings_df.to_excel(path_to_proceedings_excel)
print(f"==> Saving the parsed data to Excel at the following path: {path_to_proceedings_excel}")
print(f"----")