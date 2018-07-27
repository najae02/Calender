gwc = 10
print("Let's do a countdown!")
while(gwc > -1):
    if(gwc == 0):
        print("Blast off!")
    else:
        print(str(gwc) +"...")

        gwc -= 1

print(" ")
print("Now let's count random stuff")

for i in range(10):
    print("Number: " + str(i))
