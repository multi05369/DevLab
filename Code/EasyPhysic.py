'''function'''
def physic(distant, time):
  '''solution'''
  velocity = distant / time
  print("%d km/h" % velocity)

physic(int(input()), int(input()))
