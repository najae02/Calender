# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if (user_input == "left"):
    print("You decide to go left and you come across another intersection.")
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if (user_input1 == "left"):
        print("You decide to go left and run into a monster.")
        user_input1 = input()
        if (user_input == "left"):
            print("You choose to go left and you're still stuck with the monster.")
        elif (user_input2 == "right"):
            print("You choose to go right and you go back to the intersection.")
            user_input3 = input()
        elif (user_input3 == "right"):
            print("You decide to go right and come across witch.")
            print("witch:You should go left.")
            print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
            user_input = input()
            if (user_input == "left"):
                    print("You choose to go left and...")
            elif (user_input == "right"):
                    print("You choose to go right and...")

    elif (user_input == "right"):
            print("You choose to go right and you hit a dead end.")
            print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
            user_input = input()
            if (user_input == "left"):
                print("You choose to go left and you go back to the starting point.")
            elif (user_input == "right"):
                print("You choose to go right and you don't go anywhere.")

                        #     # Continue code to finish story.
                        #
                        #
                        #     # Continue code to finish story.
