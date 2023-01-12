#!/usr/bin/env python3
"""
StephanieCobble | Lab 96 - Challenge - Query Parameters
Trivia Game API Challenge
From: https://opentdb.com/api_config.php
Returning Data From Complex JSON
"""

import requests
import random
import html

URL= "https://opentdb.com/api.php?amount=4&category=20&difficulty=medium"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    # print(data)

    #randnum = random.randint(0,3)

    for trivia in data.get("results"):
        print(html.unescape(trivia.get("question")))
        print(html.unescape(trivia.get("correct_answer")))
        print(html.unescape(trivia.get("incorrect_answers")))
        print()


if __name__ == "__main__":
    main()

