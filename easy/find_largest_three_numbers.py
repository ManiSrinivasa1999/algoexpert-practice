"""

  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.

  The function should return duplicate integers if necessary; for example, it
  should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12]
  
"""
def findThreeLargestNumbers(array):
    res = []
    m1 = max(array)
    array.remove(m1)
    m2 = max(array)
    array.remove(m2)
    m3 = max(array)
    array.remove(m3)
    if m1 <= m2 and m1 <= m3:
        res.append(m1)
        if m2 <= m3:
            res.append(m2)
            res.append(m3)
        else:
            res.append(m3)
            res.append(m2)
    elif m2 <= m3 and m2 <= m1:
        res.append(m2)
        if m1 <= m3:
            res.append(m1)
            res.append(m3)
        else:
            res.append(m3)
            res.append(m1)
    elif m3 <= m2 and m3 <= m1:
        res.append(m3)
        if m2 <= m1:
            res.append(m2)
            res.append(m1)
        else:
            res.append(m1)
            res.append(m2)
    return res
print(findThreeLargestNumbers(list(map(int, input().split()))))