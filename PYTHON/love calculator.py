print("Hi, Welcome to the love calculator")
name1=input("Enter your name\n")
name2=input("Enter your partners name\n")
#combining name1 and name2 
both=name1+name2
#converting the names to lowercase
lowercase_both=both.lower()
#calculating the number of times the letter appear on both names 
t=lowercase_both.count("t")
r=lowercase_both.count("r")
u=lowercase_both.count("u")
e=lowercase_both.count("e")
true=t+r+u+e
l=lowercase_both.count("l")
o=lowercase_both.count("o")
v=lowercase_both.count("v")
e=lowercase_both.count("e")
love=l+o+v+e
#combining the percentage of the string
love_score=str(true)+str(love)
new_love_score=int(love_score)
print(new_love_score)
if new_love_score <10 or new_love_score>90:
    print(f"your score is  {new_love_score} ,your characters blend in together")
elif new_love_score>=40 and new_love_score<=50:
    print(f"your score is  {new_love_score},you are alright together")
else:
    print(f"your score is  {new_love_score}, you are a boring couple")
