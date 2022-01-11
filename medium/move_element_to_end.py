def moveElementToEnd(array, toMove):
    count = array.count(toMove)
    res = []
    for i in array:
        if i != toMove:
            res.append(i)
    for i in range(count):
        res.append(toMove)
    return res


print(moveElementToEnd(list(map(int, input().split())), int(input())))
