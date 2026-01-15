from src.data.load_data import load_data
from src.data.preprocess import data_preprocess
from src.models.logistic_regression import log_regression


def main():
    data = data_preprocess()

    log_regression(data.train_data, data.train_labels, data.test_data, data.test_labels)


if __name__ == "__main__":
    main()
