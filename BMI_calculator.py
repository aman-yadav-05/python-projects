height = float(input("Enter your height in m(meter):"))
# print(type(height))
weight = float(input("Enter your weight in kg(kilogram):"))
# print(type(weight))
bmi=int(weight/(height**2))
# print(int(weight/(height**2)))

if(bmi<=18.5):
    print(f"Your BMI is {bmi}, you are underweight")
elif(bmi>18.5 and bmi<=25):
    print(f"Your BMI is {bmi}, you are normal")
elif(bmi>25 and bmi<=30):
    print(f"Your BMI is {bmi}, you are slightly over weight")
elif(bmi>30 and bmi<=35):
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")