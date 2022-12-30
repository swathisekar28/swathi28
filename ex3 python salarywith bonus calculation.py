salary=int(input("enter the salary:"))
print("salary:",salary)
if(salary<1000):
    bonus=salary*(10/100)
    print("bonus:",bonus)
    print("total:",salary+bonus)
else:
    salary>1000
    bonus=salary*(12/100)
    print("bonus:",bonus)
    print("total:",salary+bonus)
    
