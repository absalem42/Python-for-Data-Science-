import pandas as pd



def load(path: str):
    try:
        data = pd.read_csv(path)

        # print(f"Loading dataset of dimensions ... {data.shape}")

        return data

    except Exception as e:
        print(f"Error: {e}")
        return None






if __name__ == "__main__":
    print(load("life_expectancy_years.csv"))
    










# i need to write the dimensions of the data set after oepning the file 