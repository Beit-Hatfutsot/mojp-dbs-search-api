import os
import elasticsearch

# port 9200 is exposed by the default docker compose environment
ES_HOST = os.environ.get('ES_HOST', 'localhost')
ES_PORT = os.environ.get('ES_PORT', '9200')

es_connection_string = '{}:{}'.format(ES_HOST, ES_PORT)

INDEX_NAME = os.environ.get('INDEX_NAME', 'mojp')
ES_SERVERS_LIST = [{"host": ES_HOST, "port": int(ES_PORT)}]
DEFAULT_TIMEOUT = 60

SEARCHABLE_DATAPACKAGES = [
    "../mojp-dbs-pipelines/data/clearmash/download-entities/datapackage.json"
    # "https://storage.googleapis.com/mojp-dbs-data/places/datapackage.json",
    # "https://storage.googleapis.com/mojp-dbs-data/photoUnits/datapackage.json",
    # "https://storage.googleapis.com/mojp-dbs-data/persons/datapackage.json",
    # "https://storage.googleapis.com/mojp-dbs-data/movies/datapackage.json",
    # "https://storage.googleapis.com/mojp-dbs-data/personalities/datapackage.json",
    # "https://storage.googleapis.com/mojp-dbs-data/familyNames/datapackage.json",
]
NON_SEARCHABLE_DATAPACKAGES = [
    # "https://storage.googleapis.com/mojp-dbs-data/documents/datapackage.json",
]

_es = None


def get_es_client():
    global _es
    if _es is None:
        _es = elasticsearch.Elasticsearch(ES_SERVERS_LIST, timeout=DEFAULT_TIMEOUT)
    return _es
