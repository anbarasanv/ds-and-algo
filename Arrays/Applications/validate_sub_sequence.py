""" 
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ Sample InputSample InputGiven two non-empty arrays of integers, write a    │
  │ function that                                                              │
  │ determines whether the second array is a subsequence of the first one.     │
  │                                                                            │
  │ A subsequence of an array is a set of numbers that aren't necessarily      │
  │ adjacent in the array but that are in the same order as they appear in     │
  │ the array.                                                                 │
  │                                                                            │
  │ For instance, the numbers [1, 3, 4] form a subsequence of the array [1,    │
  │ 2, 3, 4], and so do the numbers                                            │
  │ [2, 4]. Note that a single number in an array and the array itself are     │
  │ both valid subsequences of the                                             │
  │ array.                                                                     │
  │                                                                            │
  └────────────────────────────────────────────────────────────────────────────┘
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ array = [5, 1, 22, 25, 6, -1, 8, 10]                                     │
  │ sequence = [1, 6, -1, 10]                                                │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ true                                                                     │
  └──────────────────────────────────────────────────────────────────────────┘
 """


def validate_sub_sequence(array, subsequence):
    """
    >>> validate_sub_sequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
    True
    """
    count = 0
    for element in array:
        if subsequence[count] == element:
            count += 1
    return count == len(subsequence)


""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Time Complexity: O(n)                                                    │
  └──────────────────────────────────────────────────────────────────────────┘
 """
