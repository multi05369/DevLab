'''function'''
def findnumber(num):
    '''solution'''
    numlist = input().split(" ")
    find = int(input())
    print("Yes" if str(find) in numlist else "No")

findnumber(int(input()))
