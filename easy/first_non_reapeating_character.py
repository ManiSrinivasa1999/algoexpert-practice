"""

  Write a function that takes in a string of lowercase English-alphabet letters
  and returns the index of the string's first non-repeating character.
  The first non-repeating character is the first character in a string that
  occurs only once.
  If the input string doesn't have any non-repeating characters, your function
  should return -1
"""


def firstNonRepeatingCharacter(string):
    for i in range(len(string)):
        tempString = string[i]
        if tempString in string[i+1:] or tempString in string[0:i]:
            print(string[i:])
            continue
        else:
            return i
    return -1


print(firstNonRepeatingCharacter(input()))
