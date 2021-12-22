def generateDocument(characters, document):
  characters = list(characters)
  for i in document:
    if i in characters:
      characters.remove(i)
      continue
    else:
      return False
  return True
print(generateDocument(input(), input()))
