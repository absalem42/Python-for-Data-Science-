import sys


def convert_morse(string: str) -> str:
    """
    convert_morse(string: str) -> str
    takes a string as an argument and
    encodes it into Morse Code
    """
    # Morse Code Dictionary
    NESTED_MORSE = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '/',
    }

    result = []
    try:
        for char in string.upper():
            if char in NESTED_MORSE:
                result.append(NESTED_MORSE[char])
            else:
                raise AssertionError("the arguments are bad")
                sys.exit(1)

        print(' '.join(result))

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


def main():

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

    string = sys.argv[1]

    convert_morse(string)


if __name__ == "__main__":
    main()
