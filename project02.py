#!/usr/bin/python3
"""
Will Park | Heist / Escape RPG Game (Python Project 2)

A text-based heist and escape game where the player has to
find a certain item in a room and escape to win.
"""

def show_game_info():
    """Print game information"""
    # print game objective and commands
    print("""
    Mission Objective: Find a secret document and get to the escape zone

    >>>>>-------------------------------------------------------
    Commands:
        info              -->  Displays (this) game information again.
        map               -->  Shows the map.
        go [direction]    -->  Go to a different room (e.g., move east).
        search            -->  Search the room for an item.
        escape            -->  Escape from the building.
    >>>>>-------------------------------------------------------
    """)

def print_item_message(item):
    """Print an appropriate message when the user acquires an item"""
    # if the user has acquired a military order (which is actually the secret document)
    if item == "military orders":
        # prompt them to escape to the escape zone
        print("It seems that you've found a document. Maybe it's time to go home?")
    # if the user has acquired a stack of paper (which is a fake secret document)
    if item == "a stack of paper":
        # prompt a lingering message
        print("It seems that you've found some documents. Is this what you were looking for?")
    # for other regular items, inform the user of what item they acquired
    else:
        print(f"You have a {item} now.")

def show_status():
    """Display the current status of the game"""
    # print the user's current location
    print("------------------------------")
    print("Number of Moves (Between Rooms): " + str(num_moves)) 
    print("Current Location: " + current_room)
    # print what the player is carrying
    print("Current Inventory:", inventory)
    # check if there's an item in the room
    print("------------------------------")

def search_room():
    """Check if there is an item in the room and print the information and let the user either grab it or leave it"""
    # if there is an item in the room
    if "item" in rooms[current_room]:
        # placeholder for user's choice
        user_choice = ""
        # inform the user about the found item and keep prompting for their decision until they enter "y" or "n"
        while user_choice == "":
            # wait until user enters a decision and save their response as a variable
            user_input = input(f"You found a {rooms[current_room]['item']}. Do you want to grab it? (y/n)\n>>> ").lower().strip()
            # if the user's response is "y"
            if user_input == "y":
                # change user_choice variable to escape the loop
                user_choice = "y"
                # add the item to their inventory
                inventory.append(rooms[current_room]["item"])
                # print appropriate message regarding the item
                print_item_message(rooms[current_room]["item"])
                #delete the item key:value pair from the room's dictionary
                del rooms[current_room]["item"]
            # if the user's response is "n"
            if user_input == "n":
                # change user_choice variable to escape the loop
                user_choice = "n"
                # inform them that they did not grab the item
                print(f"You decided to leave {rooms[current_room]['item']} in this room.")
    # if there is no item in the room
    else:
        # inform the user that there is no item in the room
        print("You've searched the room but couldn't find anything.")

def escape():
    """Handles escape scenarios if the player uses the escape command in Room 3"""
    # if the player has acquired the correct document
    if "military orders" in inventory:
        print("Radio: \"Good job, Pete. This will prove our innocence.\"")
        print("--- You Won ---")
    # if the player grabbed the wrong document
    elif "a stack of paper" in inventory:
        print("Radio: \"This is not the right document. The emperor is very disappointed...\"")
        print("--- You Lost ---")
    # if the player escaped without any document
    else:
        print("Radio: \"You escaped with nothing? The emperor wants to see you... NOW.\"")
        print("--- You Lost ---")

# move counter used to trigger the alarm item
num_moves = 0

# user's inventory (initially empty)
inventory = []

# a dictionary linking a room to other rooms
rooms = {
    "Room1": {
        "east" : "Room2",
        "south": "Room4",
    },
    "Room2": {
        "east" : "Room3",
        "west" : "Room1",
        "item" : "taser"
    },
    "Room3": {
        "west" : "Room2",
        "south" : "Room5"
    },
    "Room4": {
        "east" : "Room5",
        "north" : "Room1",
        "south" : "Room6"
    },
    "Room5": {
        "west" : "Room4",
        "north" : "Room3",
        "south" : "Room7",
        "item" : "a stack of paper",
        "person" : "guard"
    },
    "Room6": {
        "east" : "Room7",
        "north" : "Room4",
        "item" : "alarm",
    },
    "Room7": {
        "west" : "Room6",
        "north" : "Room5",
        "item" : "military orders",
        "person" : "guard"
    }
}

