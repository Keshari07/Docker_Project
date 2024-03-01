import random
import os
#RussianRoulettegame

number =random.randint(1,10)
guess = input("Guess a number between 1 and 10")
guess = int(guess)

if guess == number:
 print("You Won !!")
os.remove("")
