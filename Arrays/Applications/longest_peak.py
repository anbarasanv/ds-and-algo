""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in an array of integers and returns the length of    ║
  ║ the                                                                              ║
  ║ longest peak in the array.                                                       ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ A peak is defined as adjacent integers in the array that are strictly            ║
  ║ increasing until                                                                 ║
  ║ they reach a tip (the highest value in the peak), at which point they become     ║
  ║ strictly                                                                         ║
  ║ decreasing. At least three integers are required to form a peak.                 ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10     ║
  ║ don't and                                                                        ║
  ║ neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form   ║
  ║ a peak                                                                           ║
  ║ because there aren't any strictly decreasing integers after the 3.               ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]                               ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ 6 // 0, 10, 6, 5, -1, -3                                                         ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def longest_peak(array):
    """
    >>> longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])
    6
    """
    longest_peak_len = 0
    i = 1

    while i < len(array)-1:
        is_peak = array[i-1] < array[i] and array[i] > array[i+1]
        # if peak not found continue the search
        if not is_peak:
            i += 1
            continue

        # if peak found check the left of the peak are in strictly decreasing order
        # The reason to take i-2 to jump one elemnt left of peak is to compare immediate
        # left element with next to that element.
        left_idx = i-2
        while left_idx >= 0 and array[left_idx] < array[left_idx+1]:
            left_idx -= 1

        # Similar way comparing right of the peak decreasing
        right_idx = i+2
        while right_idx < len(array) and array[right_idx] < array[right_idx-1]:
            right_idx += 1

        # finding the longes peak, hear subtracting 1 because right index might have
        # already jumped next to the decreasing order
        current_peak_len = right_idx - left_idx - 1
        longest_peak_len = max(longest_peak_len, current_peak_len)
        # now we are not going to find any peak where aleary found peak length
        # we are going to start our next search with right index.
        i = right_idx

    return longest_peak_len


print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
