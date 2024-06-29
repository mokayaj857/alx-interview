#!/usr/bin/python3
"""
Pascal triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    # Initialize the first row of Pascal's triangle
    pascal = [[1]]

    for i in range(1, n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        row.append(1)  # Last element is always 1
        pascal.append(row)

    return pascal
