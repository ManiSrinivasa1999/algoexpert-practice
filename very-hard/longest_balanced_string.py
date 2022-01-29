def longestBalancedSubstring(string):
    maxLength = 0
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1, 2):
            if isBalanced(string[i:j]):
                currentLength = j - i
                maxLength = max(maxLength, currentLength)
    return maxLength


def isBalanced(string):
    openParensStack = []

    for char in string:
        if char == '(':
            openParensStack.append('(')
        elif len(openParensStack) > 0:
            openParensStack.pop()
        else:
            return False
    return len(openParensStack) == 0