# a list of strings that represent the map and its legends
map = [
    " EE  =>  Escape Zone\n\n",
    " /D/ =>  Door\n\n",
    " X   =>  Mystery Item\n\n",
    " @   =>  Guard (Enemy)\n\n"
    "               Floor 1\n\n",
    "+---------------+-----------+--------------+\n",
    "|               |           |           EE |\n",
    "|     Room 1   /D/  Room 2 /D/   Room 3    |\n",
    "|               |  X        |              |\n",
    "+------/D/------+-----------+-----/D/------+\n",
    "|               |                          |\n",
    "|     Room 4    |          Room 5          |\n",
    "|               |                          |\n",
    "|              /D/                X        |\n",
    "|               |            @             |\n",
    "|               |                          |\n",
    "|               |                          |\n",
    "+------/D/------+--------+-------/D/-------+\n",
    "|                        |             @   |\n",
    "|         Room 6        /D/    Room 7      |\n",
    "|    X                   |               X |\n",
    "+------------------------------------------+\n"
]

# start the game with user in Room 1
current_room = "Room1"

# display the game information with mission objectives and commands at the beginning of the game
show_game_info()

# allow the user to keep playing the game until the game is over
while True:
    # display the current game status
    show_status()

    # keep prompting the player to enter a command until they enter one 
    command = ""
    while command == "":  
        command = input("Enter your next command\n>>> ").strip()

    # print empty lines for better readability
    print("\n\n")

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    command = command.lower().split(" ", 1)

    # if the command is "info", display the game info again
    if command[0] == "info":
        show_game_info()

    # if the command is "map", display the map
    if command[0] == "map":
        print("".join(map))

    # if the command starts with "go"
    if command[0] == "go":
        # if the user entered a valid direction followed by "go"
        if command[1] in rooms[current_room]:
            # if the user moved from Room 1 to Room 4, delete Room 4's "north" key-value pair (reference to Room 1)
            if current_room == "Room1" and command[1] == "south":
                # delete Room 4's "north" key-value pair
                del rooms["Room4"]["north"]
                # inform the user about the trap door
                print("It seems that it's a one-way door. You can't go back that way now.")
            # set the current room to be the new room
            current_room = rooms[current_room][command[1]]
            # increment the number of moves
            num_moves += 1
        # if the user is trying to go to an unreachable room (wrong directin after "go")
        else:
            # inform the user about the invalid input and prompt them to use the map
            print("You cannot go that way. Please check the map again.")

    # if the command is "search"
    if command[0] == "search":
        # search the room and display appropriate results
        search_room()

    # if the command is "escape"
    if command[0] == "escape":
        # check if the user is currently in Room 3
        if current_room == "Room3":
            # and if so, print appropriate game result
            escape()
            break
        # if the user is not in room 3 and used "escape" command, inform them where they can escape
        else:
            print("You cannot escape from here (you can only escape in Room 3).")

    # following checks are used to trigger game events after the user has made a move.
    # check if the player is in room 5 (possible player loss scenario)
    if current_room == "Room5" or current_room == "Room7":
        # and if the user has taser in the inventory
        if "person" in rooms[current_room]:
            if "taser" in inventory:
                # eliminate the guard from current room
                del rooms[current_room]["person"]
                # player tases the guard and can continue the game
                print() # print an empty line for better readability
                print("Nice try, guard! You saw the enemy first and tased him.")
            # if the player does not have taser in the inventory
            else:
                # the guard shoots them and the player loses the game
                print("Oh shoot! The guard saw you first and shot you with a handgun.")
                print("--- You Lost ---")
                break
    
    # if the player grabbed the alarm item and has moved more than 6 times (players loss scenario)
    if "alarm" in inventory and num_moves > 6:
        # the alarm goes off and player loses
        print("Uh oh. The alarm you grabbed started blaring and alerted more guards.")
        print("Hint: The alarm may go off if you move more than 6 times between rooms while it's in your inventory.")
        print("--- You Lost ---")
        break

    # print empty lines for better readability after a command
    print("\n\n")