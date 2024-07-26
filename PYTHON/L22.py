age=input("What is your current age?")
new_age=int(age)
days=365
new_days=int(days)
months=12
new_months=int(months)
weeks=52
new_weeks=int(weeks)
max_age=90
new_max_age=int(max_age)
rem_months=(new_max_age*new_months)-(new_age*new_months)
rem_weeks=(new_max_age*new_weeks)-(new_age*new_weeks)
rem_days=(new_max_age*new_days)-(new_age*new_days)
print(f"your remaining months are {rem_months}, your remaining weeks is{rem_weeks}, your remaining days is {rem_days}" )