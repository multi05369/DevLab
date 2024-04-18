'''function'''
def reversesorting(num):
    '''solution'''
    numlist = []
    for _ in range(num):
        number = int(input())
        numlist.append(number)
    for i in reversed(numlist):
        print(i)

reversesorting(int(input()))
