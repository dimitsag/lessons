# Error Handling
while True:
    try:
        age = int(input("what is your age?: "))
        10 / age
        print(f"you are {age} years old!")
    except ValueError:
        print("please try a number")
    except ZeroDivisionError:
        print("please enter a number higher than 0 ")
    else:
        print("thanks dude")
        break
    finally:    # it always runs at the end of the loop after every try
        print("ok i am finally done")


def summary(num1, num2):
    try:
        return num1 + num2
    except TypeError as error:
        print(f"please enter a number {error}")


print(summary(1, 2))
