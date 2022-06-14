#Word Problem 2
#Calculate the number of Milk Bottles needed to ship in Containers

#Input:
countMilk = int(input("how many milk bottles do we need to ship?"))
perBox = int(input("what is the capacity of each Container?"))

#Calculations:
countBoxes= countMilk // perBox
remain = countMilk % perBox

#Output:
print("the total number of Containers needed will be:", countBoxes)
print("the number of remaining Milk Bottles is:", remain)
print("mmmmm Milk was a bad choice!!")

