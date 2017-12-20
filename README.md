# mojp-dbs-search-api


## Running

```
docker-compose up -d --build
```

* http://localhost:18000/search/exemptions/web/2000-01-01/2019-01-01/4/0
* http://localhost:18000/search/budget,national-budget-changes,contract-spending,entities/%D7%9E%D7%99%D7%A7/1992-01-01/2019-01-01/10/0


## Configuration

The following environment variables are supported:

* `ES_HOST` / `ES_PORT` - elasticsedarch connection details


## Development

```
python3 -c 'from mojp_dbs_search_api.main import app; app.run()'
```

This is the search URL format:

`http://localhost:5000/search/comma_seperated_table_names/search_term/from_data/to_date/maxinum_size_of_result/offset`

for example - http://localhost:5000/search/places/poland///4/0


