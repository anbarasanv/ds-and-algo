""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ You're given an array of integers and an integer. Write a function               ║
  ║ that moves all instances of that integer in the array to the                     ║
  ║ end of the array and returns the array.                                          ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ The function should perform this in place                                        ║
  ║ (i.e., it should mutate the input array) and                                     ║
  ║ doesn't need to maintain the order of the other integers.                        ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ array = [2, 1, 2, 2, 2, 3, 4, 2]                                                 ║
  ║ toMove = 2                                                                       ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4                              ║
  ║ could be ordered differently                                                     ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def move_element_to_end(array, to_move):
    """
    >>> move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)
    [4, 1, 3, 2, 2, 2, 2, 2]
    """
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] == to_move and right != to_move:
            array[left], array[right] = array[right], array[left]
            right -= 1
        if array[right] == to_move:
            right -= 1
        if array[left] != to_move:
            left += 1
    return array
