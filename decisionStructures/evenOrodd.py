#Exercise 2 Problem 1 (Version1)
#is the input Even/Odd

#Input:
num = int(input("enter integer"))

#Calculations & Output:
if(num % 2 == 0):
    print(num, "is even")

else:
    print(num, "is odd")


#Version2

#Input:

num = int(input("enter integer"))

#Calculations & Output:
if(not(num % 2)):
   print(num, "is even")

else:
    print(num ,"is odd")

