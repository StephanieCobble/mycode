#!/usr/bin/env python3

'''
StephanieCobble | Lab 62 - using for loops

'''

def main():
    
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    
    NE_animals = farms[0]["agriculture"]
    for animal in NE_animals:
        print(f'NE: {animal}')

    W_animals = farms[1]["agriculture"]
    for w_animal in W_animals:
        print(f'W: {w_animal}')

    SE_animals = farms[2]["agriculture"]
    for se_animal in SE_animals:
        print(f'SE: {se_animal}')

    veg = ["carrots", "celery"]

    user_input = input('Please choose a farm to see the animals/plants there. \n\
    Your choices are:\n NE Farm \n W farm \n SE farm \n')

    for farm in farms:
        if farm["name"].lower() == user_input.lower():
            # print(f'{farm["agriculture"]}')
            for agr in farm["agriculture"]:
                if agr not in veg:
                    print(agr)


if __name__ == "__main__":
    main()


