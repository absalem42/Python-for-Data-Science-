import numpy as np


def validate_lists(data: list) -> bool:
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
    """
    Slice a 2D list (list of lists) from 'start' to 'end',
     print original and new shapes, and return the result.

    Converts the input to a NumPy array, prints
     its shape before and after slicing,
    then returns the sliced portion as a Python list of lists.

    Args:
        family (list): A non-empty list of lists
         with numeric values (int or float).
        start (int): Start index (inclusive).
        end (int): End index (exclusive).

    Returns:
        list: The sliced 2D list.

    Raises:
        TypeError: If arguments are of incorrect types.
        ValueError: If 'family' is empty or contains invalid elements.
    """

    if not isinstance(family, list):
        raise TypeError("Expected 'family' to be a list.")
    "Error: 'family' must be a list."

    if len(family) == 0:
        raise ValueError("Input 'family' is an empty list.")
    if not validate_lists(family):
        raise ValueError("All elements in lists must be list.")

    if not isinstance(start, int):
        raise TypeError("Start index must be an integer.")
    if not isinstance(end, int):
        raise TypeError("End index must be an integer.")

    my_numpy_array = np.array(family)
    print(f"My shape is : {my_numpy_array.shape}")
    sliced = my_numpy_array[start:end]
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()


# def main():
#     try:
#         family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
#         print(slice_me(family, 0, 2))
#         print(slice_me(family, 1, -2))
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# if __name__ == "__main__":
#     main()
