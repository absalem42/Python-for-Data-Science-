

ft_list = ["Hello", "tata!"]  # mutable
ft_tuple = ("Hello", "toto!")  # immutable, unordered
ft_set = {"Hello", "tutu!"}  # mutable and cannot have the same element
ft_dict = {"Hello": "titi!"}  # mutable


ft_list[1] = "World!"
change_t = list(ft_tuple)
change_t[1] = "UAE!"
ft_tuple = tuple(change_t)
ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")
ft_dict["Hello"] = "42Abu Dhabi!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
