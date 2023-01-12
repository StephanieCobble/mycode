#!/usr/bin/python3

"""
StephanieCobble | Lab 95 - APIs & Dev Keys
Challenge 01 - user input for start & end dates
"""

import requests
import pprint
import os

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    # with open("/home/student/nasa.creds", "r") as mycreds:
        # nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    # nasacreds = "api_key=" + nasacreds.strip("\n")
    
    ## Challenge 02 - get key from local shell
    nasacreds = os.getenv("NASAKEY", default="DEMO_KEY")
    nasacreds = "api_key=" + nasacreds

    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## user input start and end dates
    userstart = input("Enter start date as YYYY-MM-DD: ").strip("\n")
    userend = input("Enter end date as YYYY-MM-DD: ").strip("\n")
    startdate = "start_date=" + userstart
    enddate = "end_date=" + userend

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    pprint.pprint(neodata)

if __name__ == "__main__":
    main()

