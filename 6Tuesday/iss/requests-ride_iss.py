#!/usr/bin/python3
"""
StephanieCobble | Lab 90 - Standard vs Third Party Libraries & Open APIs
tracking the iss using
api.open-notify.org/astros.json | Alta3 Research
"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)
    

    ## print the name of the astros and what craft they're on (challenge 1 - lab 90)
    for astros in people:
        print(f'{astros["name"]} is on the {astros["craft"]}')    

if __name__ == "__main__":
    main()

