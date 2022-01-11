def reverseWordsInString(string):
	res = []
	index = 0
	for i in range(len(string)):
		char = string[i]
		if char == ' ':
			res.append(string[index:i])
			index = i
		elif string[index] == " ":
			res.append(' ')
			index = i
	res.append(string[index:])
	reverseList(res)
	return ''.join(res)

def reverseList(words):
	start, end = 0, len(words) - 1
	while start < end:
		words[start], words[end] = words[end], words[start]
		start += 1
		end -= 1
	return words
