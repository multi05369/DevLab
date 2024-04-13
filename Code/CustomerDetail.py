'''function'''
def customerdetail(firstname, surname, address, gender, tel):
  '''solution'''
  print("--- Customer Detail ---")
  print("Name : %s %s" % (firstname, surname))
  print("Address : %s" % address)
  print("Gender : %s" % gender)
  print("Tel : %s" % tel)

customerdetail(str(input()), str(input()), str(input()), \
               str(input()), str(input()))
