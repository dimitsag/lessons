# generate a number 1-10
# input from user
# check that input is a number 1 -10
# check if number is the right guess.
# Otherwise ask again
# import sys
import rand

number = int(random.randint(1, 10))

while True:
    try:
        guess_num = int(input("guess a number from 1 to 10: "))
        if 0 < guess_num < 11:
            if guess_num == number:
                print("spot on, A GREAT GUESS")
                break
            else:
                print("wrong answer try again")
                continue
        else:
            print("a number FROM 1 TO 10 you numnum")
    except ValueError:
        print("please enter a number")
        continue
