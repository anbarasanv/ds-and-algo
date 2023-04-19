""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in an array of integers and returns a sorted         ║
  ║ version                                                                          ║
  ║ of that array. Use the Quick Sort algorithm to sort the array.                   ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def quick_sort(array):
    """
    >>> quick_sort([8, 2, 4, 5, 3, 1])
    [1, 2, 3, 4, 5, 8]
    """
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, start_idx, last_idx):
    # base case
    if start_idx >= last_idx:
        return
    # recursive case
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = last_idx

    while left_idx <= right_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
            left_idx += 1
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    array[pivot_idx], array[right_idx] = array[right_idx], array[pivot_idx]

    # ==================================================================================
    #  *                    INFO
    #    we are trying to find the smallest sub array, because when we run the recursive
    #    alogo on that then the large array the space complexity will be O(log n)
    # ==================================================================================
    left_sub_arry_small = (right_idx - 1 - start_idx) < (last_idx - (right_idx + 1))
    if left_sub_arry_small:
        quick_sort_helper(array, start_idx, right_idx - 1)
        quick_sort_helper(array, right_idx + 1, last_idx)
    else:
        quick_sort_helper(array, right_idx + 1, last_idx)
        quick_sort_helper(array, start_idx, right_idx - 1)
