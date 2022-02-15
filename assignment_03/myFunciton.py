
def min(integers):
  min = integers[0]
  for x in integers:
    if min > x:
      min = x
  return min

def max(integers):
  max = integers[0]
  for x in integers:
    if max < x:
      max = x
  return max
