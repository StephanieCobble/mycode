#!/usr/bin/python3
"""
Alta3 Research | RZFeeser@alta3.com
StephanieCobble - Lab 80 cont
Challenge Solution 01 - CSV to Excel
"""

import pandas

def main():

    # create a dataframe from csv
    df = pandas.read_csv("5movies.csv")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")

if __name__ == "__main__":
    main()

