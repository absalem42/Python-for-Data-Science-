def validate_int_float(data):
    """
    Validates if each element in a list is an integer or a float.

    Args:
        data: A list of elements.

    Returns:
        True if all elements are integers or floats, False otherwise.
    """

    for item in data:
        if not isinstance(item, (int, float)):
            return False
    return True


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculates the BMI for each pair of height and weight.

    Args:
        height: A list of heights (int or float).
        weight: A list of weights (int or float).

    Returns:
        A list of BMI values (float).

    Raises:
        ValueError: If the lists are
         not the same length or contain non-numeric values.
    """

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be the same length.")
    if not validate_int_float(height):
        raise ValueError("All elements in height must be integers or floats.")
    if not validate_int_float(weight):
        raise ValueError("All elements in weight must be integers or floats.")
    Bmi = []
    for (
        h,
        w,
    ) in zip(height, weight):
        Bmi.append(w / h**2)
    return Bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if each BMI value is above a given limit.

    Args:
        bmi: A list of BMI values (int or float).
        limit: An integer limit.

    Returns:
        A list of booleans, True if BMI is above the limit, False otherwise.
    """

    if not validate_int_float(bmi):
        raise ValueError("All elements in BMI must be integers or floats.")
    return [x > limit for x in bmi]


# def main():
#     try:
#         height = [2.71, 1.15]
#         weight = [165.3, 38.4]
#         bmi = give_bmi(height, weight)
#         print(bmi, type(bmi))
#         print(apply_limit(bmi, 26))
#     except ValueError as e:
#         print(ValueError.__name__ + ":", e)


# if __name__ == "__main__":
#     main()
