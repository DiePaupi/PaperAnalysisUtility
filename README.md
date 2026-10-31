# Paper Analysis Utility (PAU)


## ❓ What is PAU?

This *Paper Analysis Utility (PAU)* is essentially a multi-stage academic paper auditing pipeline and will help with automatically checking:
1) the paper's structure and relative length of each section
2) the usage of references
    - if all publications referenced in the text are also detailed in the bibliography
    - if all publications listed in the bibliography are also used somewhere in the text
3) if any spcific author is referenced relativley often
4) the existance of provided references
    - PAU differentiates between mismatches in 
        - author names
        - publication years (>1year)
        - publication years (=1year)
    - and specifically lists references that could *not* be matched based on their title
5) the (JQ / CORE) ranking of the outlets of all references from the bibliography
6) if references given in sentences are a thematical match or seem unrelated

> [!IMPORTANT]
> PAU does ***not evaluate the content quality of a paper***. Instead, it focuses on questions like:
> - How is the paper structured?
> - Is the literature used correctly?
> - Are references consistent and verifiable?
> - Are the cited venues reputable?

This makes PAU useful for:
- 🧑‍🔬 **reviewers** performing quick technical checks
- 🎓 **students** learning how academic papers should reference literature


> [!NOTE]
> *PAU is available under the [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) licence.*
> *If you want to reference PAU, please use the following citation:*
> ```
> Speckmann, P., Fischer, R., & Janiesch, C. (2026). Check and Trust with PAU: A Paper Analysis Utility for Automated Bibliographic Verification. Proceedings of the AAAI ACM Conference on AI, Ethics, and Society, 9(4), 2408–2420. https://doi.org/10.1609/aies.v9i4.43316
> ```
> 
> *BibTeX export:*
> ```
> @inproceedings{
>     author    = {Speckmann, Pauline and Fischer, Raphael and Janiesch, Christian},
>     title     = {{C}heck and {T}rust {W}ith {PAU}: {A} {P}aper {A}nalysis {U}tility for {A}utomated {B}ibliographic {V}erification},
>     booktitle = {Proceedings of the AAAI/ACM conference on AI, Ethics, and Society (AIES)},
>     location  = {Malmö, Sweden},
>     year      = {2026},
>     volume    = {9},
>     number    = {4},
>     pages     = {2408--2420},
>     doi       = {10.1609/aies.v9i4.43316}
> }
> ```


## 🔍 How does PAU work?

Structurewise, PAU works as follows:
PDF → Structure Parsing
    → Reference Extraction
    → Reference Validation
    → In‑text Citation Analysis
    → Literature Quality Metrics
    → Outlet Ranking Analysis
    → LLM Semantic Checks
    → Report Generation

The architecture is modular with specialized components:
- ReferenceChecker → extracts and parses bibliography
- BibSearcher → validates references against external databases
    - PAU checks whether references actually exist and match their metadata. It automatically searches for publications using:
        - **Semantic Scholar**
        - **DBLP**
        - optional **Google Scholar fallback**
            - *Disclaimer: For educational purposes only; the Boolean variable ```USE_GS_AS_FALLBACK``` is set in the BibSearcher.py*
    - For each reference PAU verifies: title, authors, year, and link validity
        - Potential problems are flagged in the report.
For each reference PAU verifies: title, authors, year, and link validity
→ Potential problems are flagged in the report.
- RefIntextChecker → compares in‑text citations with bibliography
- AuthorsChecker → author frequency analysis
    - Per default, all (co-)authors referenced three or more times will be listed
    - You can define your own threshold by changing ```MAX_AUTHOR_REFERENCES``` in ```AuthorsChecker.py```
- RankingChecker → outlet quality assessment
- UnicodeChecker → formatting quality detection
- Main script → orchestrates the pipeline and generates the report

<img width="5735" height="2573" alt="PAU_uml_v4" src="https://github.com/user-attachments/assets/2515d997-c52c-4b60-9447-1ca5f748268e" />



---

### Comparing Citations with the Bibliography

PAU analyzes the paper text and extracts all in‑text citations.
It then checks:
- references cited in the text but missing from the bibliography
- references listed in the bibliography but never cited (in the main text; appendices excluded)

