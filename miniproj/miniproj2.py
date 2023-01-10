#!/usr/bin/python3
'''
StephanieCobble | Lab 70 - Mini-Project2 - RPG Script
Starter code from the mygame01 file
Driving a simple game framework with a dictionary object | Alta3 Research
'''

def showInstructions():
    # Show the game instructions when called
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    To WIN: Find the key, potion, and make it to the Garden! 
    Make sure to avoid monsters, or you LOSE!
    Commands:
      go [direction]
      get [item]
    ''')


def showStatus():
    # determine the current status of the player
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])

    # to print to user where they can go
    if currentRoom == 'Hall':
        for key in rooms.get(currentRoom).keys():
            if key != 'item':
                print(f'You may go: {key}')
    elif currentRoom == 'Kitchen':
        for key in rooms.get(currentRoom).keys():
            if key != 'item':
                print(f'You may go: {key}')
    elif currentRoom == 'Dining Room':
        for key in rooms.get(currentRoom).keys():
            if key != 'item':
                print(f'You may go: {key}')
    elif currentRoom == 'Garden':
        for key in rooms.get(currentRoom).keys():
            if key != 'item':
                print(f'You may go: {key}')

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room',
        'item': 'sword' # added sword
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

move_count = 0

# breaking this while loop means the game is over
while True:
    showStatus()
    # move count will log the number of times the user interacts in the game
    move_count += 1
    print(f'Move count: {move_count}')
    # print("---------------------------")
    # the player MUST type something in
    # otherwise input will keep asking
    move = ''

    while move == '':
        move = input('>')
    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)


    # if they type 'go' first
    if move[0] == 'go':

        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'sword' in inventory:
            del rooms[currentRoom]['item']
            print("You have defeated the monster!")
        else:
            print('A monster got you... GAME OVER!')
            break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
