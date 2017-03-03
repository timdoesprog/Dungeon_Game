# 03.03.2017

import random
import os

# draw the grid
# pick random location for player
# pick random location for exit door
# random location for the monster
# draw player
# input for movement
# move player, unless invalid move ( outside grid )
# check for win/loss
# clear screen and redraw grid


# Grid with 5x5 cells
# tuples with (x, y)
CELLS = [   (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
        ]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




def get_location():
    # picks three unique random positions in the grid
    return random.sample(CELLS, 3)

def move_player(player, move):
    # get the player's location
    # move LEFT =   x - 1
    # move RIGHT =  x + 1
    # move UP =     y - 1
    # move DOWN =   y + 1
    x, y = player

    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "DOWN":
        y += 1
    if move == "UP":
        y -= 1
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player

    # if player's y == 0, they can't move UP
    # if player's y == 4, they can't move DOWN
    # if player's x == 0, they can't move LEFT
    # if player's x == 4, they can't move RIGHT
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")

    return moves



# populate the grid
monster, door, player = get_location()


while True:
    valid_moves = get_moves(player)
    clear_screen()
    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player))
    print("You can move {}".format(", ".join(valid_moves)))
    print("Enter QUIT to quit.")

    move = input(">> ").upper()

    if move == "QUIT" or move == "Q":
        break

    if move in valid_moves:
        player = move_player(player, move)
    else:
        print("\n ** Opps, hit a wall! ** \n")
        continue


    # on door = win
    # on monster = lose
