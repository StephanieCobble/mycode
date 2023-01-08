#!/usr/bin/python3
'''
StephanieCobble | 1/3/23
Objective: Write a script that contains the following:

An input asking the user's name.

An input asking what day of the week it is.

A print statement that reads:
'''

def main():
    input_name = input('Please enter your name: ')
    input_day = input('Please enter the day of the week: ')

    print(f'Hello, {input_name}! Happy {input_day}!!')

if __name__ == '__main__':
    main()
