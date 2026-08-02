# Welcome to TIC TAC TOE

import random
print("**** Welcome to TIC TAC TOE!**** \n")
p1 = 'tim'  # input("Enter a name for Player 1: ").title()
p2 = 'sarah'  # input("Enter a name for Player 2: ").title()

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

grid = [[' ' for k in range(3)] for j in range(3)]

# grid = [
#    [" ", " ", " "],
#   [" ", " ", " "],
#  [" ", " ", " "]
# ]


def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)


print_grid(grid)

# Choose a coordinate on a grid
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

grid[row-1][column-1] = "X"
print_grid(grid)

choice *= -1
if choice == 1:
    print(f"Now its {p1}'s turn! \n")
else:
    print(f"Now its {p2}'s turn! \n")
