# Maina Maurice Macharia
# SCT211-0010/2022

def main():
    year=int(input("Enter year: "))
    leap_year_check(year)
    
    
def leap_year_check(year):
    if (year%4==0 and year%100!=0 or year%400==0):
        print(f"{year}, is leap")
    
    else:
        print(f"{year}, is not leap")
        

main()
