# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth = 1):
  sum = 0
  for i in array:
    if type(i) is list:
      sum += productSum(i, depth + 1)
    else:
      sum += i
  return sum * depth
