#Exercise 2 Problem 7
#Calculate the overseas cost of a credit card purchase

#Input
purchase=float(input("enter the purchase amount"))
foreign_rate=float(input("enter foreign transaction fee rate"))
flat_fee=float(input("enter flat fee"))

#Calculations & Output:
fee=purchase*foreign_rate/100
if(fee<flat_fee):
    total=purchase+flat_fee
    print("foreign transaction fee is", format(fee,".2f"))
    print("since it is less than flat fee")
    print("flat fee is charged")
    print("your total price is", format(total, ".2f"))
else:
    total=purchase+fee
    print("foreign transaction fee is", format(fee,".2f"))
    print("since it is greater than flat fee")
    print("foreign transaction fee is charged")
    print("your total price is", format(total,".2f"))
          
