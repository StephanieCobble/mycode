#!/usr/bin/env python3
"""
StephanieCobble | Lab 92 - ISS Tracker

"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    ts = datetime.datetime.fromtimestamp(resp["timestamp"])
    tsprint = ts.strftime('%Y-%m-%d %H:%M:%S')
    
    loc_resp = rg.search((resp["iss_position"]["latitude"], resp["iss_position"]["longitude"]))
    city = loc_resp[0]["name"]
    country = loc_resp[0]["cc"]

    print(f'The current location of the ISS is: \n\
            Timestamp: {tsprint} \n\
            Lon: {resp["iss_position"]["longitude"]} \n\
            Lat: {resp["iss_position"]["latitude"]} \n\
            City & Country: {city}, {country}')

if __name__ == "__main__":
    main()

