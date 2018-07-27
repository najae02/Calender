#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 5)
# For Testing: print(aRandomNumber)

i = 0
for i in range(3):
	tries = str(i)
	print(tries)
	guess = input("Guess a number between 1 and 5:")
	if(aRandomNumber > 5):
		print("Try Again")
		continue
	if(aRandomNumber < 1):
		print("Try Again")
		continue
	else:
		print(str(aRandomNumber))
		print("You did it!")
		break
print("Game Over")
