"""
  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.

  Note that the absolute difference of two integers is the distance between
  them on the real number line. For example, the absolute difference of -5 and 5
  is 10, and the absolute difference of -5 and -4 is 1.
  
  You can assume that there will only be one pair of numbers with the smallest
  difference.
"""


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    arrayOneIndex = 0
    arrayTwoIndex = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while arrayOneIndex < len(arrayOne) and arrayTwoIndex < len(arrayTwo):
        firstNum = arrayOne[arrayOneIndex]
        secondNum = arrayTwo[arrayTwoIndex]
        if firstNum < secondNum:
            current = secondNum - firstNum
            arrayOneIndex += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            arrayTwoIndex += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


print(smallestDifference(list(map(int, input().split())),
      list(map(int, input().split()))))
