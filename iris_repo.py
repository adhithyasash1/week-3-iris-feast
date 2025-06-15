from feast import Entity, FeatureView, BigQuerySource
from feast.types import Float32, String
from datetime import timedelta

# Define Entity
flower = Entity(
    name="flower_id",
    join_keys=["flower_id"],
    description="ID of each Iris flower",
)

# Define BigQuery Source
iris_source = BigQuerySource(
    table_ref="your-gcp-project.iris_dataset.iris_table",  # should update this
    event_timestamp_column="event_timestamp",
)

# Define Feature View
iris_feature_view = FeatureView(
    name="iris_features",
    entities=[flower],
    ttl=timedelta(days=1),
    schema=[
        {"name": "sepal_length", "dtype": Float32},
        {"name": "sepal_width", "dtype": Float32},
        {"name": "petal_length", "dtype": Float32},
        {"name": "petal_width", "dtype": Float32},
        {"name": "species", "dtype": String}
    ],
    online=False,  # using only historical features
    source=iris_source,
)
