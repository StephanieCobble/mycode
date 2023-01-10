#!/usr/bin/python3

"""
StephanieCobble
Lab 81 - Pandas Dataframes w/ Excel, csv, json, HTML, & beyond
"""

import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    # display first 5 entries of the ciscocsv dataframe
    print(ciscocsv.head())

    # display first 5 entries of the ciscojson dataframe            
    print(ciscojson.head())

    ciscodf = pd.concat([ciscocsv, ciscojson])
    # uncomment the line below to "fix" the index issue
    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    print(ciscodf)

if __name__ == "__main__":
    main()

