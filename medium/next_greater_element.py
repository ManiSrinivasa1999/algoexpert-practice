def nextGreaterElement(array):
    res = [-1] * len(array)
    stack = []

    for i in range(2 * len(array)):
        circularIndex = i % len(array)

        while len(stack) > 0 and array[stack[len(stack) -
                                             1]] < array[circularIndex]:
            top = stack.pop()
            res[top] = array[circularIndex]
        stack.append(circularIndex)
    return res
