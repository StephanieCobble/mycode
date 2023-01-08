#!/usr/bin/env python3
'''
StephanieCobble | Lab 44 - testing with if
'''
# collect user input 
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## Use str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("The hostname matches expected config")

print("Exiting the script")
