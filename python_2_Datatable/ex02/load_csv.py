import pandas as pd


def load(path: str):
    """
    Loads a CSV file into a pandas DataFrame, prints its dimensions,
    and returns it.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    try:
        data = pd.read_csv(path)
        print(f"Data loaded with shape: {data.shape}")
        return data

    except Exception as e:
        print(f"Error: {e}")
        return None
