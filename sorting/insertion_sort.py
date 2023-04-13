""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in an array of integers and                          ║
  ║ returns a sorted version of that array.                                          ║
  ║ Use the Insertion Sort algorithm to sort the array.                              ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def insertion_sort(array):
    """
    >>> insertion_sort([8, 10, 12, 7, 13, 5, 6, 4, 1, 2])
    [1, 2, 4, 5, 6, 7, 8, 10, 12, 13]
    """
    for i in range(1, len(array)):
        curr_num = array[i]
        while array[i - 1] > curr_num and i > 0:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
    return array
