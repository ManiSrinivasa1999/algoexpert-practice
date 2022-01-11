"""
  Write a function that takes in a non-empty array of integers and returns an
  array of the same length, where each element in the output array is equal to
  the product of every other number in the input array.

  In other words, the value at output[i] is equal to the product of
  every number in the input array other than input[i]"""


def arrayOfProducts(array):
    res = []
    for i in range(0, len(array)):
        temp = []
        for k in range(0, len(array)):
            if k != i:
                temp.append(array[k])
        mul = 1
        for j in temp:
            mul *= j
        res.append(mul)
    return res


print(arrayOfProducts(list(map(int, input().split()))))
