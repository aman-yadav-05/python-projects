import random

print("Welcome to Rock-Paper-Scissors game")
player = input("Enter Your name:\n")
user_choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors:\n"))

if(user_choice == 0):
    print("you chose: rock")
elif(user_choice == 1):
    print("you chose: paper")
else:
    print("you chose: scissors")

# generating random no. between 0 and 2
randChoice = random.randint(0, 2)

if(randChoice == 0):
    print("computer chose: rock")
elif(randChoice == 1):
    print("computer chose: paper")
else:
    print("computer chose: scissors")

if(randChoice == 0):
    if(user_choice == 0):
        print("you both chose rock, it's a tie.🤝")
    elif(user_choice == 1):
        print(f"paper captured rock, {player} won 🎉")
    else:
        print(f"rock smashed scissors, {player} lose 👎")
elif(randChoice == 1):
    if(user_choice == 0):
        print(f"paper captured rock, {player} lose 👎")
    elif(user_choice == 1):
        print("you both chose paper, it's a tie.🤝")
    else:
        print(f"scissors cut paper into pieces, {player} won 🎉")
else:
    if(user_choice == 0):
        print(f"rock smashed scissors, {player} won 🎉")
    elif(user_choice == 1):
        print(f"scissors cut paper into pieces, {player} lose 👎")
    else:
        print("you both chose scissors, it's a tie.🤝")

print("____E__N__D____")
