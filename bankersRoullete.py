import random

print("Welcome to BankersRoullete")
name=input("enter all the name separated by commas(,):")

#we can change the string to list with the help of split function 
nameList=name.split(",")

rNum=random.randint(0,len(nameList))
# print(rNum)
# print(nameList)
# print(len(nameList))

print(f"{nameList[rNum]} will pay all the bill today.")