import sys


def count_characters(text: str) -> dict[str, int]:
    """
    Count different types of characters in the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing counts of different character types:
            - 'upper_case': Number of uppercase letters.
            - 'lower_case': Number of lowercase letters.
            - 'punctuation': Number of punctuation marks.
            - 'digits': Number of numeric digits.
            - 'space': Number of whitespace characters.
    """

    counts = {
        "upper_case": 0,
        "lower_case": 0,
        "punctuation": 0,
        "digits": 0,
        "space": 0,
    }
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for ch in text:
        if ch.isupper():
            counts["upper_case"] += 1
        elif ch.islower():
            counts["lower_case"] += 1
        elif ch in punctuation_chars:
            counts["punctuation"] += 1
        elif ch.isdigit():
            counts["digits"] += 1
        elif ch.isspace():
            counts["space"] += 1

    return counts


def process_input(input_args: list[str]) -> str:
    """
    Processes command-line arguments or prompts the user for input.

    Args:
        input_args (list): List of command-line arguments.

    Returns:
        str: The text to be processed.

    Raises:
        AssertionError: If more than one argument is provided.
    """

    if len(input_args) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(input_args) == 2:
        return input_args[1]
    else:
        try:
            return input("What is the text to count?\n")
        except EOFError:
            print("\nInput interrupted (Ctrl+D detected). Exiting...")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nInput interrupted (Ctrl+C detected). Exiting...")
            sys.exit(1)


def main(args: list[str]) -> None:
    """
    Processes input text, counts character types, and displays the results.

    Args:
        args (list[str]): Command-line arguments [script_name, optional_text].
    """
    try:
        text = process_input(args)

        counts = count_characters(text)

        print(f"The text contains {len(text)}")
        print(f"{counts['upper_case']} upper letters")
        print(f"{counts['lower_case']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['space']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as er:
        print(AssertionError.__name__, +":", er)


if __name__ == "__main__":
    main(sys.argv)
