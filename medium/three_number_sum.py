"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.
  If no three numbers sum up to the target sum, the function should return an
  empty array.
"""


def threeNumberSum(array, targetSum):
    res = []
    for i in range(0, len(array)):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            for k in range(j + 1, len(array)):
                thirdNum = array[k]
                if firstNum + secondNum + thirdNum == targetSum:
                    temp = []
                    temp.append(firstNum)
                    temp.append(secondNum)
                    temp.append(thirdNum)
                    temp.sort()
                    res.append(temp)
    return sorted(res)


print(threeNumberSum(list(map(int, input().split())), int(input())))
