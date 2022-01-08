def threeNumberSort(array, order):
  array.sort()
  res = []
  for i in order:
    for _ in range(array.count(i)):
      res.append(i)
  return res
