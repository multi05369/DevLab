'''function'''
def calculategrade(score):
  '''solution'''
  if 80 <= score <= 100:
    print("A")
  elif 70 <= score <= 79:
    print("B")
  elif 60 <= score <= 69:
    print("C")
  elif 50 <= score <= 59:
    print("D")
  else:
    print("F")

calculategrade(int(input()))
