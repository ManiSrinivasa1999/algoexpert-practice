def rightSmallerThan(array):
    res = []
    for i in range(len(array)):
        temp = 0
        for j in array[i:]:
            if array[i] > j:
                temp += 1
        res.append(temp)
    return res
