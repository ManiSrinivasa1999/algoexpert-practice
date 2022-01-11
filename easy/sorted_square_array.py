# Write a function that takes in a non-empty array of integers that are sorted
#   in ascending order and returns a new array of the same length with the squares
#   of the original integers also sorted in ascending order.
def sortedSquaredArray(array):
    result = [int(i)*int(i) for i in array]
    return sorted(result)


print(sortedSquaredArray(input().split(' ')))
