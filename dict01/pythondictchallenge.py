#!/usr/bin/env python3
"""
StephanieCobble | Lab 41
Challenge - Dictionaries
 
"""

def main():
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")
    char_name = char_name.capitalize()
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")
    char_stat = char_stat.lower()

    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
             }

    print(marvelchars.get(char_name).get(char_stat))
    print(f'{char_name}\'s {char_stat} is {marvelchars.get(char_name).get(char_stat)}')

if __name__ == "__main__":
    main()
