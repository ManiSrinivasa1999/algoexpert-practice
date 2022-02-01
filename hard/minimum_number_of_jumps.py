def minNumberOfJumps(array):
    count = 0
    startIndex = 0
    lastIndex = len(array) - 1
    while startIndex < lastIndex:
        for i in range(len(array) - 1):
            startIndex += array[i]
            if startIndex < len(array) - 1:
                array = array[startIndex:]
        count += 1
    return count
