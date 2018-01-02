from .data_source import DataSource

searchable_sources = [
    DataSource("../mojp-dbs-pipelines/data/clearmash/places/datapackage.json"),
    DataSource("../mojp-dbs-pipelines/data/clearmash/familynames/datapackage.json"),
    DataSource("../mojp-dbs-pipelines/data/clearmash/movies/datapackage.json"),
    DataSource("../mojp-dbs-pipelines/data/clearmash/personalities/datapackage.json"),
    DataSource("../mojp-dbs-pipelines/data/clearmash/photounits/datapackage.json"),
]
non_searchable_sources = []


sources = dict(
    (ds.type_name, ds) for ds in searchable_sources
)


all_sources = non_searchable_sources + searchable_sources
all_sources = dict(
    (ds.type_name, ds) for ds in all_sources
)
