
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.





ft_list = ["Hello", "tata!"] #mutable 
ft_tuple = ("Hello", "toto!") #immutable, unordered 
ft_set = {"Hello", "tutu!"}  #mutable and cannot have the same element, not ouders not indexed 
ft_dict = {"Hello" : "titi!"} #mutable  


ft_list[1]= 'World!'
# ft_tuple = ('Hello', 'France!')
change_t = list(ft_tuple)
change_t[1] = 'France!'
ft_tuple = tuple(change_t)
change_s = {"Hello", "Paris!"}
ft_set = change_s
ft_dict["Hello"] = "42Paris!"



print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)