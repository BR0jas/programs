#Word Problem 5
#Calculate Final Grade

#Declaration of Constant Variables
final = 90
homework = 10

#Input:
final_exam = int(input("enter final exam grade"))
homework_assignments = int(input("enter homework grade"))

#Calculations:
finalGrade = final_exam*(final/100)+homework_assignments*(homework/100)

#Output:
print("the final grade is", int(finalGrade+0.5))

