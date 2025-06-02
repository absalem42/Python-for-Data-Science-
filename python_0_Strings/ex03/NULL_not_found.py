def NULL_not_found(object: any) -> int:
    if object is None:
        
         


if isinstance(object, list):
        print(f"List : {type(object)}$")


def main():
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))


if __name__ == "___main__":
    main()