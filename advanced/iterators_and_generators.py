# iterators = list, string, tuple, set, frozenset, dictionary
from time import perf_counter


def get_range_fun(num) -> list:
    return range(num)


def get_range_gen(num):
    for i in range(num):
        yield i


a = get_range_gen(1000000000000000)


start = perf_counter()

for _ in range(10):
    next(a)
# get_range_fun(100000)


end = perf_counter()

print(f"Total execution took {end-start}")
