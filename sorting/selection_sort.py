""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in an array of integers and returns a sorted         ║
  ║ version of that array. Use the Selection Sort algorithm to sort the array.       ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def selection_sort(array):
    """
    >>> selection_sort([8, 10, 12, 7, 13, 5, 6, 4, 1, 2])
    [1, 2, 4, 5, 6, 7, 8, 10, 12, 13]
    """
    array_len = len(array)
    for i in range(array_len):
        j = i + 1
        curr_idx = i
        while j < array_len:
            if array[curr_idx] > array[j]:
                curr_idx = j
            j += 1
        array[i], array[curr_idx] = array[curr_idx], array[i]
    return array
