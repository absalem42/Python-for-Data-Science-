import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame, prints its dimensions,
    and returns it.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame | None: The loaded DataFrame, or None if an error occurs.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except Exception:
        return None
