#!/usr/bin/env python3

'''
StephanieCobble | Lab 61 - range() practice 
-Write a script that will output ALL 99 LINES of the song 99 Bottles of Beer on the Wall! If you're unfamiliar with the song, here's what the output would look like:
HINT: you will need to use range() as well as a for loop to pull this off.
EXTRA CREDIT 01: include an input() in your script that allows the user to dictate how many bottles of beer you're counting down from!
EXTRA CREDIT 02: don't let the user count down from more than 100 bottles of beer.
'''

import time

def main():
    # counter = 100
    counter = int(input("How many bottles would you like to start with? \nChoose a number between 1 and 100.\n "))
    while counter >= 0:
        if counter <= 100:
            # counter -= 1
            for count in range(counter, 0, -1):
                print(f'{count} bottles of beer on the wall!')
                print(f'{count} bottles of beer on the wall! {count} bottles of beer! Take one down, pass it around!')
                time.sleep(1)
        
        else:
            print("Please enter a number between 1 and 100")
            main()
        break

if __name__ == "__main__":
    main()
