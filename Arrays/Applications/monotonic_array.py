""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in an array of integers and returns                  ║
  ║ a boolean representing whether the array is monotonic.                           ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ An array is said to be monotonic if its elements, from left to right,            ║
  ║ are entirely non-increasing or entirely non-decreasing.                          ║
  ║ Non-increasing elements aren't necessarily exclusively decreasing;               ║
  ║ they simply don't increase. Similarly, non-decreasing elements aren't            ║
  ║ necessarily exclusively increasing; they simply don't decrease.                  ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ Note that empty arrays and arrays of one element are monotonic.                  ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]                         ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ true                                                                             ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def monotonic_array(array):
    """
    >>> monotonic_array([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])
    True
    """
    increasing = True
    decreasing = True
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            increasing = False
        elif array[i] > array[i+1]:
            decreasing = False
        if not increasing and not decreasing:
            return False
    return True


""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Time Complexity: O(n)                                                            ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ Space Complexity: O(1)                                                           ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
"""
