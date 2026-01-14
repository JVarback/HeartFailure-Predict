from src.data.load_data import load_data


def main():
    df = load_data()
    print(df.head())


if __name__ == "__main__":
    main()
