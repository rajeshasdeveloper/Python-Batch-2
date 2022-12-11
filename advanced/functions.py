# args, kwargs
from lambda_fun import get_user_var


def addition(*args):
    if type(args[0]) == list:
        return sum(args[0])
    return sum(args)


def dic_calc(**kwargs):
    print(kwargs)


print(get_user_var())
