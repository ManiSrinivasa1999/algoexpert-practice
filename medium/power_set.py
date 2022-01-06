def powerset(array):
  res = [[]]
  for i in array:
    for j in range(len(res)):
      currentSubset = res[j]
      res.append(currentSubset + [i])
  return res