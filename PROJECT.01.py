#PYTHON NUMBER GUESSING GAME
import random


import  random
guesses=0
max_value=90
min_value=30
is_running= True
answer=random.randint(min_value,max_value)

print("Python Number Guessimg Game")
print(f"Select a number between{min_value} and {max_value}")
while is_running:
    guess=input("enter your number: ")
    if guess.isdigit():
        guess= int(guess)
        guesses+= 1
        if guess < min_value or guess > max_value:
            print("the number is out of range")
            print(f"please select a number between {min_value} and {max_value} ")
        elif guess < answer:
            print("WRONG! try again with a more larger number")
        elif guess > answer:
            print("WRONG!try again with a more smaller number")
        else:
            print(f"CORRECT! the answer is {answer}")
            print(f"the number of gusses is {guesses}")
            is_running=False
    else:
        print("INVALID GUESS")
        print(f"please select a number between {min_value} and {max_value}")






















