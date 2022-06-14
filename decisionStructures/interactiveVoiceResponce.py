#Exercise 2 Problem 14
#Program simulates a simple system that give Menu Options and asks for input

#Declaration of Constant Variables
COST= 199.99

#Input:
print("Main Menu")
print("Press 0 -> Exit")
print("Press 1 -> Tech Support\n\tSub-Menu: 1->TV, 2->Internet, 3->Phone")
print("Press 2 -> Billing")

main_choice=int(input("Enter Main Menu choice "))


#Calculations & Output:
if(main_choice==0):
    print("Goodbye!")
elif(main_choice==1):
    print("You entered 1, Technical Support. Is that correct?")
    confirm=input("Enter 'Y' to Confirm ")
    confirm=confirm.upper()
    if(confirm=='Y'):
        print("Thankyou for confirming you selection")
        print("Enter type of service you need help with")
        second_choice=int(input("1->TV, 2->Internet, 3->Phone "))
        if(second_choice==1):
            print("One moment for 'TV' support...")
        elif(second_choice==2):
            print("One moment for 'Internet' support...")
        elif(second_choice==3):
            print("One moment for 'Phone' supoort...")
        else:
            print("Invalid input for Main Menu Selection..")
    else:
        print("Sorry for misunderstanding, transferring back to the Main Menu")
elif(main_choice==2):
    print("You entered 2, Billing. Is that correct?")
    confirm=input("Enter 'Y' to Confirm ")
    confirm=confirm.upper()
    if(confirm=='Y'):
        print("Thankyou for confirming your selections")
        payment=float(input("Enter Payment Amount "))
        if(payment>0):
            balance=COST-payment
            if(balance==0):
                print("Your payment has been recieved. There is no remaining Balance.")
            else:
                print("Your balance is", balance)
        else:
            print("You entered an Invalid Payment Amount")
    else:
        print("Sorry for misunderstanding, transferring back to the Main Menu")
else:
    print("ERROR Invalid Input for Main Menu Selection")

    

