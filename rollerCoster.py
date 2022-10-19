import string


height=int(input("Enter your height in cm:"))
bill=0
# now adding a feature to take user input whether they want to take photo or not 
if height>=150:
    print("You can ride rollercoster!!!!")
    age=int(input("Enter your age:"))
    if age<12:
        bill=20
        print("Ticket price for kids: 20$")
    elif age<=18:
        bill=50
        print("Ticket price for Young:  50$")
    else:
        bill=70
        print("Ticket price for elders: 70$")

    takePhoto=input("Do you want to take a photo?(cost:10$) type y for yes and n for no:")
    if (takePhoto.lower()=="y"):
        bill+=10

    print(f"total amount to be paid:{bill}$")        #return outside of the if block because if a person dont want to take photo still we need to print the value of bill.
else:
    print("You are too short to ride the rollercoster...")
