from datetime import timedelta

from feast import Entity, FeatureView, Field, ValueType
from feast.infra.offline_stores.bigquery_source import BigQuerySource
from feast.types import Float32, Int64, String

# 1. Defining entity
flower = Entity(
    name="flower_id",
    join_keys=["flower_id"],
    # value_type=Int64,
    description="Unique identifier for each Iris flower"
)

# 2. BigQuery source (offline store)
iris_source = BigQuerySource(
    table="true-sprite-459511-f5.iris_feast_pipeline.iris_table",  # project.dataset.table
    timestamp_field="event_timestamp",
    # created_timestamp_column="created",
)

# 3. Feature view definition
iris_features = FeatureView(
    name="iris_features",
    entities=[flower],
    ttl=timedelta(weeks=52),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width",  dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width",  dtype=Float32),
        Field(name="species",      dtype=String),
    ],
    source=iris_source,
    online=True,
    tags={
        "domain": "iris",
        "version": "feast"
    }
)
