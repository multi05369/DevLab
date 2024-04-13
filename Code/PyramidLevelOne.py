'''function'''
def pyramid(num):
  '''solution'''
  for i in range(num):
    for _ in range(i + 1):
      print("*", end="")
    print()

pyramid(int(input()))
