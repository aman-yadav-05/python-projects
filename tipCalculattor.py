print("!!Welcome to tip Calculator!!")
print()
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip will you like to give? 10,12 or 15? "))

calTip = bill*(tip/100)
bill += calTip

print(f"Bill amount:{bill}")

people=int(input("How many people to split the bill?"))
each = round(bill/people,2)

print(f"Each person should pay:${each}")
