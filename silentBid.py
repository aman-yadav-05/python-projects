import os
from time import sleep

# print("hello this is to test the os function")
# sleep(2)
# os.system('cls')
register = {}
flag = True
while flag:
    name = input("What is your name? ")
    bid = int(input("Enter the amount of money you want to bid:$ "))

    register[name] = bid

    # print(register)
    choice = input("Is there any other bidder left? (yes or no) :").lower()

    if choice == "yes":
        # sleep(1)

        print("storing data")
        sleep(1)
        os.system('cls')
    else:
        # flag = False
        highest = 0
        for key in register:
            if(register[key] > highest):
                highest = register[key]
                os.system('cls')
                print(f"{key} is the highest bidder with ${highest}")

        # print(highest)
        flag = False

# print(register)
