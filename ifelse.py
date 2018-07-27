print("Let's see how well you know me")

print("\nNow let's try it using while True and break instead of a variable")
while True:
    name = input("What is my name?: ")
    if(name == "Najae"):
        print("yess das meee")
    age = input("What is my age?: ")
    newAge = int(age)
    if(age == "15"):
        print("correct")
    else:
        print("You don't get to play anymore")
        print("Im done, bye (sadly exists game)")
        break
