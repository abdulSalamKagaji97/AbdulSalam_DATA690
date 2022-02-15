
def min(integers):
  min = integers[0]
  for x in integers:
    if min > x:
      min = x
  return min
