def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    startIndex = 0
    longest = [0, 1]
    for i, char in enumerate(string):
        if char in lastSeen:
            startIndex = max(startIndex, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIndex:
            longest = [startIndex, i + 1]
        lastSeen[char] = i
    return string[longest[0]:longest[1]]
