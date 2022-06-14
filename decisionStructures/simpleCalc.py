#Exercise 2 Problem 11
#A simple Calculator that reads 2 integers and operator, and performs operation
#Division by Zero not allowed

#Input:
operator=input("Enter Operator ")
num1=int(input("Enter the first operand "))
num2=int(input("Enter the second operand "))

#Calculations & Output:

if(operator=='+'):
    print(num1, operator, num2, "=", num1+num2)
elif(operator=='-'):
    print(num1, operator, num2, "=", num1-num2)
elif(operator=='*'):
    print(num1, operator, num2, "=", num1*num2)
elif(operator=='/'):
    if(num2!=0):
          print(num1, operator, num2, "=", num1/num2)
    else:
        print("ERROR: division by zero is not allowed here")
elif(operator=='%'):
    if(num2!=0):
        print(num1, operator, num2, "=", num1%num2)
    else:
        print("ERROR: division by zero is not allowed here")
else:
    print("ERROR, that is not an Operator here")

    
