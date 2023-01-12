#!/usr/bin/env python3

"""
StephanieCobble | Lab 91 - API Looping;  Practice with API Slicing
"""

import requests
import wget

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi)

    ## Pt 1 - Slicing (No for loop)
    ## Find the "sprites" key. Print the URL to "front_default", which is a link to an image of your Pokemon!
    imgURL = pokeapi["sprites"]["front_default"]
    print(imgURL)

    ## Pt 2 - Slicing WITH a for loop
    ## Look at the "moves" key. It returns a list of dictionaries; each dictionary contains the name of one of the Pokemon's "moves."
    ## Print out the "name"s of ALL the selected Pokemon's "moves".
    for pokemove in pokeapi["moves"]:
        print(f'Poke moves: {pokemove["move"]["name"]}')

    ## Pt 3 - Loop or NOT to loop
    ## Look at the "game_indices" key. This returns a list of dictionaries; each dictionary contains the name of each Pokemon game this character appeared in! (Pokemon Red, Pokemon Black, Pokemon Crystal, etc.
    ## Count up the total number of games this Pokemon character appeared in. You can solve this with a loop or without a loop... your choice!
    ## Print the count of how many games the selected Pokemon has been in!

    counter = 0
    for index in pokeapi["game_indices"]:
        counter += 1
    print(f'This pokemon has been in {counter} games!')

    ## no loop
    print(f"{pokeapi['name']} has appeared in {len(pokeapi['game_indices'])} games!")

    wget.download(imgURL, "/home/student/static/")

main()

