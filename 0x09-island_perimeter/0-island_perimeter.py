#!/usr/bin/python3
"0x09. Island Perimeter"


def island_perimeter(grid):
    """
        Create a function def island_perimeter(grid)
        that returns the perimeter of the island
        described in grid
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(grid[0]):
            if grid[i][j] == 1:
                perimeter += 4

                # Check above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                # Check left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                # Check below
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

                # Check right
                if j < len(grid(0)) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
