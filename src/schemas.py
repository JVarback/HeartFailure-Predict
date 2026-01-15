from pydantic import BaseModel
from pydantic import ConfigDict
import pandas as pd


class DataframeWrapper(BaseModel):
    df: pd.DataFrame
    train_data: pd.DataFrame
    test_data: pd.DataFrame

    model_config = ConfigDict(arbitrary_types_allowed=True)
