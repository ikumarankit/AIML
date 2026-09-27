# Dictionary :- key : value pairs
# keys are always unique 

# dict_name = {
#     key1_name : value, 
#     key2_name : value
# }

# we can also use integer value or any other data type as key 
info = {
    "name": "Ankit",
    "cgpa": 7.5,
    "subjects": ["math", "science"],
    3.14: "PI"
}

print(info)
print(type(info))


# Access any key value 
print(info["name"])
print(info[3.14])


# Dictionary is by default mutable in python and unorder(because there is no index rule in dictionary unlike list, tuple and strings)
info["cgpa"] = 8.0
print(info["cgpa"])




# Dictionary methods 
# d.keys()   # returns all keys 
print(info.keys())
dict_keys = info.keys()
print(dict_keys)
print(type(dict_keys))   # dict_keys

# we can also convert it into list 
dictionary_keys = list(info.keys())
print(dictionary_keys)
print(type(dictionary_keys))   # list 



# d.values()   # returns all values 
print(info.values())
dict_values = info.values()
print(dict_values)
print(type(dict_values))   # dict_keys

# we can also convert it into list 
dictionary_values = list(info.values())
print(dictionary_values)
print(type(dictionary_values))   # list 



# d.items()   # returns (key, val) pairs
print(info.items())



# d.get(val)  # returns val according to key
# dict[key]  -> value (if the key does not exist it gives error)
# dict.get(key) -> value (if the key does not exist it gives none)

print(info.get("cgpa"))
# print(info["cgpa2"])   # this gives key error 
print(info.get("cgpa2"))  # gives none(none is type of data which we learn previously)



# d.update(new_item)  # adds new item to dictionary
info.update({
    "city": "Delhi"
})

print(info)


