import pandas as pd


def load(path: str):
    
    try:
        data = pd.read_csv(path)
        return data

    except Exception as e:
        print(f"Error: {e}")
        return None
