#!/usr/bin/python3
"""Pascal's Triangle || ALX Interview project"""


def pascal_triangle(n):
    """
    returns a list of lists of numbers
    representing the pascal triangle
    """
    if n <= 0:
        return []

    # Initialize the pascal triangle list with the first row
    pa_triangle = [[1]]
    
    # Generate each subsequent row of the triangle
    for row_num in range(1, n):
        # Initialize the current row with the first element
        row = [1]
        
        # Generate the elements of the current row
        for i in range(1, row_num):
            # Each element is the sum of the two elements diagonally above it
            element = pa_triangle[row_num-1][i-1] + pa_triangle[row_num-1][i]
            row.append(element)
        
        # Add the last element to the row and append the row to the triangle list
        row.append(1)
        pa_triangle.append(row)
    
    # Return the entire triangle
    return pa_triangle
