'''function'''
def calculategradetwo(tscore, mscore, escore, sscore, spscore):
  '''solution'''
  print("THAI = %.1f" % tscore)
  print("MATH = %.1f" % mscore)
  print("ENGLISH = %.1f" % escore)
  print("SCIENCE = %.1f" % sscore)
  print("SPORT = %.1f" % spscore)
  print("---")
  print("GPA = %.1f" % ((tscore + mscore + escore + sscore + spscore) / 5))

calculategradetwo(float(input()), float(input()), \
          float(input()), float(input()), float(input()))
