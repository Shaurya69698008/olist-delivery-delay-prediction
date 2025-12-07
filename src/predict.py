import pandas as pd
from src.utils import load_model
from src.preprocess import clean_data

def predict_new(csv_path):

    df = pd.read_csv(csv_path)
    df = clean_data(df)

    model = load_model("models/model.joblib")
    preds = model.predict(df)

    df["prediction"] = preds
    df.to_csv("data/predictions.csv", index=False)

    print("Predictions saved to data/predictions.csv")


if __name__ == "__main__":
    predict_new("data/new_data_for_scoring.csv")
