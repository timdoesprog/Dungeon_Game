# 03.03.2017


import random
import os
# TODO LIST
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
# tuples with (x, y) coordinates
CELLS = [   (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
        ]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        # for all the cells except the most right one
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        # for the last cell on the right
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")

        print(output, end=line_end)



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


def game_loop():
    # populate the variables
    monster, door, player = get_location()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)

        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit.")

        move = input(">> ").upper()

        if move == "QUIT" or move == "Q":
            print("\n ** See you next time. ** \n")
            break

        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n ** NOOOO! The monster ate you whole. ** \n")
                playing = False

            if player == door:
                print("\n ** Congratulations! You escaped the dungeon.** \n")
                playing = False

        else:
            input("\n ** Opps, hit a wall! ** \n")

    # gets executed if now break occurs in the while loop
    # so when the player either gets eaten by the monster
    # or finds the door
    else:
        if input("Play again? [Y/n]").lower() != "n":
            game_loop()


clear_screen()
print("You ended up in a wet and dark dungeon!")
print("You need to find the room with the exit.")
print("But beware! A monster lingers in one of the rooms")
print("and will eat you alive if you come across it.")
input("Press return to Start")
clear_screen()
game_loop()
