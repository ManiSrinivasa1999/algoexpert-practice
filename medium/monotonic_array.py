def isMonotonic(array):
  if len(array) > 1:
    if sorted(array) == array:
      isIncOrDec = 'I'
    else:
      isIncOrDec = 'D'
  else:
    return True
  for i in range(len(array)-1):
    if array[i] <= array[i+1] and isIncOrDec == 'I':
      continue
    elif array[i] >= array[i+1] and isIncOrDec == 'D':			
      continue
    else:
      return False
  return True
print(isMonotonic(list(map(int, input().split()))))			
