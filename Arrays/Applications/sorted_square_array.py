""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Write a function that takes in a non-empty array of integers             │
  │ that are sorted in ascending order and returns a new array of            │
  │ the same length with the squares of the original                         │
  │ integers also sorted in ascending order.                                 │
  └──────────────────────────────────────────────────────────────────────────┘
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ array = [1, 2, 3, 5, 6, 8, 9]                                            │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ [1, 4, 9, 25, 36, 64, 81]                                                │
  └──────────────────────────────────────────────────────────────────────────┘
"""


def sorted_squared_array(array):
    """
    >>> sorted_squared_array([1, 2, 3, 5, 6, 8, 9])
    [1, 4, 9, 25, 36, 64, 81]
    """
    array_len = len(array)
    first_idx = 0
    last_idx = array_len-1
    result = [0] * array_len

    while first_idx <= last_idx:
        array_len -= 1
        if abs(array[first_idx]) <= abs(array[last_idx]):
            result[array_len] = array[last_idx]**2
            last_idx -= 1
        if abs(array[first_idx]) > abs(array[last_idx]):
            result[array_len] = array[first_idx]**2
            first_idx += 1
    return result


""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Time Complexity: O(n)                                                    │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ Space Complexity: O(n)                                                   │
  └──────────────────────────────────────────────────────────────────────────┘
 """
