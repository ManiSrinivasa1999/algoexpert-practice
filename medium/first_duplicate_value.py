"""
  Given an array of integers between 1 and n ,
  inclusive, where  is the length of the array, write a function
  that returns the first integer that appears more than once (when the array is
  read from left to right).
  In other words, out of all the integers that might occur more than once in the
  input array, your function should return the one whose first duplicate value
  has the minimum index.
  If no integer appears more than once, your function should return -1
"""
def firstDuplicateValue(array):
    nonRepeatedValues = []
    result = 0
    if len(array) == 0 or len(array) == 1 or len(array) == len(set(array)):
        return -1
    for i in array:
        if i not in nonRepeatedValues:
            nonRepeatedValues.append(i)
        else:
            result =+ i
            break
    return result
print(firstDuplicateValue(list(map(int, input().split()))))