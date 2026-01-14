from src.data.load_data import load_data
from src.data.preprocess import data_preprocess


def main():
    df = load_data()
    data_preprocess()


if __name__ == "__main__":
    main()
