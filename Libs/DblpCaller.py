###############################################################################
# Imports
###############################################################################
import json
import requests

import pandas as pd



###############################################################################
# INFO
###############################################################################



###############################################################################
# Gloal Variables
###############################################################################



###############################################################################
# Helper functions
###############################################################################

def generate_query(keywords: list, batch: int, batch_size: int):
    """
    https://dblp.org/faq/How+to+use+the+dblp+search+API.html
      - https://dblp.org/search/publ/api for publication queries
      - https://dblp.org/search/author/api for author queries
      - https://dblp.org/search/venue/api for venue queries
      - q = The query string to search for
      - format = The result format of the search. 
                 Recognized values are "xml", "json", and "jsonp".
      - h = Maximum number of search results (hits) to return. 
            For bandwidth reasons, this number is capped at 1000.
      - f = The first hit in the numbered sequence of search results (starting with 0) to return. 
            In combination with the h parameter, this parameter can be used for pagination of search results.
      - c = Maximum number of completion terms (see below) to return.
            For bandwidth reasons, this number is capped at 1000.

    https://dblp.org/faq/1474589.html
      - prefix search = default; "sig" matches "SIGIR" as well as "signal"
      - exact word = append dollar sign ($); "graph$" matches "graph", but not "graphics"
      - boolean AND = separate words by space; "codd model" matches "Codd's Relational Model" and "A Model by Codd"
      - boolean OR = connect words by pipe symbol (|); "graph|network" matches "graph algorithm" and "Network Analysis"
    """

    base_url = "https://dblp.org/search/publ/api"
    params = {
        "q": ', '.join(kw for kw in keywords),
        "h": batch_size,
        "f": batch * batch_size,  # Max results per query
        "format": "json"
    }
    return base_url, params
    

def query_papers(keywords: list, batch_size=1000):
    base_url, params = generate_query(keywords, 0, batch_size)
    try:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"  -> Failed to query dblp API. Status code: {response.status_code}")
            return ""
        else:
            return response.text
    except Exception as e:
        print(f"  => ERROR: Reaching dblp failed: {e}")
        return ""


def parse_results(dblp_result: str):
    data = []
    try:
        res_json = json.loads(dblp_result)
        hit_list = res_json['result']['hits']['hit']
    except Exception as e:
        print(f"  => ERROR loading dblp result as JSON: {e}")
        return pd.DataFrame()

    for hit in hit_list:
        try:
            hit_info = hit['info']
            
            author_list = []
            if 'authors' in hit_info:
                author_dict_list = hit_info['authors']['author']
                if type(author_dict_list) is list:
                    for author_dict in author_dict_list:
                        if "text" in author_dict:
                            author_list.append(author_dict['text'])
                else:
                    if "text" in author_dict_list:
                        author_list.append(author_dict_list['text'])
            
            year = 0
            if 'year' in hit_info:
                if type(hit_info['year']) is list:
                    year = int(hit_info['year'][-1])
                else:
                    year = int(hit_info['year'])

            if 'title' in hit_info and 'year' in hit_info and 'authors' in hit_info and \
               'venue' in hit_info and 'pages' in hit_info and 'access' in hit_info and \
               'doi' in hit_info:
                
                data.append({
                    'title': hit_info['title'],
                    'year': year,
                    'authors': author_list,
                    'outlet': hit_info['venue'],
                    'pages': hit_info['pages'],
                    'access': hit_info['access'],
                    'link': hit_info['ee']
                })
            elif 'title' in hit_info and 'year' in hit_info and 'authors' in hit_info and \
                 'venue' in hit_info and 'access' in hit_info and 'doi' in hit_info:
                data.append({
                    'title': hit_info['title'],
                    'year': year,
                    'authors': author_list,
                    'outlet': hit_info['venue'],
                    'pages': "unknown",
                    'access': hit_info['access'],
                    'link': hit_info['ee']
                })
            elif 'title' in hit_info and 'year' in hit_info and 'authors' in hit_info:
                data.append({
                    'title': hit_info['title'],
                    'year': year,
                    'authors': author_list,
                    'outlet': "unknown",
                    'pages': "unknown",
                    'access': "unknown",
                    'link': "unknown"
                })
        except Exception as e:
            print(f"  => ERROR parsing dblp results: {e}")
            return pd.DataFrame()
    
    return pd.DataFrame(data)



###############################################################################
# Main code
###############################################################################

def get_dblp_result_df(keywords:list, path_to_results: str):
    all_results = query_papers(keywords)
    data = parse_results(all_results)

    if path_to_results:
        data.to_csv(path_to_results, index=False, sep=';')
    
    return data



# TESTING
if __name__ == "__main__":
    get_dblp_result_df(["Turing", "1950"], None)