Supported referencing formats (as used within the document's text) include:
- Numeric citations
    - Example: ```[1]``` and ```[4,7]```
- Author‑year citations
    - Example: ```[Doe et al., 2025, Smith et al., 2021]``` or ```(Doe et al. 2025)```

Supported bibliography numberings (as used in the 'References' section) include:
- 'natbib' = No numbering; reference in 'References' section starts with the authors' names
- 'numbered_squares' = Numbers in square brackets; reference start with, e.g., ```[1]```
- 'number_with_dot' = Numberes followed by a point; reference start with, e.g., ```1.```

Supported bibliography layouts (as used in the 'References' section) include:
- 'LFTOY' = Lastname, Firstname, Title, Outlet, Year
    - This is, for example, used by Springer Nature
- 'LFYTO' = Lastname, Firstname, Year, Title, Outlet
    - This is, for example, used by the AAAI/ACM Conference
- 'FLYTO'   = Firstname, Lastname, Year, Title, Outlet
    - This is, for example, used by ACM
- 'FLTOY'  = Firstname, Lastname, Title, Outlet, Year
    - This is, for example, often used by the NeurIPS Conference

---

## 👩‍💻 How to use PAU?

### 1. Install Dependencies

PAU requires Python <= 3.11 and several libraries. Please check the requirements.txt for details.
Typical dependencies include:

```
pymupdf
pandas
plotly
requests
rich
openpyxl
scholarly
```

> [!NOTE]
> If you want to use all of PAU's functions, you'll need to provide LLM access by creating an `.env`-file in the `Libs` folder!
> There, you can provide the following keys:
> - an LLM provider for citation validation
>     - CampusKI (`CKI_API_KEY`); the default
>     - OpenAI (`OPENAI_API_KEY`); to use, please set `USE_CAMPUS_KI = False` in the `LLMCaller.py`
> - Semantic Scholar API access (`SEMANTIC_SCHOLAR_API_KEY`)
>
> *Please note that this is completly optional! Per default, PAU will ask you to confirm LLM functionalities, where you can just deny. :)*



### 2. Run PAU

Execute the main script: run ```python PAU.py``` or execute ```PAU.py``` via your IDE.

PAU will ask for a few inputs (see above for examples):

| Input | Description |
|-------|-------------|
| Path to the PDF file | The global path to the PDF file |
| formatting template | If there are header lines to consider; choose between ```springer``` = 2 header lines, and ```acm``` = no header lines |
| bibliography layout | The order in which the entries' information (namely **L**astname, **F**irstname, **T**itle, **O**utlet, and **Y**ear) are listed; choose between ```LFTOY```, ```LFYTO```, ```FLTOY```, and ```FLYTO``` |
| bibliography numbering style | The numbering preceding each bibliography entry; choose between ```natbib```, ```numbered_squares```, and ```number_with_dot``` |
| referencing style | Referring to how bibliographic entries are referenced within the text; choose between ```numeric``` and ```authoryear``` |



### 3. Inspect the Report

After processing the document, PAU generates a report:

```
PAU_results.md
```

The report includes:

- document structure analysis
- reference validation statistics
- missing or unused citations
- outlet rankings
- citation relevance checks
- full parsed reference list

Several charts are also generated and embedded into the report.

---

---

## 🫂 Want to get involved?

PAU was intentionally designed to be **easy to extend**.  
If you want to add new parsing rules, citation styles, or data sources, here is where to start.

---

### Reference Parsing

- File: ```Libs/ReferenceChecker.py```
- Core function: ```parse_reference()```
- Bibliography styles are defined near the top of the file.
    - Examples: ```LFTOY```, ```LFYTO```, ```FLTOY```, and ```FLYTO```
    - To support a new reference format:
        1. define a new layout dictionary
        2. add it to `supported_bib_layouts`
        3. extend the parsing logic in `parse_reference()`

---

### Reference Section Extraction

- File: ```Libs/ReferenceChecker.py```
- Important function: ```check_page_text()```
- This reconstructs full references from the raw PDF text using heuristics such as:
    - numbering patterns
    - year detection
    - author separators

---

### Author Normalization

- File: ```Libs/AuthorsChecker.py```
- Functions: ```normalize_authors_str()```, ```extract_authors_commasep()```, ```extract_authors_spacesep()```
- This module converts author names into a canonical form such as ```Smith J.``` which allows robust matching across databases.
    - Please note that only the first letter of the firstname is kept

---

### In‑Text Citation Parsing

- File: ```Libs/RefIntextChecker.py```
- Core function: ```compare_intext_references_to_bib()```
- Citation formats are defined at the top of the file.
    - To add a new citation style, add a new constant String, extend `supported_ref_templates`, and adjust the parsing in `IntextRefParser.py`.

---

### Literature Validation

- File: ```Libs/BibSearcher.py```
- Reference lookup uses *Semantic Scholar* and *DBLP*.
    - Matching logic is implemented in: ```compare_dicts_df_to_reference()```

---

### Venue Ranking Analysis

- File: ```Libs/RankingChecker.py```
- This module loads ranking datasets (given in the 'Rankings' folder) and matches them to parsed outlets.
    - You can add more ranking datasets to the folder and include their check in the RankingChecker.py by copying the relevant lines and adjusting the name; don't forget to also adjust the output (and charts) by adapting them in PAU.py!

---

### Document Structure Analysis

- Main script: ```PAU.py```
- Key functions: ```parse_numbered_headings()```, ```parse_unnumbered_headings()```, and ```check_document_structure()```
- NOTE: These detect headings and compute section lengths; especially the unnumbered headings are a general heuristic, so feel free to extend!
