#!/usr/bin/python3
'''
Your script alta3research-flask01.py should demonstrate proficiency with the flask library. 
Ensure your application has:
    at least two endpoints
    at least one of your endpoints should return JSON
    has ONE additional feature from the following list:
        one endpoint returns HTML that uses jinja2 logic
        requires a session value be present in order to get a response
        writes to/reads from a cookie
        reads from/writes to a sqlite3 database
'''

from flask import Flask
import requests

app = Flask(__name__)

url_fact = "https://catfact.ninja/fact"
url_breeds = "https://catfact.ninja/breeds"

@app.route("/breeds")
def cat_breeds():
    search = requests.get(url_breeds)
    breeds_json = search.json()
    for breeds in breeds_json.get("data"):
        return f'List of cat breeds: \n {breeds["breed"]}'

@app.route("/fact")
def search_term():
    search = requests.get(url_fact)
    fact_json = search.json()
    return f"Cat fact of the day! \n {fact_json['fact']}"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)