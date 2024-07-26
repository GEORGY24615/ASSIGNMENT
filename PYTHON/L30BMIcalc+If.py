weight=float(input("Enter your weight in kg"))
height=float(input("Enter your height in metres"))
BMI=round(weight)/(height**2)
print(f"YOUR BMI IS {BMI}")
if BMI<18.5:
    print("you are underweight")
elif BMI <25:
    print("you are normal weight")
elif BMI <30:
    print("you are overweight")
elif BMI <35:
    print("you are obese")
elif BMI >35:
    print("You are clinically Obese")
 