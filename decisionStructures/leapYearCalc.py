#Exercise 2 Problem 8
#Determine whether the year entered is a leap year

#Input:
year=int(input("enter a year"))

#Calculations & Output:
if(year>0):
    if(year<1582):
        print(year, "is not a leap year, it is before 1582")
    elif(((year%4==0)and(year%100!=0)or(year%400==0))):
        print(year,"is a Leap Year")
    else:
        print(year, "is not a Leap Year")
else:
    print("invalid input entered yo")
    

