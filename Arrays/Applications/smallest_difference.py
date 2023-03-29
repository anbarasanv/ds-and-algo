""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in two non-empty arrays of integers,                 ║
  ║ finds the pair of numbers (one from each array) whose absolute                   ║
  ║ difference is closest to zero, and returns an array containing                   ║
  ║ these two numbers, with the number from the first array in the                   ║
  ║ first position.                                                                  ║
  ║                                                                                  ║
  ║ Note that the absolute difference of two integers is the                         ║
  ║ distance between them on the real number line. For example,                      ║
  ║ the absolute difference of -5 and 5 is 10, and the absolute                      ║
  ║ difference of -5 and -4 is 1.                                                    ║
  ║                                                                                  ║
  ║ You can assume that there will only be one pair of numbers                       ║
  ║ with the smallest difference.                                                    ║
  ║                                                                                  ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ arrayOne = [-1, 5, 10, 20, 28, 3]                                                ║
  ║ arrayTwo = [26, 134, 135, 15, 17]                                                ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ [28, 26]                                                                         ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def smallest_difference(array_1, array_2):
    """
    >>> smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    [28, 26]
    """
    # we can assign to first index because it's a non-empty array
    array_1.sort()
    array_2.sort()
    current_smallest = abs(array_1[0]-array_2[0])
    result = None
    a1_idx = 0
    a2_idx = 0

    while a1_idx < len(array_1) and a2_idx < len(array_2):
        if array_1[a1_idx] == array_2[a2_idx]:
            return [array_1[a1_idx], array_2[a2_idx]]

        current_small_diff = abs(array_1[a1_idx]-array_2[a2_idx])
        if current_small_diff < current_smallest:
            current_smallest = current_small_diff
            result = [array_1[a1_idx], array_2[a2_idx]]

        if array_1[a1_idx] <= array_2[a2_idx]:
            a1_idx += 1
        elif array_1[a1_idx] > array_2[a2_idx]:
            a2_idx += 1

    return result


""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Time Complexity: O(n)                                                            ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ Space Complexity: O(1)                                                           ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """
