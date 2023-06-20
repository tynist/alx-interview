#!/usr/bin/python3
"""
Calculates the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Args:
        grid (list of list of integers): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """

    # Get the number of rows and columns in the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Initialize the perimeter
    perimeter = 0

    # Iterate over each cell in the grid
    for row in range(num_rows):
        for col in range(num_cols):

            # Check if current cell is land, add 4 to the perimeter
            if grid[row][col] == 1:
                perimeter += 4

                # if current cell is also land & not on the grid's edge
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # minus 2 from d perimeter(shared side)

                # Check if the cell to the left is also land
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # minus 2 from d perimeter(shared side)

    return perimeter
