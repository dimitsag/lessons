import random
def guess_game(guess_num, number):
    if 0 < guess_num < 11:
            if guess_num == number:
                print("spot on, A GREAT GUESS")
                return True
    else:
        print("a number FROM 1 TO 10 you numnum")
        return False


if __name__ == "__main__":
    number = random.randint(1, 10)

    while True:
        try:
            guess_num = int(input("guess a number from 1 to 10: "))
            if guess_game(guess_num, number):
                break
        except ValueError:
            print("please enter a number")
            continue
