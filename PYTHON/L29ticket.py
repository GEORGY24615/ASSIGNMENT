print("welcome to the rollercoaster")
adult_price=int(12)
child_price=int(7)
age=int(input("Enter your age"))
if age<12:
    bill=5
    print("child tickets are $5")
elif age<=18:
    bill=7
    print("youth price is $7")
elif age>=45 and age<=55:
    bill=0
    print("You will have a free ride")    
else:
    bill=12
    print("Adult tickets are 12")  
add_photo=input("would you like a photo? y,n")
if add_photo=="y":
    bill+=2
    print(f"your total bill is {bill}")               