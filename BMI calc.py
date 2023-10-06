# Maina Maurice Macharia
# SCT211-0010/2022

def main():
    weight=float(input("Enter weight in (kgs): "))
    height=float(input("Enter height in (M): "))
    BMI_check(weight,height)
    
    
def BMI_check(weight,height):
    normal_BMI1=18.5
    normal_BMI2=24.9
    my_BMI=weight/pow(height,2)
    
    if my_BMI<normal_BMI1:
        print("Underweight!")
        
    elif normal_BMI1<=my_BMI<=normal_BMI2:
        print("Normal weight")
    
    else:
        print("Overweight")
        
        
main()
