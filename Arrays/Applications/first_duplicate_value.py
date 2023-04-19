""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ find the first duplicate value from the 1..n array                               ║
  ║ the returned array value must be minimum in the index                            ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def first_duplicate(array):
    """
    >>> first_duplicate([2,1,5,2,3,3,4])
    2
    """
    for item in array:
        if array[abs(item) - 1] < 0:
            return abs(item)
        else:
            array[abs(item) - 1] = array[abs(item) - 1] * -1
    return -1
