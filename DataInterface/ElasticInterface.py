#!/usr/bin/python3
from DataInterface.DatabaseInterface import *
from elasticsearch import Elasticsearch

class ElasticFetcher(DatabaseFetcher):
    def __init__(databaseLocation):
        pass
    def get(location):
        return NotImplemented
    def check(location):
        return NotImplemented

class ElasticUploader(DatabaseUploader):
    def __init__(databaseLocation):
        pass
    def push(data,location):
        return NotImplemented
