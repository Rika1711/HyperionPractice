# Compulsory Task 1
#
# Create a function that takes a grid of # and -:
#   '#' represents a mine
#   '-' represents a mine-free spot
# Return a grid, where each dash is replaced by a digit that indicates
# the number of mines adjacent ot the spot.

import copy
import pprint

print("##### Minesweeper Grid #####\n")

choice = input("Would you like to create your own grid? \ny or n: ").lower()
input_grid = []

if choice == "y":
    # Additional to main task: Code that lets user define a custom grid.
    def get_mine_grid():
        grid = []
        print('''\nPlease create a grid. It shall consist of 5x5 symbols.
Enter 5 symbols per row and separate them with a white space.
Enter "#" for a mine or "-" for a blank space.
''')

        for i in range(5):
            grid_row = input(f"Row #{i+1}: ")

            # This code makes sure that a row only gets added to the grid
            # if exactly 5 symbols are added.
            while len(grid_row.replace(" ", "")) != 5:
                print("You did not enter 5 symbols. Try again.")
                grid_row = input(f"Row #{i+1}: ")

            grid.append(grid_row.split())
        return grid

    input_grid = get_mine_grid()

elif choice == "n":
    # Code will use pre-determined "input-grid".
    input_grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]
else:
    print("Incorrect input.")
    exit()

output_grid = copy.deepcopy(input_grid)

# This code block goes through every row and column.
for row in range(len(input_grid)):
    for col in range(len(input_grid[0])):

        # If the symbol is not a "#", it will look at
        # the adjacent spots and count mines.
        if input_grid[row][col] != '#':
            mine_count = 0

            # This code is needed to search adjacent rows and columns.
            # The code checks for every possible combination of
            # coordinates for adjacent cells.
            for adj_row in (-1, 0, 1):
                for adj_col in (-1, 0, 1):

                    # This code block makes sure that the code does not
                    # check outside of the grid.
                    # For each mine found in an adjacent cell, +1 will be
                    # added to the counter.
                    if (0 <= row+adj_row < len(input_grid) and
                        0 <= col+adj_col < len(input_grid[0]) and
                        input_grid[row+adj_row][col+adj_col] == '#'):
                        mine_count += 1

            # This block of code will change the value of the
            # current cell to its mine_count.
            output_grid[row][col] = str(mine_count)

print("\nInput grid:")
pprint.pprint(input_grid, width=30)
print("\nOutput grid:")
pprint.pprint(output_grid, width=30)
