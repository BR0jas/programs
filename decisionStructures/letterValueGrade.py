#Exercise 2 Problem
#Calculate the letter value of the grade recieved

#Input:
grade=int(input("enter the grade you received"))

#Calculations & Output:
if(grade>=0 and grade<=100):
    if(grade>=90):
        print(grade,"is an A")
    elif(grade>=80):
        print(grade,"is a B")
    elif(grade>=70):
        print(grade,"is a C")
    elif(grade>=60):
        print(grade,"is a D")
    else:
        print(grade,"is an F, you failed, you are a failer.")

else:
    print("invalid grade input yo")
    
