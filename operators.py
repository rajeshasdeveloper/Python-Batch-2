'''
Arithmetic operators /done
Logical operators /done
membership operators /done
bitwise operators - holding
comparison operators - /done
Identity operators /done
Assignment operators /done
'''

# divisor, dividend, reminder, quotient

# "+, -, *, /, //, %, **"

# a = 10
# print('a location', id(a))
# b = 12

# print(a + b)  # 25
# print(a - b)  # -5
# print(a * b)  # 150
# print(a / b)  # 0.6666 --> Division
# print(a // b)  # 0 --> Floor division
# print(a % b)  # 10 --> Modulo division
# print(a ** b)  # 10 15 --> 0's --> Exponentiation

# print('Overwriting a value from 10 to 15')
# a = a + 5
# c = a
# print('a value = ', a)
# print('a location', id(a))
# print('c value at a is 15 = ', c)
# print('c location at a is 15 ', id(c))
# a = 20
# print('a value = ', a)
# print('a location', id(a))
# c = a
# print('c value at a is 20 = ', c)
# print('c location at a is 20', id(c))


# print(a)

# a = 10

# a = a + 5
# a += 5

# a -= 10 # a = a - 10
# a /= 10
# a *= 5
# a //= 5
# a %= 5
# a **= 2

# & --> 0 & 1 => 0; 1 & 0 => 0; 0 & 0 => 0; 1 & 1 => 1
# | --> 0 | 1 => 1; 1 | 0 => 1; 0 | 0 => 0; 1 | 1 => 1
# ^ --> 0 | 1 => 1; 1 | 0 => 1; 0 | 0 => 0; 1 | 1 => 0
# ~ --> 1 => 0; 0 => 1
# <<
# >>

# Logical Operators

# '''
# and or not
# '''


# print(True and True)
# print(True and False)  # vice versa
# print(True or False)  # vice versa
# print(True or True)
# print(False or False)
# print(not True)
# print(not False)

# print(ord('a'))
# print(ord('A'))
# print(bool(' '))
# print(bool(' '))
# print(bool([]), len([]))
# print(bool([0]), len([0]))

# False, 0, '', None, [], {}  # --> False

# ' ', 'a', 1, '0', 'False', True, 'None', [0], {'key': 'value'}  # --> True

#  Identity opertor

# 'is', 'is not'

# flag = [1, 2]
# counter_flag = [1, 2]

# const_flag = 25
# counter_const_flag = 25
# print(
#     f'\n\nid of flag 25 is {id(const_flag)},id of counter_flag 25 is {id(counter_const_flag)}, {const_flag is counter_const_flag}')
# print(
#     f'\n\nid of array_flag is {id(flag)},id of counter_array_flag is {id(counter_flag)}, {flag is counter_flag}\n\n')

# print(id(flag), id(counter_flag), flag is counter_flag)
# print(flag is not counter_flag)
# if (flag is not counter_flag):
#     counter_flag = flag

# print(id(flag), id(counter_flag), flag is counter_flag)

#  membership operators

# 'in', 'not in
# user_name = 'python is awesome'
# lho = 'python'
# super_array = list(range(11))  # [0,1,2,3, ...  10]
# # print(super_array)
# super_array.append((1, 2, 3))
# # print(super_array)
# sub_array = [1, 2, 3]
# sub_num = 1

# dic = {'name': 'rajeshk', 'age': 777}
# print('name' in dic)  # True
# print('rajeshk' in dic)  # False

# print(lho in user_name)
# print(sub_array in super_array)
# print(sub_num in super_array)

# Comparison operators
# '''
# ==
# !=
# >
# <
# <=
# >=
# '''

# print(1 < 2)
# print(2 < 1)
# print(2 == 2)
# print(2 >= 2)
# print(2 <= 2)
# print(3 <= 2)
# print(2 > 2)
# print(2 < 2)
