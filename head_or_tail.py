import random
rand=random.randint(0,1)
# print(rand)

choice=input("Choose your side of coin (heads or tails):").lower()
print(f"your chose {choice}")

if(rand==0):
    print(rand)
    if(choice=="tails"):
        print("you won")
    else:
        print("you lose")
else:
    print(rand)
    if(choice=="heads"):
        print("you won")
    else:
        print("you lose")