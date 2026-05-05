###############################################################################
# Imports
###############################################################################
from dotenv import load_dotenv
import os
from pathlib import Path
import requests

import pandas as pd



###############################################################################
# INFO
###############################################################################

# Semantic Scholar contains three APIs, each with its own unique base URL:
# -> See https://www.semanticscholar.org/product/api/tutorial
# - Academic Graph API returns details about papers, paper authors, paper citations \
#   and references.
#    -> Base URL: https://api.semanticscholar.org/graph/v1
# - Recommendations API recommends papers based on other papers you give it.
#    -> Base URL: https://api.semanticscholar.org/recommendations/v1
# - Datasets API lets you download Semantic Scholar's datasets onto your local machine, \
#   so you can host the data yourself and do custom queries.
#    -> Base URL: https://api.semanticscholar.org/datasets/v1

# Query for a bulk search: str
# - Text query that will be matched against the paper's title and abstract.
# - All terms are stemmed in English.
# - By default all terms in the query must be present in the paper.

# Specific paper search
#paper_id = "???"
#url = f"https://api.semanticscholar.org/graph/v1/paper/{paperId}"
#query_params = {"fields": "title,year,abstract"}
#headers = {"x-api-key": api_key}



###############################################################################
# Gloal Variables
###############################################################################
cwd = os.getcwd()
path_to_env = Path(os.path.join(cwd, "SubScripts",".env"))

MAX_RETRIES = 100



###############################################################################
# Helper functions
###############################################################################

def generate_bulk_query(keywords: list):
    load_dotenv(path_to_env)
    SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    if not SEMANTIC_SCHOLAR_API_KEY:
        api_key = ""
    else:
        api_key = SEMANTIC_SCHOLAR_API_KEY

    # Keyword paper search
    url = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
    query_params = {"query" : '+'.join(kw for kw in keywords),
                    "fields": "authors,title,year,abstract",
                    "year": f"{int(keywords[-1])-1}-{int(keywords[-1])+1}"}
    headers = {"x-api-key": api_key}

    return url, query_params, headers


def generate_title_query(query: str):
    load_dotenv(path_to_env)
    SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    if not SEMANTIC_SCHOLAR_API_KEY:
        api_key = ""
    else:
        api_key = SEMANTIC_SCHOLAR_API_KEY

    # Title paper search
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    query_params = {"query" : query,
                    "fields": "authors,title,year,abstract"}
    headers = {"x-api-key": api_key}

    return url, query_params, headers
    

def query_papers(query, do_title_search: bool):
    if do_title_search:
        url, query_params, headers = generate_title_query(query)
    else:
        url, query_params, headers = generate_bulk_query(query)

    for i in range(0, MAX_RETRIES):
        response = requests.get(url, params=query_params, headers=headers)

        if response.status_code == 429:
            if i % 10 == 1:
                print(f"  -> Semantic Scholar not reachable, trying again ... (TryCount = {i})")
            continue
        elif response.status_code != 200:
            print(f"  -> Failed to query SemanticScholar API. Status code: {response.status_code}")
            return ""
        else:
            return response.json()


def parse_title_results(semantic_scholar_result: str):
    data = []

    if 'data' in semantic_scholar_result:
        hit_list = semantic_scholar_result['data']
        for hit in hit_list:
            try:
                if 'title' in hit and 'year' in hit and 'authors' in hit \
                    and 'abstract' in hit and 'openAccessPdf' in hit:
                    data.append({
                        'title': hit['title'] if hit['title'] else "unknown",
                        'year': int(hit['year']) if hit['year'] else 0,
                        'authors': [author_dict['name'] for author_dict in hit['authors']],
                        'abstract': hit['abstract'] if hit['abstract'] else "unknown"
                    })
            except Exception as e:
                print(f"  => ERROR parsing semantic scholar title search results: {e}")
                return pd.DataFrame()
    else:
        print(f"  => ERROR: Semantic Scholar didn't find any results to parse!")
        return pd.DataFrame()
    
    return pd.DataFrame(data)



###############################################################################
# Main code
###############################################################################

def get_semantic_scholar_result_df(query, do_title_search: bool, path_to_results: str):
    all_results = query_papers(query, do_title_search)
    if do_title_search and all_results:
        data = parse_title_results(all_results)
    elif not do_title_search and all_results:
        # TODO
        return pd.DataFrame()
    else:
        return pd.DataFrame()

    if path_to_results:
        data.to_csv(path_to_results, index=False, sep=';')
    
    return data



# TESTING
if __name__ == "__main__":
    get_semantic_scholar_result_df("Interactive Explainable Intelligent Systems: Requirements, Design Principles, and Prototypical Implementation", True, None)

    """
    Example result from query_papers:
    {'total': 37, 
     'offset': 0,
     'next': 10,
     'data': [
        {'paperId': 'f3227aa3c925881801b72661c832c7dfa37d5f30', 
         'title': 'Interactive Explainable Intelligent Systems: Requirements, Design Principles, and Prototypical Implementation',
         'year': 2025,
         'openAccessPdf': {...},
         'authors': [...],
         'abstract': None},
        {'paperId': '010ff11cd9efdf9ddd71f8c464fc4e5b8e3c2f29',
         'title': 'From engineering principles to healthcare practice: A hybrid reasoning framework for transparent clinical decision support',
         'year': 2026,
         'openAccessPdf': {...},
         'authors': [...],
         'abstract': 'Clinical decision support systems (CDSS) are increasingly reliant on purely data-driven machine learning models, 
                      leading to significant challenges in clinical adoption due to their “black-box” nature, high risk of algorithmic bias, 
                      and inability to enforce hard safety constraints. This lack of transparency and clinical alignment poses major challenges 
                      for regulatory compliance and professional trust. This study proposes a novel hybrid artificial intelligence (AI) 
                      meta-model for CDSS design, which formally translates established engineering decision support paradigms into the 
                      clinical domain to create systems that are inherently safer and more explainable. The framework rigorously integrates: 
                      (i) Web Ontology Language 2 for formalizing medical concepts; (ii) a semantic web rule language rule base to serve as 
                      “clinical guardrails” for enforcing evidence-based guidelines and safety constraints; and (iii) a modular inference policy 
                      that intelligently matches decision problems with specific data-driven or probabilistic methods. A prototype was 
                      implemented, combining this explicit knowledge layer with modular inference engines and template-based explanations. 
                      Evaluation across two large-scale clinical tasks (oncology using the Surveillance, Epidemiology, and End Results database 
                      and intensive care using the Medical Information Mart for Intensive Care-IV database) demonstrated superior performance over 
                      data-driven baselines. Specifically, the hybrid system achieved a 78% reduction in guideline-violation errors (reducing 
                      the contraindication rate from 18% to 6%) while maintaining high predictive accuracy (area under the receiver operating 
                      characteristic curve of 0.84 and 0.87, respectively). Furthermore, a clinician usability study confirmed that the 
                      transparent, knowledge-driven explanations resulted in significantly higher decision clarity (Likert rating of 6.2/7) 
                      and reduced cognitive load. The findings validate that this hybrid AI architecture represents a robust and transferable 
                      approach to designing clinically aligned, trustworthy, and explainable CDSS, directly addressing critical requirements 
                      for the responsible deployment of AI in healthcare.'}, 
        ...
    """