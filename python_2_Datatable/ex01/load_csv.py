import pandas as pd


def load(path: str):
    """Load a CSV file and return a pandas DataFrame."""
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    print(load("life_expectancy_years.csv"))
