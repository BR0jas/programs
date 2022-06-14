#Exercise 2 Problem 3
#Declaration of constant variables
rate_low=1
rate_high=2
threshold=1000

#Input:
deposit= float(input("enter deposit amount"))

#Calculations & Output:
#this program uses a nested if-else structure
if(deposit>0):
    if(deposit<=threshold):

        rate=rate_low
    else:
        rate=rate_high

    total=deposit*(1+rate/100)
    
    print("total is",format(total, ".2f"))
else:
    print("thats a no no, Invalid input")
    


                   
