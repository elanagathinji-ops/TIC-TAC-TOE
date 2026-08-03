# Welcome to TIC TAC TOE

import random
# Assign players and print blank grid
print("**** Welcome to TIC TAC TOE!**** \n")
p1 = 'tim'  # input("Enter a name for Player 1: ").title()
p2 = 'sarah'  # input("Enter a name for Player 2: ").title()
grid = [[' ' for k in range(3)] for j in range(3)]

# Randomly allocate who goes first
while True:
    choice = random.randint(-1, 1)
    if choice == 1:
        print(f"{p1} goes first! \n")
        break
    elif choice == -1:
        print(f"{p2} goes first! \n ")
        break
    else:
        continue


def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

# Choose a coordinate on a grid


def choose_coord():
    while True:
        row = '2'  # (input(" Select a row (1,2 or 3): "))
        # in case input is not a valid number
        if row == '1' or row == '2' or row == '3':
            row = int(row)
            break
        else:
            print("Invalid input - please enter either 1, 2 or 3")
    while True:
        column = '3'  # (input("Select a column (1,2 or 3): "))
        if column == '1' or column == '2' or column == '3':
            column = int(column)
            break
        else:
            print("Invalid input - please enter either 1, 2 or 3")
    return [row-1,  column-1]

# Draw 'X' or 'O' in the grid
# Check if coord is already full


def draw_symbol():
    while True:
        row, column = choose_coord()
        if grid[row][column] != " ":
            print("Oops! That spot is taken, try again.")
            continue
        else:
            if choice == 1:
                grid[row][column] = 'X'
            else:
                grid[row][column] = 'O'
            break
    return grid


# check for

# Switch turns

def switch_turns():
    choice *= -1
    if choice == 1:
        print(f"Now its {p1}'s turn! \n")
    else:
        print(f"Now its {p2}'s turn! \n")


# Need to check if play has won after 3 turns
def game_status():
    for row in grid:
        if row == ['X', 'X', 'X'] or row[0] == row[1] and row[1] == row[2] and row[0] == "X":
            print(f"Congratulations, {p1}! You win!")
        elif row == ['O', 'O', 'O'] or row[0] == row[1] and row[1] == row[2] and row[0] == "O":
            print(f"Congratulations, {p2}! You win!")
        else:
            continue


# Game must end if a player wins or board is full (=draw)

print_grid(grid)
# Game play


draw_symbol()
print()
print_grid(grid)
game_status()
