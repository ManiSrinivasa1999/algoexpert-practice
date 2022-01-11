def binarySearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


print(binarySearch(list(map(int, input().split())), int(input())))
