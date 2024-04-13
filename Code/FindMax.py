'''function'''
def findmax():
  '''solution'''
  numlist = []
  for _ in range(3):
    num = int(input())
    numlist.append(num)
  print("MAX : %d" % max(numlist))

findmax()
