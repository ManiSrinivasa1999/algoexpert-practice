"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4]  form a subsequence of the array
  [1, 2, 3, 4] , and so do the numbers [2, 4]
  Note:
  that a single number in an array and the array itself are both valid
  subsequences of the array.
"""
def isValidSubsequence(array, sequence):
    arrIndex = 0
    seqIndex = 0
    while arrIndex < len(array) and seqIndex < len(sequence):
        if array[arrIndex] == sequence[seqIndex]:
            seqIndex += 1
        arrIndex += 1
    return seqIndex == len(sequence)
print(isValidSubsequence(list(map(int, input().split())),list(map(int, input().split()))))