"""
  Given a non-empty string of lowercase letters and a non-negative integer
  representing a key, write a function that returns a new string obtained by
  shifting every letter in the input string by k positions in the alphabet,
  where k is the key. 
  Note that letters should "wrap" around the alphabet; in other words, the z  shifted by one returns the letter a

"""
def caesarCipherEncryptor(string, key):
    array = []
    key = key%26
    for i in string:
        temp = ord(i)
        if temp+key > 122:
            array.append(chr(temp+key - 26))
        else:
            array.append(chr(temp+key))		
    return ''.join(array)
print(caesarCipherEncryptor(input(), int(input())))
