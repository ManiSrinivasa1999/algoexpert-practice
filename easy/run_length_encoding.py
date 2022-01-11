def runLengthEncoding(string):
    res = {}
    for i in string:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    resultKeys = list(res.keys())
    resultValues = list(res.values())
    result = []
    for i in range(len(resultKeys)):
        if resultValues[i] > 9:
            for _ in range(resultValues[i]//9):
                result.append(str(9))
                result.append(resultKeys[i])
            result.append(str(resultValues[i] % 9))
            result.append(resultKeys[i])
        else:
            result.append(str(resultValues[i]))
            result.append(resultKeys[i])
    return ''.join(result)


print(runLengthEncoding(input()))
