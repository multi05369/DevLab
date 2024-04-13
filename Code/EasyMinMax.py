'''function'''
def minormax(xnum, mnum):
  '''solution'''
  if xnum < mnum:
    xnum, mnum = mnum, xnum
  print("MAX : %d" % xnum)
  print("MIN : %d" % mnum)

minormax(int(input()), int(input()))
