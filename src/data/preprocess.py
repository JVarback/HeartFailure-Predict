from src.data.load_data import load_data
import pandas as pd


def data_preprocess() -> pd.DataFrame:
    df = load_data()
    print(f"Shape of the Data: {df.shape}")
    print(df.head(5))
    print(df.info())  # Does a check to see if there is any Null values for each of the columns
    print(df.isnull().sum())  # Returns the number of missing values
    print(f'Remove cholesterol values of 0: {len(df[df["Cholesterol"] == 0])}')
    indices_to_drop = df[df["Cholesterol"] == 0].index
    df.drop(indices_to_drop, inplace=True)
    print(f'Remove cholesterol values of 0: {len(df[df["Cholesterol"] == 0])}')
    print(f"Shape of the Data: {df.shape}")

    return df
