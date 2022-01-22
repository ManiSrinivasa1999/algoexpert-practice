def shiftedBinarySearch(array, target):
    for i in range(len(array)):
        if target == array[i]:
            return i
    return -1