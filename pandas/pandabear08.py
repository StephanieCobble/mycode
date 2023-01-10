#!/usr/bin/python3
"""
Alta3 Research | RZFeeser@alta3.com
StephanieCobble - Lab 80 cont
Challenge Solution 01 - JSON to Excel
"""

import pandas

def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")

if __name__ == "__main__":
    main()

