import sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.data.load_data import load_data
from src.schemas import DataframeWrapper


def data_preprocess() -> DataframeWrapper:
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

    train, test = train_test_split(df, test_size=0.2)

    return DataframeWrapper(df=df, train_data=train, test_data=test)
