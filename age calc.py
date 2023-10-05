import datetime

current_date = datetime.date.today()

birth_year = int(input("Enter your birth year: "))

age = current_date.year - birth_year

if current_date.month < birth_year:
    age -= 1

birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

birthdate_this_year = datetime.date(current_date.year, birth_month, birth_day)

age_days = (current_date - birthdate_this_year).days

age_months = age_days // 30
age_days %= 30

print(f"You are {age} years, {age_months} months, and {age_days} days old.")
