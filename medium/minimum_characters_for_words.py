def minimumCharactersForWords(words):
    res = []
    for i in words:
        temp = []
        for j in i:
            if j not in res:
                for _ in range(i.count(j)):
                    res.append(j)
    for i in words:
        for j in i:
            if i.count(j) != res.count(j):
                for _ in range(i.count(j) - res.count(j)):
                    res.append(j)
    return res
