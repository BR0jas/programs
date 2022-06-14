#Exercise 2 Problem 13
#3 integers stored in a Month,Day,Year format, program increments to next date

#Input:
month=int(input("Enter Month's Numeric Value "))
day= int(input("Enter Day Numeric Value "))
year=int(input("Enter the Year Numeric Value "))

#Calculations & Output:

#flag variable
input_valid=True
if(year>0 and month>=1 and month<=12):
    if(month==2):
            if(year<1582):
                days_in_month=28
            elif(year%4==0) and (year%100!=0):
                days_in_month=29
            elif(year%400==0):
                days_in_month=29
            else:
                days_in_month=28
    elif(month%2!=0 and month<=7):
        days_in_month=31
    elif(month%2==0 and month>=8):
        days_in_month=31
    else:
        days_in_month=30
else:
    input_valid=False #invalid month or/and year
if(input_valid):
    if(day==days_in_month):
        day=1
        if(month==12):
            month=1
            year+=1
        else:
            month+=1
    else:
        if((day>=1)and(day<days_in_month)):
            day+=1
        else:
            input_valid=False #invalid day
if(input_valid):
    print("The Next Day is: ",month,day,year)
else:
    print("Invalid Input for Date")
    
                
                
