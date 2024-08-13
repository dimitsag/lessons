driver_age = int(input("What is your age? "))

if driver_age >= 18:
    print("You are old enough to drive !")
else:
    print("sorry not old enough :(")
    exit()

driver_licence = input("do you have a licence? Answer with yes or no ")

if driver_licence == "yes":
    print("you are able to drive!! ")
else:
    print("you are not able to drive :(")
