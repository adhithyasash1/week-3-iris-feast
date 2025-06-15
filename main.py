import pandas as pd
from feast import FeatureStore
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load historical features
store = FeatureStore(repo_path=".")

entity_df = pd.DataFrame({
    "flower_id": list(range(3)) * 50,  # 150 samples across 3 classes
    "event_timestamp": pd.to_datetime("now")
})

# Pull features
features_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_features:sepal_length",
        "iris_features:sepal_width",
        "iris_features:petal_length",
        "iris_features:petal_width",
        "iris_features:species"
    ]
).to_df()

# Prepare data
X = features_df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = features_df["species"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, stratify=y, random_state=42)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {acc:.3f}")
