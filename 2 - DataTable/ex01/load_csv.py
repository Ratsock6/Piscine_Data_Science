import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file from the given path.

    Prints the dimensions of the dataset and returns it as a DataFrame.
    Returns None if the path is invalid or the file cannot be read.
    """
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Entry point for testing the load function."""
    from load_csv import load
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()