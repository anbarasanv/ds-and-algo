

def spiral_traverse(array):
    """
    Traverse the outermost layer of the matrix, then traverse the next outermost layer, 
    and so on.

    Args:
      array: the 2D array we're traversing

    Returns:
      the spiral traversal of the array.

    >>> spiral_traverse([
    ... [1,   2,  3, 4],
    ... [12, 13, 14, 5],
    ... [11, 16, 15, 6],
    ... [10,  9,  8, 7],
    ... ])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    """
    result = []
    first_row, last_row = 0, len(array)-1
    first_col, last_col = 0, len(array[0])-1

    while first_row <= last_row and first_col <= last_col:
        # Treversing Letft --> Range inclusive of last column
        for col in range(first_col, last_col+1):
            result.append(array[first_row][col])

        # This required for the edge case where arrray with one row
        if first_row == last_row:
            break

        # Treversing Down --> Range inclusive of last row
        for row in range(first_row+1, last_row+1):
            result.append(array[row][last_col])

        # This required for the edge case where arrray with one column
        if first_col == last_col:
            break

        # Treversing Right <-- Range exlusive of last colum
        for col in reversed(range(first_col, last_col)):
            result.append(array[last_row][col])

        # Treversing Top --> Range exlusive of last row
        for row in reversed(range(first_row+1, last_row)):
            result.append(array[row][first_col])

        first_row += 1
        last_row -= 1
        first_col += 1
        last_col -= 1

    return result


array = [
    [1,   2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
]
print(spiral_traverse(array))
