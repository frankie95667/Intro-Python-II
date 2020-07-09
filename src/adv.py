from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Parses moves
def parse_move(room, move):
    valid_moves = ["n", "s", "e", "w"]

    if(move == "q"):
        return

    try:
        valid_moves.index(move)
    except:
        print("Not a valid move. Try again")
        return room

    try:
        if(move == "n"):
            return room.n_to
        elif(move == "s"):
            return room.s_to
        elif(move == "w"):
            return room.w_to
        elif(move == "e"):
            return room.e_to
    except:
        print("No room there. Try again.")
        return room

#
# Main
#
is_playing = True
while(is_playing):

    # Make a new player object that is currently in the 'outside' room.
    name = input("What do you want to be called? ")
    player = Player(name, room['outside'])
    # Write a loop that:
    #
    has_won = False
    while(not has_won and is_playing):
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        print(player.current_room)
        # * Waits for user input and decides what to do.
        move = input("What would you like to do? ")
        if(move == "q"):
            is_playing = False
        player.current_room = parse_move(player.current_room, move)
        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
