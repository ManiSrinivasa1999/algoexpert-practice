def searchForRange(array, target):
    res = []
    for i in range(len(array)):
        if array[i] == target:
            res.append(i)
            break
    if array.count(target) == 1:
        res.append(res[0])
        return res
    if not res:
        return [-1, -1]
    else:
        res.append(array.count(target) + res[0] - 1)
    return res
