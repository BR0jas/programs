#Exercise 3 problem 5

#one 3 digit positive integer
#integer's digits calculated and printed on separate lines

#Input:
print("enter a number 100-999")
num = int(input("enter positive 3-digit number"))

#preserves the original input value
saveNum = num

#Calculations:
lastDigit = num%10
num//=10

#original value will be divided by 10
#and the new result will OVERWRITE the original value
#after this step num has only TWO digits

middleDigit = num%10
num//=10
#after this step num has only ONE digit left

firstDigit = num

sum = lastDigit+middleDigit+firstDigit

#Output:
print("the digits of", saveNum, "are:")
print(firstDigit)
print(middleDigit)
print(lastDigit)
print("the sum of the digits in", saveNum, "is:", sum)

#pay attention:
#at the end of the program the value of variable num differs
#from its original input value since we modified num through the
#program, but the value of variable saveNum remains the same and
#keeps the original input value
