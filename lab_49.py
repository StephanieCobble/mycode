#!/usr/bin/env python3
'''
StephanieCobble | Lab 49 - Challenge - Number guessing game
Number guessing game! User has 5 chances to guess a number between 1 and 100!
'''

import random


def main():
    num= random.randint(1,100)

    guess = ''
    rounds= 0

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds + 1

        if guess < num:
            print("Too low!")
            rounds + 1

        else:
            print("Correct!")
main()