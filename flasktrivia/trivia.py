'''
Lab 103 - CHALLENGE - Flask Trivia API Pt 1
Make the landing page ("/") return an HTML form.

The form should ask a trivia question of your choosing (feel free to re-use HTML from prior labs!)
The answer should be POSTed to another path.
Depending on the answer POSTed from the form, do the following:

If the answer is correct, redirect your user to the "/correct" route!
If the answer is wrong, return them to the form to try again.
'''
'''
Lab 106 - CHALLENGE - Flask Trivia API Pt 2
-Adapt the HTML and render_template function in 
your previous script to do the following:
--Pass a variable into your render_template function 
  (like step 20 in lab 91)
--Use that variable in your HTML! (like step 23 in lab 91) Some ideas:
---Include the player's name
---Did you create separate pages for correct or incorrect 
   answers? Why not combine those into a single page- and 
   use jinja2 if-logic to display whether the answer was 
   correct or incorrect.
---Display a random question (you don't NEED to use an API 
   call for this; you can create a list/dictionary of your own making 
   inside your Flask script!)
---Turn your trivia into a number guessing game! Use jinja2 
   if-logic to tell the user if they guessed too high, too low, or correctly!
'''

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/correct")
def success():
    return f'Correct!'

@app.route("/")
def home():
    return render_template("trivia.html")

@app.route("/login", methods = ["POST"])
def login():
    if request.form.get("nm") and request.form.get("nm").capitalize() == "Scotland":
        return redirect("/correct")
    else:
        return redirect("/")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)