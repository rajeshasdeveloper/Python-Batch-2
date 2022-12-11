# map, filter, reduce
from functools import reduce


# square = list(map(lambda x, y: x * y, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
# # print(square)

# is_divisible_by_two = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

# # print(is_divisible_by_two)

# reduce_list = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print(reduce_list)


def get_user_var():

    u_input = input("Enter the numbers: ")

    parsed_input = list(map(int, list(u_input)))
    return parsed_input
