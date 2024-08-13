# Functional Programming
from functools import reduce


def multiply_by2(li):
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list


print(multiply_by2([1, 2, 3]))

# map()
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [100, 200, 300]


def multiply_by2_0(i):
    return i * 2


print(list(map(multiply_by2_0, my_list)))


# filter()

def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

# zip()

print(list(zip(my_list, your_list, their_list)))

# reduce()


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 10))

# lamda works with all the functions above

my_list = [1, 2, 3]
print(list(map(lambda item: item*2, my_list)))
