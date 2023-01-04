#!/usr/bin/env python3
import random
'''
StephanieCobble | Lab 31
-Append int 4 to the wordbank list
-Include an input asking for a number between 0 and 20. Save this as the variable num.
-Use the integer num to slice one of the elements from the list tlgstudents. Save the name you return as the variable student_name.
-Using elements from the tlgstudents list and the student_name string, print this output: 
    <student_name> always uses <4> <spaces> to indent.
'''


wordbank= ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

num = int(input("Please choose a number between 0 and 20. "))

student_name = tlgstudents[num]

print(f'{student_name} always uses {wordbank[2]} {wordbank[1]} to indent')


'''
Bonus 1

Find a way to randomize what student name is picked. HINT: There is a function for this; don't be afraid to look for answers on the docs page!

Bonus 2

The list of TLG students for the course is consistently changing. Class sizes can expand or diminish with each teaching (although the expectation is that classes will grow!). 
Set the num variable to account for changing list lengths, without having to manually recode the list range. 
Finally, code the input() to allow the user to type a number beginning from 1 (users don't like to think about zero-indexing). Hint - Check the Python built-in functions.
'''
# Bonus 1
rand_num = random.randint(0,20)

student_name2 = tlgstudents[rand_num]

print(f'{student_name2} always uses {wordbank[2]} {wordbank[1]} to indent')

# Bonus 2
arr_length = len(tlgstudents)
print(f'Length of tlgstudents is {arr_length}')
user_num = int(input(f'Please choose a number between 1 and {arr_length}. '))
student_name3 = tlgstudents[user_num - 1]
print(f'student name 3: {student_name3}')
print(f'{student_name3} always uses {wordbank[2]} {wordbank[1]} to indent')

