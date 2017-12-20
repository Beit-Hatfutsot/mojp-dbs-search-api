import json
import requests

# from mojp_dbs_search_api import main
data = json.loads(open("c:\\temp\\temp.txt", "r", encoding="utf-8").read())
requests.post("http://127.0.0.1:8888/index/places", json.dumps(data))
