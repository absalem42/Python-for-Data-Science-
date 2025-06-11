import sys
from ft_filter import ft_filter


def process_input(args: list[str]) -> tuple[str, int]:
    """
    Validates and processes the input arguments.

    Args:
        args (list[str]): Command-line arguments.

    Returns:
        tuple[str, int]: A tuple containing the string and integer arguments.

    Raises:
        AssertionError: If the number of arguments is not 2
        or if the arguments are of the wrong type.
    """

    if len(args) != 3:
        raise AssertionError("the arguments are bad")

    if not isinstance(args[1], str):
        raise AssertionError("the arguments are bad")

    try:
        second_arg = int(args[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    return args[1], second_arg


def main(args: list[str]) -> None:
    """
    Processes input arguments, filters words based on their length,
     and prints the result.

    Args:
        args (list[str]): Command-line arguments
         [script_name, string_arg, length_arg].
    """
    try:
        string_arg, length_arg = process_input(args)
        words = string_arg.split()
        filtered_words = list(word for word in ft_filter(lambda w: len(w) > length_arg, words))
        print(filtered_words)
    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)


if __name__ == "__main__":
    main(sys.argv)
