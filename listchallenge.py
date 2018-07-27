#imports the ability to get a random number (we will learn more about this later!)
from random import *
print("Welcome to Jae's Cafe")

#Create the list of words you want to choose from.
sides = ["French Fries", "Broccoli", "Mac and Cheese", "Mashed Potatos"]
mains = ["Steak", "Baked Chicken", "Lobster", "Salmon"]
desserts = ["Cheesecake", "Ice Cream", "Pie", "Cake"]

variable = input("Pick a number 0-4")
variable = int(variable)
print(sides[variable])

variable = input("Pick a number 0-4")
variable = int(variable)
print(mains[variable])

variable = input("Pick a number 0-4")
variable = int(variable)
print(desserts[variable])
#Generates a random integer.
# aRandomIndex = (len(sides))
# print("First: ", sides)
# print("Second: ", mains)
# print("Third: ", dessert)
# print(str(aRandomIndex))
