from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capital(string):
    return string.upper()


print(list(map(capital, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()


print(list(zip(my_strings, my_numbers)))

scores = [73, 20, 65, 19, 76, 100, 88]


def scores_over_50(scr):
    return scr > 50


print(list(filter(scores_over_50, scores)))


def acculator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(acculator, (my_numbers + scores)))
