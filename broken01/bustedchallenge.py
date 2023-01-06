#!/usr/bin/env python3
'''
StephanieCobble | Lab 51 - More Troubleshooting
Code repair challenge 

'''

def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True:
        name= input("What is your name?\n>")
        num= int(input("Pick a number between 1 and 3: "))

        if name and num in words.keys():
            # Hi <name>! Welcome to Day 2 of Python Training!
            print(f'Hi, {name.capitalize()}! Have a {words[num]} day!')
            # print("Hi " + name.capitalize + "! Have a " + words[num] + " day!")
            break
        else:
          print("Come on, follow directions. Try again.")
          continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!
main()