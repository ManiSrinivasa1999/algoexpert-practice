def indexEqualsValue(array):
    for i in range(len(array)):
        if i == array[i]:
            return i
    return -1
