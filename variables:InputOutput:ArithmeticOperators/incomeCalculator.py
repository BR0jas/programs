#Word Problem 4
#Calculate Monthly Salary

#Input:
hours = int(input("enter number of working hours per day"))
perHour = float(input("enter hourly wage"))
days = int(input("enter number of working days in a month"))
taxRate = float(input("enter the income tax rate"))

#Calculations:
totalHours = hours*days
gross = totalHours*perHour
incomeTax = gross*(taxRate/100)
payCheck = gross - incomeTax

if hours==0:
    print("get off your ass you bumm") 

#Output:
print("Your monthly paycheck is", format(payCheck, '.2f'))
print("dolla dolla bills yall")
