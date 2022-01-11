def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    waitingTime = 0
    for i in range(len(queries)):
        waitingTime += queries[i] * (len(queries) - 1 - i)
    return waitingTime


print(minimumWaitingTime(list(map(int, input().split()))))
