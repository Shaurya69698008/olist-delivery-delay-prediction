import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.copy()
    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

def save_cleaned_data(df, out_path):
    df.to_csv(out_path, index=False)
