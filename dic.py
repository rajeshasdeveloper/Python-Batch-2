dictionary = {"name": "rajesh", "age": 25}

dictionary["skills"] = ["JavaScript", "Python", "ReactJs", "nodeJs"]
dictionary["degree"] = "Masters"
dictionary["exp"] = "3.5 yrs"

# print(dictionary["degree"])
# print(dictionary.get("exp"))

# is_present_flag = dictionary.setdefault("exp", "4 years")

# print(dictionary)

# dictionary["exp"] = "4 years"

# removed_item = dictionary.pop("name")
# removed_item = dictionary.popitem()
# print(removed_item)

print(dictionary)

# print(list(dictionary.keys()))
# print(list(dictionary.values()))

sample_dictionary = {"a": 1, "b": 2}
flag_dictionary = {"exp": "4 years", "b": 4}

dictionary.update(sample_dictionary)
dictionary.update(flag_dictionary)

print(dictionary)
