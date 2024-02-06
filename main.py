# tictactoe

# import necessary modules

import os
import sys

# initialize gloval variable
turn = 1

# Set up play grid
grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def playfield():
    print("-" * 13)
    print("| " + grid[0] + " | " + grid[1] + " | " + grid[2] + " |")
    print("-" * 13)
    print("| " + grid[3] + " | " + grid[4] + " | " + grid[5] + " |")
    print("-" * 13)
    print("| " + grid[6] + " | " + grid[7] + " | " + grid[8] + " |")
    print("-" * 13)


print("Tic Tac Toe")
playfield()


def player_one():
    global turn
    while True:
        if turn > 9:
            gameover()
        else:
            print(f"Turn: {turn}")
            print(f"Which space do you want to take {player1}?")
            move = int(input("Enter the number here: "))
            if player1symbol in grid[move - 1] or player2symbol in grid[move - 1]:
                print("Space taken. Try again.")
                continue
            else:
                grid[move - 1] = player1symbol
                turn += 1
                os.system('cls')
                playfield()
                player_two()


def player_two():
    global turn
    while True:

        if turn > 9:
            gameover()
        else:
            print(f"Turn: {turn}")
            print(f"Which space do you want to take {player2}?")
            move = int(input("Enter the number here: "))
            if player1symbol in grid[move - 1] or player2symbol in grid[move - 1]:
                print("Space taken. Try again.")
                continue
            else:
                grid[move - 1] = player2symbol
                turn += 1
                os.system('cls')
                playfield()
                player_one()


def gameover():
    playing == False
    print("game over")
    sys.exit("Goodbye!")


# Get player names
print()
print("Who will play Xs?")
player1 = input("Enter your first name: ").title()
print()
print("Who will play Os?")
player2 = input("Enter your first name: ").title()
print()
print(f"Welcome {player1} and {player2}!")

# Player symbols
player1symbol = "X"
player2symbol = "O"

playing = True
while playing == True:
    player_one()
