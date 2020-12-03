from elasticsearch import Elasticsearch

es=Elasticsearch()
# created=es.indices.create(index="demo1",ignore=400) #command to create index
# print(created)
#
# deleted=es.indices.delete(index="demo1") #command to delete index
# print(deleted)

#exists=es.indices.exists(index="demo1") #command to find if index exists or not

doc1={"name":"Utkarsh","city":"Kanpur"}
doc2={"name":"Prat","city":"Washington"}
es.index(index="dataset",doc_type="personsInfo",id=2,body=doc1)
es.index(index="dataset",doc_type="personsInfo",id=1,body=doc2)
es.get(index="dataset",id=1)
result=es.search(index="dataset",body={"from":0,"size":1,"query":{"match":{"name":"Prat"}}})#query for search
print(result)