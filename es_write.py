from elasticsearch import Elasticsearch
import json
import sys

es = Elasticsearch(host="localhost", port=9200)

infile = 'newref.json'
readfile = open(infile, "r")
line = readfile.readline()
while(line):
    jsondata = json.loads(line)
    if jsondata:
        query = {"query": {
            "match": {
                "id": jsondata['id']
            }
        }}
        es.delete_by_query(index='aminer_papers', body=query)
        es.index(index="aminer_papers",body=jsondata)
        result = es.search(index="aminer_papers",
                               body=query)
        line = readfile.readline()
