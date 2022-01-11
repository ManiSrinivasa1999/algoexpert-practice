def searchInSortedMatrix(matrix, target):
    rowIndex = 0
    for row in matrix:
        rowIndex += 1
        colIndex = 0
        for col in row:
            colIndex += 1
            if target == col:
                return [rowIndex - 1, colIndex - 1]
    return [-1, -1]
