#Exercise 2 Problem 2 (Version 2)
#this solution could be generalized for any number of inputs

#Input:
num1=int(input("enter first integer"))
num2=int(input("enter second integer"))
num3=int(input("enter third integer"))

#Calculations:

#Step1: assign num1 to max_value - intialization of max_value
max_value=num1

#Step2: compare num2 to current max_value and make change if needed
if(num2>max_value):
    max_value=num2

#Step3: compare num3 to current max_value and make change if needed
if(num3>max_value):
    max_value=num3

#Output:
    print("the maximum among the integers", num1,num2,num3, "is", max_value)
    





