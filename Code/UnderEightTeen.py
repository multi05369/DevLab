'''function'''
def countage(name, age):
    '''solution'''
    if 2021 - age > 18 or name == "A A":
        print("Welcome %s to NongGipsy Pub" % name)
    else:
        print("You shall not pass!")

countage(input(), int(input()))
