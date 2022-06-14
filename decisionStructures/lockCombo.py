#Exercise 2 Problem 5
#Guess the 3-digit lock combo to the chest that contains 1 million shmeckles
#Rule1=first digit equals last digit
#Rule2=middle digit is odd


#Input:
num=int(input("enter a 3-digit positive integer to open the chest-> "))

#Calculations and Output:
if(num>99 and num<1000):
    #preserve input number
    num_old=num

    #separating digits
    last_digit= num%10
    num=num//10
    mid_digit=num%10
    num=num//10
    first_digit=num%10

    #checking conditions and outputing results
    if((last_digit==first_digit) and (mid_digit%2!=0)):
        print("Yes", num_old, "opens the chest!")
    else:
        print("Nope", num_old, "does not open the chest...")
    #alternative way to write the if condition is:
    #if((last_digit==first_digit) && (mid_digit%2))

else:
    print("invalid combo input")
