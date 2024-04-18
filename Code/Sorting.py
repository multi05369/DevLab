'''function'''
def sorting():
    '''solution'''
    numlist = []
    for _ in range(5):
        num = int(input())
        numlist.append(num)
    numlist.sort()
    for i in reversed(numlist):
        print(i)

sorting()
