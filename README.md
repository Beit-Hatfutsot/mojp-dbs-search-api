# mojp-dbs-search-api


## Running

```
docker-compose up -d --build
```

* http://localhost:18000/search/places/poland///4/0

This is the search URL format:

`http://localhost:5000/search/comma_seperated_table_names/search_term/from_data/to_date/maxinum_size_of_result/offset`


## Configuration

The following environment variables are supported:

* `ES_HOST` / `ES_PORT` - elasticsedarch connection details


## Development

```
python3 -c 'from mojp_dbs_search_api.main import app; app.run()'
```
