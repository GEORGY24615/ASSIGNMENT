print("Welcome to python pizza deliveries")
size=input("What Size do you want? S,M,L")
add_pepperoni=input("Would you like an extra pepperoni?  Y,N")
add_cheese=input("Would you like extra cheese? Y,N")
if size=="S":
    if add_pepperoni=="Y":
        if add_cheese=="Y":
         print("Your final bill is $18")
        else:
              print("your final bill is $17")    
    else:
      print("your final bill is $15") 
else:  
 if size=="M":
    if add_pepperoni=="Y":
        if add_cheese=="Y":
         print("your final bill is $24")
        else:
          print("your final bill is $23")
    else:
     print("your final bill is $20") 
 if size=="L":
    if add_pepperoni=="Y":
        if add_cheese=="Y": 
         print("Your final bill is $29")  
        else:
            print("your final price is $28") 
    else:
     print("your final bill is $25")