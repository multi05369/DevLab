'''function'''
def sorting(num):
  '''solution'''
  numlist = []
  for _ in range(num):
    item = int(input())
    numlist.append(item)
  for i in sorted(numlist, reverse=True):
    print(i)

sorting(int(input()))
