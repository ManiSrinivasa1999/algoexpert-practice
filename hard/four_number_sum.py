def fourNumberSum(array, targetSum):
    res = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                for l in range(k + 1, len(array)):
                    if array[i] + array[j] + array[k] + array[l] == targetSum:
                        res.append([array[i], array[j], array[k], array[l]])
    return res
