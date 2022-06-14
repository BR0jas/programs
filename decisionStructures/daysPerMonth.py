#Exercise 2 Problem 10
#find the total days in each month
#using "while" loop to restrict 'character' value (attempted/FAILED)

#Input:
month=int

#Calculations & Output:
while month==int:
    if month!=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12:
        month=int(input("Enter a Months Numeric Value "))
        print("Nice, that month has..")
    else:
        print("That is not a Numeric Value, try again")     
if(month)>=1 and (month)<=12:
    if(month)==2:
        print("Febuary has 28 or 29 days, depending on if it is a Leap Year")
    elif(month)%2!=0 and (month)<=7:
        print("31 Days")
    elif(month)%2==0 and (month)>=8:
        print("31 days")
    else:
        print("30 days")
else:
    print("Invalid input for Numeric Value/Month, try again")
           
