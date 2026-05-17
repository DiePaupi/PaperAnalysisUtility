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
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print(f"  -> Failed to query dblp API. Status code: {response.status_code}")
        return ""
    else:
        return response.text


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
    get_dblp_result_df(["Speckmann", "Nadj", "Janiesch", "2025"], None)

    """
    Example result from query_papers:
    '{\r\n"result":{
        \r\n"query":"Speckmann* Nadj* Janiesch* 2025*",
        \r\n"status":{\r\n"@code":"200",\r\n"text":"OK"\r\n},
        \r\n"time":{\r\n"@unit":"msecs",\r\n"text":"36.55"\r\n},
        \r\n"completions":{\r\n"@total":"1",\r\n"@computed":"1",\r\n"@sent":"1",\r\n"c":{\r\n"@sc":"2",\r\n"@dc":"2",\r\n"@oc":"2",\r\n"@id":"66779749",\r\n"text":"2025"\r\n}\r\n},
        \r\n"hits":{
            \r\n"@total":"2",
            \r\n"@computed":"2",
            \r\n"@sent":"2",
            \r\n"@first":"0",
            \r\n"hit":[{
                \r\n"@score":"4",
                \r\n"@id":"439038",
                \r\n"info":{"authors":{"author":[{"@pid":"407/0203","text":"Pauline Speckmann"},{"@pid":"172/6888","text":"Mario Nadj"},{"@pid":"54/2624","text":"Christian Janiesch"}]},
                            "title":"Interactive Explainable Intelligent Systems: Requirements, Design Principles, and Prototypical Implementation.",
                            "venue":"DESRIST",
                            "pages":"51-65",
                            "year":"2025",
                            "type":"Conference and Workshop Papers",
                            "access":"closed",
                            "key":"conf/desrist/SpeckmannNJ25",
                            "doi":"10.1007/978-3-031-93979-2_4",
                            "ee":"https://doi.org/10.1007/978-3-031-93979-2_4",
                            "url":"https://dblp.org/rec/conf/desrist/SpeckmannNJ25"},
                \r\n"url":"URL#439038"\r\n},
            \r\n{\r\n"@score":"4",
                \r\n"@id":"647175",
                \r\n"info":{"authors":{"author":[{"@pid":"407/0203","text":"Pauline Speckmann"},{"@pid":"172/6888","text":"Mario Nadj"},{"@pid":"54/2624","text":"Christian Janiesch"}]},
                    "title":"IXAII: An Interactive Explainable Artificial Intelligence Interface for Decision Support Systems.",
                    "venue":"CoRR",
                    "volume":"abs/2506.21310",
                    "year":"2025",
                    "type":"Informal and Other Publications",
                    "access":"open",
                    "key":"journals/corr/abs-2506-21310",
                    "doi":"10.48550/ARXIV.2506.21310",
                    "ee":"https://doi.org/10.48550/arXiv.2506.21310",
                    "url":"https://dblp.org/rec/journals/corr/abs-2506-21310"},
                \r\n"url":"URL#647175"\r\n}
            \r\n]\r\n}
        \r\n}
    \r\n}
    \r\n'
    """