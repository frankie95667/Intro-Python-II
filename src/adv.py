from room import Room
from item import Item
from monster import Monster
from lightSource import LightSource
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

# Declare all monsters
sharkhead = Monster("sharkhead", "Shark head with a human body")
clown = Monster("clown", "Seems funny and playful until you get too close")

# Add monster to room
room['outside'].addMonster(sharkhead)
room['outside'].addMonster(clown)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Set if room is light
room['outside'].is_light = True
room['foyer'].is_light = False
room['overlook'].is_light = True
room['narrow'].is_light = False
room['treasure'].is_light = False

# Items

hammer = Item("hammer", "hammer")
torch = LightSource("torch", "lights up rooms")
coin = Item("coin", "cash money bitches")
sword = Item("sword", "Inflicts 100%% damage to everyone")
rubberduck = Item(
    "ducky", "Destroys the remainder of your enemies you and you win the game")

# Add items to rooms

room['outside'].addItem(torch)
room['foyer'].addItem(hammer)
room['foyer'].addItem(sword)
room['treasure'].addItem(coin)
room['overlook'].addItem(rubberduck)


# Parses moves
def parse_move(player, move):
    valid_moves = ["n", "s", "e", "w"]
    room = player.current_room

    if(len(move.split(" ")) > 1):
        action = move.split(" ")[0]
        name = move.split(" ")[1]

        if(action == "take" or action == "get"):
            removedItem = room.removeItem(name)
            if(removedItem):
                player.addItem(removedItem)
            return room
        elif(action == "drop"):
            removedItem = player.removeItem(name)
            if(removedItem):
                room.addItem(removedItem)
            return room
        elif(action == "attack"):
            monster = room.getMonster(name)
            if(monster):
                health = monster.on_attack(player)
                if(health <= 0):
                    room.removeMonster(name)
            return room
        else:
            return room
    else:
        if(move == "q"):
            return

        if(move == "i" or move == "inventory"):
            player.getInventory()
            player.isInstance()
            return room

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
        if(player.isInstance()):
            print(player.current_room)
        else:
            print("\nIt's pitch black!\n")
        # * Waits for user input and decides what to do.
        move = input("What would you like to do? ")
        if(move == "q"):
            is_playing = False
        player.current_room = parse_move(player, move)
        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
