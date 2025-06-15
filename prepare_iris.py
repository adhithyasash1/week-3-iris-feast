import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from datetime import datetime

# Load base Iris dataset
df = pd.read_csv("data/iris.csv")

# Add flower_id using label encoding of species
encoder = OrdinalEncoder()
df["flower_id"] = encoder.fit_transform(df[["species"]]).astype(int)

# Add event_timestamp required for Feast
df["event_timestamp"] = pd.to_datetime(datetime.now())

# Save processed file
df.to_csv("data/iris.csv", index=False)
print("✅ Modified iris.csv with flower_id and event_timestamp.")
