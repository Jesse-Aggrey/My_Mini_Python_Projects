from datetime import date

dob_day = int(input("Birth day? "))
dob_month = int(input("Birth month? "))
dob_year = int(input("Birth year? "))

now = date.today()

age = now.year - dob_year
if now.month < dob_month or (now.month == dob_month and now.day < dob_day):
    age -= 1

print("Your age is", age)