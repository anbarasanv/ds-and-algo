""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ You're given an array of integers and another array of                           ║
  ║ three distinct integers. The first array is guaranteed to                        ║
  ║ only contain integers that are in the second array, and                          ║
  ║ the second array represents a desired order for the integers                     ║
  ║ in the first array. For example, a second array of [x, y, z]                     ║
  ║ represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z]         ║
  ║ in the first array.                                                              ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ Write a function that sorts the first array according to the desired             ║
  ║ order in the second array.                                                       ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def three_number_sort(array, order):
    """
    >>> three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1])
    [0, 0, 0, 1, 1, 1, -1, -1]
    """
    left_num = order[0]
    right_num = order[-1]

    swap_idx = 0
    for i in range(len(array)):
        if array[i] == left_num:
            array[i], array[swap_idx] = array[swap_idx], array[i]
            swap_idx += 1

    swap_idx = -1
    for i in reversed(range(len(array))):
        if array[i] == right_num:
            array[i], array[swap_idx] = array[swap_idx], array[i]
            swap_idx -= 1

    return array
