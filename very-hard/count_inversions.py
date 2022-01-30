def countInversions(array):
    res = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                res += 1
    return res
