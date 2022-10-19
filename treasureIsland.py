print("Welcome to treasure Island")

#we need to create three list and then store them into another list
row1=["📦","📦","📦"]
row2=["📦","📦","📦"]
row3=["📦","📦","📦"]

mat=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}\n")

position=(input("choose the position where you want put treasure:"))

listPosition=position.split()
# print(listPosition)
mat[int(listPosition[0])][int(listPosition[1])]= "x" 
print(f"{row1}\n{row2}\n{row3}\n")
