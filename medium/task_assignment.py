def findIndexValue(value, tasks, tempIndices):
    for i in range(len(tasks)):
        if tasks[i] == value and i not in tempIndices:
            return i


def taskAssignment(k, tasks):
    # Write your code here.
    tempTasks = sorted(tasks)
    total = sum(tasks)/len(tasks)
    res = []
    tempIndices = []
    for i in range(len(tasks)//2):
        temp = []
        index1 = findIndexValue(tempTasks[i], tasks, tempIndices)
        index2 = findIndexValue(
            tempTasks[len(tasks) - i - 1], tasks, tempIndices)
        tempIndices.append(index1)
        tempIndices.append(index2)
        res.append([index1, index2])
    return res
