#Exercise 2 Problem 2 (Version1)
#Find the MaxValue of 3 integers

#Input:
num1=int(input("enter first integer"))
num2=int(input("enter second integer"))
num3=int(input("enter third integer"))

#Calculations:
#Step1 find the maximum between first two numbers
if(num1>num2):
    max_value=num1
else:
    max_value=num2

#Step2: compare max_value to num3 and update if needed

if(max_value<num3):
    max_value=num3

#Output:
    print("the maximum value of", num1,num2,num3, "is", max_value)


    



