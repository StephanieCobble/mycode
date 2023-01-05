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

def main():
    genres = {"horror": "Friday the 13th", "action":"Die Hard", "drama":"The Shawshank Redemption", "superhero":"Black Panther", "comedy":"Free Guy"}

    user_genre = input(f'Welcome to Movie Picker! Enter a genre so we can choose a movie for you.\nYour options are: horror, action, drama, superhero, and comedy. \n')
    user_genre = user_genre.lower()

    while user_genre != "horror" and user_genre != "action" and user_genre != "drama" and user_genre != "superhero" and user_genre != "comedy":
        main()
        break
    if user_genre == "horror":
        print(f'You picked {user_genre}. We\'ve selected {genres["horror"]} for you!')
    elif user_genre == "action":
        print(f'You picked {user_genre}. We\'ve selected {genres["action"]} for you!')
    elif user_genre == "drama":
        print(f'You picked {user_genre}. We\'ve selected {genres["drama"]} for you!')
    elif user_genre == "superhero":
        print(f'You picked {user_genre}. We\'ve selected {genres["superhero"]} for you!')
    elif user_genre == "comedy":
        print(f'You picked {user_genre}. We\'ve selected {genres["comedy"]} for you!')
    print("Grab some popcorn or your favorite snack & enjoy your movie!")

if __name__ == "__main__":
        main()
