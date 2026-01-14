from src.data.load_data import load_data


def data_preprocess():
    df = load_data()
    print(f"Shape of the Data: {df.shape}")
    print(df.head(5))
    print(df.info())  # Does a check to see if there is any Null values for each of the columns
    print(df.isnull().sum())  # Returns the number of missing values
