import sys


try:
    if len(sys.argv) == 1:
        exit(0)
    assert len(sys.argv) == 2, "more than one argument is provided"

    assert sys.argv[1].lstrip("-").isdigit(), "argument is not an integer"

    try:
        if int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer")

except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")
