# generators

def generator_func(num):
    for a in range(num):
        yield a*2


for item in generator_func(10):
    print(item)


def generator_func(num):
    for a in range(num):
        yield a


gen = generator_func(10)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
print(next(gen))

# Generators in range loop with classes not necessary to know


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)

# Fibonacci exersice


def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)
