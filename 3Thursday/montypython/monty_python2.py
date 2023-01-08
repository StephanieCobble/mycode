#!/usr/bin/env python3
'''
StephanieCobble | Lab 46 Using while, if, elif, else (Monty Python)
'''

def main(): 
    round = 0
    while True:
        round = round + 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess: ")
        if answer == 'Brian':
            print("Correct!")
            break
        elif round == 3:
            print("Sorry, the answer was Brian.")
            break
        else: 
            print("Sorry. Try again")



if __name__ == "__main__":
    main()
