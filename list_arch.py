from copy import deepcopy

a = ["a", "b", "c"]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ["a", "b", ["A", "B", [1, 2, 300], "C"], "c"]]
# print("Id of list lst", id(lst))

list_copy = deepcopy(lst)


lst[10][2][2][2] = 3

# print(list_copy, id(list_copy))

print("lst", lst, id(lst))
print("list_copy", list_copy, id(list_copy))
