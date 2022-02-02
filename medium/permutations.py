def getPermutations(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]
    res = []
    for i in range(len(array)):
        ele = array[i]
        remList = array[:i] + array[i + 1:]
        for perm in getPermutations(remList):
            res.append([ele] + perm)
    return res
