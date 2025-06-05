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
