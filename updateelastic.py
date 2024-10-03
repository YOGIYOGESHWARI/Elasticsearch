from elasticsearch import Elasticsearch, helpers
import csv
es = Elasticsearch("http://localhost:9200")
with open('Employee Sample Data 1.csv') as f:
   reader = csv.DictReader(f)
   helpers.bulk(es, reader, index='employee_index')                                                                                                 