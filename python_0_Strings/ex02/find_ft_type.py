



# def all_thing_is_obj(object: any) -> int:
#     print(type(object))
#     return 42


def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f"List : {type(object)}$")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}$")
    elif isinstance(object, set):
        print(f"Set : {type(object)}$")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}$")
    elif object == "Brian":
        print(f"Brian is in the kitchen : {type(object)}$")
    elif object == "Toto":
        print(f"Toto is in the kitchen : {type(object)}$")
    else:
        print("Type not found$")
    return 42




# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Toto")
# print(all_thing_is_obj(10))