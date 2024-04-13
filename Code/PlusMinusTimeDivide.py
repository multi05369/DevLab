'''function'''
def plusminustimedivide(num1, num2):
  '''solution'''
  print("%d + %d = %d" % (num1, num2, num1 + num2))
  print("%d - %d = %d" % (num1, num2, num1 - num2))
  print("%d * %d = %d" % (num1, num2, num1 * num2))
  print("%d / %d = %d" % (num1, num2, num1 / num2))

plusminustimedivide(int(input()), int(input()))
