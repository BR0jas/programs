#Word Problem 3
#Loan Calculator

#Declaration of the constant variable

months = 12

#Input:
loan = float(input("enter initial loan amount"))
interest = float(input("enter interest rate"))
loan_term = int(input("enter the loan term in years"))

#Calculations:
total_own = loan*(1+interest/100)
monthly_payment = total_own/(loan_term*months)

#Output:
print("monthly payment is:", format(monthly_payment, '.2f'))
