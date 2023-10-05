bill_Amount=float(input("Enter Total Bill Amount: "))

def display_Percentages():
    print("1. 10%")
    print("2. 12%")
    print("3. 15%")
while True:
    display_Percentages()
    percentage=0
    choice=int(input("Chose percentage: "))
    if choice==1:
        percentage=10
        break
    elif choice==2:
        percentage=12
        break
    elif choice==3:
        percentage=15
        break
    else:
        print("Enter correct values!!")
    

total_Amout=bill_Amount*percentage/100

number_of_People=int(input("Enter number of people splitting the bill: "))

amout_paid_by_Each=total_Amout/number_of_People

print("Amout paid by each person = ",format(amout_paid_by_Each,'.2f'))