#!/usr/bin/env python3
'''
StephanieCobble | Lab 60 - For loops and range() and with cont
For - Using a file's lines as a source for the for-loop
'''

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # create list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="")

# no need to close our file - closed automatically using 'with'
