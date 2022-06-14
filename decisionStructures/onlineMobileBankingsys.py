#Exercise 2 Problem 9
#create an online mobile banking system (MENU)

#Input:
print("Menu: D-deposit, W-withdrawal, T-transfer, E-exit")
choice = input("enter menu choice ")
choice=choice.upper()#input can be entered uppercase or lowercase

#Calculations & Output:

if(choice=='D'):
    print("You have chosen to DEPOSIT")
elif(choice=='W'):
    print("You have chosen to make a WITHDRAWAL")
elif(choice=='T'):
    print("you have chosen to make a TRANSFER")
elif(choice=='E'):
    print("EXIT from the Online/Mobile Banking System")
else:
    print("ERROR: invalid choice")



