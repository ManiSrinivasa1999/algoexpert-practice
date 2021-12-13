def tournamentWinner(competitions, results):
    scores = {}
    for i in range(len(results)):
        if results[i] == 0:
            if competitions[i][1] not in scores: 
                scores[competitions[i][1]] = 3
            else:
                scores[competitions[i][1]] += 3
        else:
            if competitions[i][0] not in scores: 
                scores[competitions[i][0]] = 3
            else:
                scores[competitions[i][0]] += 3
    keysList = list(scores.keys())
    valuesList = list(scores.values())
    maxValue = max(valuesList)
    index = 0
    for i in range(len(results)):
        if valuesList[i] == maxValue:
            index += i
            break
    return keysList[index]
print(tournamentWinner(input().split(), list(map(int, input().split()))))
