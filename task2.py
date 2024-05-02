"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

def title():
    print("Try guess the number in 10 turns")
title()
def game():
    x=int(input("Choose a random number between 1 and 100: "))
    import random
    y=random.randint(1,100)
    z=0
    while x!=y:
        if x>y:
            print("The number is over")
            z+=1
            x=int(input("Choose a random number between 1 and 100: "))
        else:
            print('The number is under')
            z+=1
            x=int(input("Choose a random number between 1 and 100: "))
        if z == 10: 
            print("You have tried 10 times now! :(")
            x=int(input("Choose a random number between 1 and 100: "))
    if x==y:
        print("You got it!")
        z+=1
        print(f"You have tried {z} times in total")
game()