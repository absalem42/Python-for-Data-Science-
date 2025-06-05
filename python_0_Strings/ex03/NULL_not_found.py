def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object.__class__ is float and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif object.__class__ is int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object.__class__ is str and object.__len__() == 0:
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0


# if isinstance(object, list):
#         print(f"List : {type(object)}$")


def main():
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ""
    Fake = False

    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))


if __name__ == "__main__":
    main()


# import numpy as np
# import pandas as pd

# def print_null_types():
#     """Prints the type of different null representations in Python."""

#     print(f"Type of None: {type(None)}")
#     print(f"Type of numpy.nan: {type(np.nan)}")

#     df = pd.DataFrame({'col1': [None, np.nan]})
#     print(f"Type of null in Pandas Series: {type(df['col1'][0])}")

# print_null_types()
