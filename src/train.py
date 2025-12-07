import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from src.preprocess import load_data, clean_data
from src.utils import save_model, evaluate

def train_model():

    # 1. Load
    df = load_data("data/cleaned_olist.csv")

    # 2. Clean
    df = clean_data(df)

    # 3. Split X/y
    X = df.drop("late_delivery", axis=1)
    y = df["late_delivery"]

    # 4. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 5. Model
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    # 6. Predict
    preds = model.predict(X_test)

    # 7. Eval
    metrics = evaluate(y_test, preds)
    print("Model Metrics:", metrics)

    # 8. Save model
    save_model(model, "models/model.joblib")

if __name__ == "__main__":
    train_model()
