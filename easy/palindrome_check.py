'''
  Write a function that takes in a non-empty string and that returns a boolean
  representing whether the string is a palindrome.

  A palindrome is defined as a string that's written the same forward and
  backward. Note that single-character strings are palindromes.
'''
def isPalindromeMethodOne(string):
	revStr = ''
	for i in range(len(string)-1, -1, -1):
		revStr += string[i]
	return revStr == string
def isPalindromeMethodTwo(string):
	return string == string[::-1]
print(isPalindromeMethodTwo(input()))
