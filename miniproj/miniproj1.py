#!/usr/bin/python3
'''
StephanieCobble | Lab 48 - Mini-Project #1
if logic script
Return unique answers based on the input provided... multiple results should be possible.
AS BEST YOU'RE ABLE, control for user errors (suggested: methods, try/except, while loop)
Use at least one while loop.
Make all code "your own."
ROUGH minimum of 40 lines of code... if code is spread out across multiple files, they are cumulative.
'''

import random
import time

def main():

    horror = ["Friday the 13th", "It", "Halloween"]
    action = ["Die Hard", "Ip Man", "300"]
    drama = ["The Shawshank Redemption", "La La Land", "tick, tick, BOOM!"]
    superhero = ["Black Panther", "Deadpool", "Spider-man: Far From Home"]
    comedy = ["Free Guy", "21 Jump Street", "The Princess Bride"]

    user_genre = input(
        f'Welcome to Movie Picker! Enter a genre so we can choose a movie for you.\n\
            Your options are: horror, action, drama, superhero, and comedy. \n').lower()
    # user_genre = user_genre.lower()

    while user_genre != "horror" and user_genre != "action" and user_genre != "drama" and user_genre != "superhero" and user_genre != "comedy":
        main()
        break
    
    if user_genre == "horror":
        print(f'You picked {user_genre}. We\'ve selected {random.choice(horror)} for you!')
        time.sleep(1)
        user_conf = input(f'Do you want to select this movie? Press y for yes or n for a new movie \n').lower()
        if user_conf == 'n':
            print(f'Let\'s try again. We\'ve selected {random.choice(horror)} for you!')
        elif user_conf == 'y':
            print("Great choice!")
    
    elif user_genre == "action":
        print(f'You picked {user_genre}. We\'ve selected {random.choice(action)} for you!')
        time.sleep(1)
        user_conf = input(f'Do you want to select this movie? Press y for yes or n for a new movie \n').lower()
        if user_conf == 'n':
            print(f'Let\'s try again. We\'ve selected {random.choice(action)} for you!')
        elif user_conf == 'y':
            print("Great choice!")
    
    elif user_genre == "drama":
        print(f'You picked {user_genre}. We\'ve selected {random.choice(drama)} for you!')
        time.sleep(1)
        user_conf = input(f'Do you want to select this movie? Press y for yes or n for a new movie \n').lower()
        if user_conf == 'n':
            print(f'Let\'s try again. We\'ve selected {random.choice(drama)} for you!')
        elif user_conf == 'y':
            print("Great choice!")
    
    elif user_genre == "superhero":
        print(f'You picked {user_genre}. We\'ve selected {random.choice(superhero)} for you!')
        time.sleep(1)
        user_conf = input(f'Do you want to select this movie? Press y for yes or n for a new movie \n').lower()
        if user_conf == 'n':
            print(f'Let\'s try again. We\'ve selected {random.choice(superhero)} for you!')
        elif user_conf == 'y':
            print("Great choice!")
    
    elif user_genre == "comedy":
        print(f'You picked {user_genre}. We\'ve selected {random.choice(comedy)} for you!')
        time.sleep(1)
        user_conf = input(f'Do you want to select this movie? Press y for yes or n for a new movie \n').lower()
        if user_conf == 'n':
            print(f'Let\'s try again. We\'ve selected {random.choice(comedy)} for you!')
        elif user_conf == 'y':
            print("Great choice!")

    time.sleep(1)
    print("Grab some popcorn or your favorite snack & enjoy your movie!")


if __name__ == "__main__":
    main()
