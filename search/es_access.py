# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch

def import_to_es(es_index,es_type,es_id,data_json):
	print '开始写es'
	es=Elasticsearch('10.1.201.152')#Elasticsearch('ip')
	res=es.index(index = es_index, doc_type = es_type,id = es_id,body = data_json)
	res['created']

