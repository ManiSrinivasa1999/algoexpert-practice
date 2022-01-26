def mergeSortedArrays(arrays):
    res = []
    for array in arrays:
        for element in array:
            res.append(element)
    return sorted(res)
