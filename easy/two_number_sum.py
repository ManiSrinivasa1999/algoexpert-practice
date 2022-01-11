'''
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.


  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.


  You can assume that there will be at most one pair of numbers summing up to
  the target sum.
'''


def twoNumberSum(array, targetSum):
    result = []
    for i in enumerate(array):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                result.append(firstNum)
                result.append(secondNum)
    return result


array = list(map(int, input().strip().split()))
targetSum = int(input())
print(twoNumberSum(array, targetSum))
