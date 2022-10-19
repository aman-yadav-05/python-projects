print("Welcome to py.pizza!!")
size=input("Enter the size of pizza you want to eat, S for small, M for medium, L for Large:")
price=0
if(size.lower()=="s"):
    price=15
    print(f"Price for small pizza:${price}")
elif(size.lower()=="m"):
    price=20
    print(f"Price for medium pizza:${price}")
else:
    price=25
    print(f"Prize for large pizza:${price}")

pep=input("Do you want to add extra pepperoni? y for yes, n for no.")

if(size.lower()=="s" and pep.lower()=="y"):
    price+=2
    print(f"Extra pepperoni added.Total amount now:${price}")
else:
    price+=3
    print(f"Extra pepperoni added. Total amount now:${price}")

cheese=input("do you want to add extra cheese?y for yes , n for no")

if(cheese.lower()=="y"):
    price+=1
    print(f"Extra cheese added. Your total bill:{price}")
else:
    print(f"Your total bill:{price}")
    
