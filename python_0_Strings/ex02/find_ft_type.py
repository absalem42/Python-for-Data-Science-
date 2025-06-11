def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):  # Check if object is a list
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):  # Check if object is a tuple
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):  # Check if object is a set
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):  # Check if object is a dictionary
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):  # Check if object is the string "Brian"
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found$")
    return 42
