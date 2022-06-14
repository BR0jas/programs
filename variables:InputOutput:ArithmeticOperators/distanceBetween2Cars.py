#In this function we are using fabs() function from MATH LIBRARY *(IMPORT MATH)* 
#Calculate the distance between 2 cars

#Input:
speed1 = float(input("enter the speed of the first car"))
speed2 = float(input("enter the speed of the second car"))
start_distance = float(input("enter the starting distance between the cars"))
time = float(input("enter the travel time"))

#Calculations:
final_distance = math.fabs(start_distance-time*(speed1+speed2))

#Output:
print("the final distance is", final_distance)




