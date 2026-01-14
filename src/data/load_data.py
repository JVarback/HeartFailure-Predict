from src.config import RAW_DATA_DIR

from pathlib import Path
import pandas as pd


def load_data(filename: str = "heart.csv") -> pd.DataFrame:
    file_path: Path = RAW_DATA_DIR / filename
    df: pd.DataFrame = pd.read_csv(file_path)

    return df
