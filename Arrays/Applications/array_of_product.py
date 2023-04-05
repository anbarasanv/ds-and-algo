""" 
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in a non-empty array of integers and                 ║
  ║ returns an array of the same length, where each element in the output            ║
  ║ array is equal to the product of every other number in the input array.          ║
  ║                                                                                  ║
  ║ In other words, the value at output[i] is equal to the product                   ║
  ║ of every number in the input array other than input[i].                          ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ Note that you're expected to solve this problem without using division.          ║
  ║                                                                                  ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ array = [5, 1, 4, 2]                                                             ║
  ╠══════════════════════════════════════════════════════════════════════════════════╣
  ║ [8, 40, 10, 20]                                                                  ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
 """


def array_of_product(array):
    """ 
    >>> array_of_product([5, 1, 4, 2])
    [8, 40, 10, 20]
    """
    result = [1]*len(array)

    # Finding the products left to the current elements
    # adding that to the result
    left_current_product = 1
    for i in range(len(array)):
        result[i] = left_current_product
        left_current_product *= array[i]

    # Finding the products right to the current elements
    # multiplying that to the result
    right_current_product = 1
    for i in reversed(range(len(array))):
        result[i] *= right_current_product
        right_current_product *= array[i]

    return result
