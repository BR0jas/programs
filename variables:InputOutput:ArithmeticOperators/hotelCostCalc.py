#Word Problem 1
#Calculate the total cost of a hotel stay

#Input:
nights = int(input("enter number of nights in the hotel"))
price = float(input("enter price per night"))
tax = float(input("enter tax percent"))

#Calculations:
full_one_night = price+price*tax/100
total = nights*full_one_night

#Output:
print("the total cost of your stay will be", format(total, ".2f"))
