#Exercise 2 Problem 12
#Ask for 9 digit integer(BarCode) program determines whether item is perishable

#Input:
barcode=int(input("Enter a 9 digit positive integer "))

#Calculations & Output:
if (barcode>=100000000 and barcode<=999999999):
    last_digit=barcode%10
    #checks condition and outputs result
    if last_digit==3 or last_digit==4 or last_digit==7:
        print("That item is Perishable")
    else:
        print("That item is Non-Perishable")
else:
    print("Invalid Input for 9 digit Positive Integer")
    
