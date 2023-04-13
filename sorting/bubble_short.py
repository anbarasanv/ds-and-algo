""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in an array of integers and                          ║
  ║ returns a sorted version of thatarray.                                           ║
  ║ Use the Bubble Sort algorithm to sort the array.                                 ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def buble_sort(arr):
    """
    >>> buble_sort([8, 10, 12, 7, 13, 5, 6, 4, 1, 2])
    [1, 2, 4, 5, 6, 7, 8, 10, 12, 13]
    """
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
