# Welcome to TIC TAC TOE

import random
print("**** Welcome to TIC TAC TOE!**** \n")
p1 = 'tim'  # input("Enter a name for Player 1: ")
p2 = 'sarah'  # input("Enter a name for Player 2: ")

# Randomly allocate who goes first
choice = random.randint(1, 2)
if choice == 1:
    print(f"{p1.title()} goes first! \n")
else:
    print(f"{p2.title()} goes first! \n ")


blank = ' '*11
row = blank + '|' + blank + '|' + blank
grid = (
    '* '*18 + '\n' +
    ((row + '\n')*5 +
     '~'*35 + '\n')*2 +
    (row + '\n')*5 +
    '* '*18 + '\n'
)
print(grid)
