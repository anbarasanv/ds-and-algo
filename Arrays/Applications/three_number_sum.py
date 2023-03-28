""" 
  ╔════════════════════════════════════════════════════════════════════════════════════╗
  ║ Write a function that takes in a non-empty array of distinct integers and          ║
  ║ an integer representing a target sum. The function should find all triplets        ║
  ║ in the array that sum up to the target sum and return a two-dimensional            ║
  ║ array of all these triplets. The numbers in each triplet should be                 ║
  ║ ordered in ascending order, and the triplets themselves should be ordered          ║
  ║ in ascending order with respect to the numbers they hold.                          ║
  ║ If no three numbers sum up to the target sum,                                      ║
  ║ the function should return an empty array.                                         ║
  ╠════════════════════════════════════════════════════════════════════════════════════╣
  ║ array = [12, 3, 1, 2, -6, 5, -8, 6]                                                ║
  ║ targetSum = 0                                                                      ║
  ╠════════════════════════════════════════════════════════════════════════════════════╣
  ║ [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]                                               ║
  ║                                                                                    ║
  ╚════════════════════════════════════════════════════════════════════════════════════╝
 """


def three_number_sum(array, target):
    """
    >>> three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    """
    expected_lst = []
    array.sort()
    for idx in range(len(array)-2):
        left = idx+1
        right = len(array)-1

        while left < right:
            current_sum = array[idx]+array[left]+array[right]
            if current_sum == target:
                expected_lst.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
    return expected_lst
