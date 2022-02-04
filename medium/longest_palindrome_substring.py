def longestPalindromicSubstring(string):
    longestString = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if len(substring) > len(longestString) and isPalindrome(substring):
                longestString = substring
    return longestString


def isPalindrome(string):
    rightIndex = len(string) - 1
    leftIndex = 0
    while leftIndex < rightIndex:
        if string[leftIndex] != string[rightIndex]:
            return False
        rightIndex -= 1
        leftIndex += 1
    return True
