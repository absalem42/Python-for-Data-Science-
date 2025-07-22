import numpy as np

def validate_lists(data):
    """
    Validates if element in is an list.

    Args:
        data: A list of lists.

    Returns:
        True if all elements are lists, False otherwise.
    """

    for item in data:
        if not isinstance(item, list):
            return False
    return True



def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError(f"Expected 'family' to be a list, got {type(family).__name__}")
    "Error: 'family' must be a list."

    if len(family) == 0:
        raise ValueError("There is nothing to show")
    if not validate_lists(family):
        raise ValueError("All elements in height must be integers or floats.")

    if not isinstance(start, int):
        raise TypeError(f"Start index must be an integer, got {type(start).__name__}")
    if not isinstance(end, int):
        raise TypeError(f"End index must be an integer, got {type(end).__name__}")
    
    my_numpy_array = np.array(family)
    print(f"My shape is : {my_numpy_array.shape}")
    sliced =  my_numpy_array[start:end]
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()










def main():
    try:    
        family = [[1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
