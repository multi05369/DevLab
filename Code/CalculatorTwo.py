'''function'''
def sommaicalculator(num):
  '''solution'''
  res = 0
  for i in range(num):
    item = int(input())
    res += item
  print("%d THB" % res)

sommaicalculator(int(input()))
