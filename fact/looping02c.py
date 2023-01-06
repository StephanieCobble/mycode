#!/usr/bin/env python3
'''
StephanieCobble | Lab 60 - For loops and range() and with cont
For - Using a file's lines as a source for the for-loop
'''

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:    # we never created a list of lines to store in memory
        #print and end without a newline
        print(svr, end="")

# no need to close our file - closed automatically
