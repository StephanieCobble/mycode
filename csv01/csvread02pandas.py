#!/usr/bin/python3
"""
Alta3 Research | RZFeeser@alta3.com
Exploring pandas dataframes
"""

import pandas

def main():

    #create a dataframe called superdf from our csv data
    superdf = pandas.read_csv("superbirthday.csv")

    # display the column names
    print(f"Column names are {', '.join(superdf)}")

    # uncomment the line below if you need to see what we are looping across
    # orient = 'records' prevents to_dict() from using the index value
    #print(superdf.to_dict(orient='records'))

    for row in superdf.to_dict(orient='records'):
        print(f"\t{row['name']} aka {row['heroname']}, was born in {row['birthday month']}.")

    # print the total number of lines (span returns (lines, columns))
    print(f"Total lines processed {superdf.shape[0]}")

    ## remove heroname and print to new regular birthday file
    superdf.pop('heroname')
    superdf.to_csv('/home/student/mycode/csv01/regularbirthday.csv')


if __name__ == "__main__":
    main()

