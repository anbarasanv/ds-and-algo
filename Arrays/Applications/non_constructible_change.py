""" 
  ╔════════════════════════════════════════════════════════════════════════════════════╗
  ║ Given an array of positive integers representing the values of                     ║
  ║ coins in your possession, write a function that returns the                        ║
  ║ minimum amount of change(the minimum sum of money) that you cannot create.         ║
  ║ The given coins can have any positive integer value and                            ║
  ║ aren't necessarily unique(i.e., you can have multiple coins of the same value).    ║
  ║ For example, if you're given coins = [1, 2, 5],                                    ║
  ║ the minimum amount of change that you can't create is 4.                           ║
  ║ If you're given no coins, the minimum amount of change that you can't create is    ║
  ║ 1.                                                                                 ║
  ╠════════════════════════════════════════════════════════════════════════════════════╣
  ║ Input                                                                              ║
  ║ coins = [5, 7, 1, 1, 2, 3, 22]                                                     ║
  ╠════════════════════════════════════════════════════════════════════════════════════╣
  ║ Output                                                                             ║
  ║ 20                                                                                 ║
  ║                                                                                    ║
  ╚════════════════════════════════════════════════════════════════════════════════════╝
"""


def non_consturctible_change(array):
    """
    >>> non_consturctible_change([5, 7, 1, 1, 2, 3, 22])
    20
    """
    sum_change = 0
    array.sort()
    for elem in array:
        if elem > sum_change+1:
            return sum_change+1
        sum_change += elem
    return sum_change+1
