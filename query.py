from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
def get_all_entries():
    query = {
        "query": {
            "match_all": {}
        }
    }
    result = es.search(index="employee_index", body=query, size=1000,
scroll='2m')
    scroll_id = result['_scroll_id']
    hits = result['hits']['hits']      
    while len(result['hits']['hits']):
       result = es.scroll(scroll_id=scroll_id, scroll='2m')
       hits.extend(result['hits']['hits'])
    return hits
if __name__ == "__main__":
  entries = get_all_entries()
  for entry in entries:
      print(entry['_source'])
