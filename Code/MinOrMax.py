'''function'''
def checkMinMax(numA, numB):
  '''solution'''
  if numA > numB:
    print("A")
  elif numB > numA:
    print("B")
  else:
    print("AB")

checkMinMax(int(input()), int(input()))
