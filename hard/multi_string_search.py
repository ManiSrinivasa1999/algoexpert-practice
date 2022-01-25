def multiStringSearch(bigString, smallStrings):
    res = []
    for i in smallStrings:
        if i in bigString:
            res.append(True)
        else:
            res.append(False)
    return res
