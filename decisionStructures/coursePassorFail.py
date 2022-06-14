#Exercise 2 Problem 4
#Calculate whether a pass or fail in the course

#Declaration of the Constant Variable
pass_grade=60

#Input:
grade=int(input("enter grade recieved"))

#Calculations:
#this program uses a nested if-else structure
if(grade>=0):
    if(grade>=pass_grade):
        print("you passed the course!")
    else:
        print("sorry dummy you failed!")
else:
    print("invalid input breh")



