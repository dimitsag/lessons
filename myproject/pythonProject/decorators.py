# decorator
from time import time


def my_decorator(func):
    def wrap_funk(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_funk


@my_decorator
def hello(greeting, emoji="🧔"):
    print(greeting, emoji)


hello("hello there !")

# decorator example


def performance(func):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f"it took {time2-time1} s to run the function")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()

user1 = {
    'name': 'Sorna',
    'valid': True
}

# decorator exercise


def authenticated(fn):
    def wrapped(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            print("invalid user")
    return wrapped


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
