#!/usr/bin/env python3
'''
StephanieCobble | Lab 57 - Import Modules
-Create a script that includes the trivia dictionary below.
-Slice and print out the trivia question and the four answers (one correct, three incorrect) from the dictionary.
-Use the html library to render the question/answers in the proper format.
-BONUS: have the user answer A, B, C, or D and see if they guess the answer correctly!
'''

import html

def main():

    
    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

    trivia_q = trivia["question"]
    correct = html.unescape(trivia["correct_answer"])
    incorrect1 = html.unescape(trivia["incorrect_answers"][0])
    incorrect2 = html.unescape(trivia["incorrect_answers"][1])
    incorrect3 = html.unescape(trivia["incorrect_answers"][2])
    
    print(f'{trivia_q}')
    print(f'Here are your answer options: \n a  {correct} \n b  {incorrect1} \n c  {incorrect2} \n d  {incorrect3}')

    answer = " "
    counter = 0
    while counter < 3 and answer != "a":
        counter += 1 # adds 1 to the counter for each wrong answer. At 3, the answer will print
        answer = input(f'Choose the correct answer: ').lower()  # lowercase the user input
        if answer == "a":
            print(f'Correct! The quote is: {correct}')
        elif counter == 3: # at 3 rounds, answer will print
            print(f'Sorry. the answer we\'re looking for was a: {correct}')
        else: # keeps going until counter hits 3 or user gets the answer correct 
            print('Sorry, that\'s incorrect!')
        



if __name__ == "__main__":
    main()
