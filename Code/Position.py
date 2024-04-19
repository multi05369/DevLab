'''function'''
def findposition(num):
    '''solution'''
    itemlist = []
    res = []
    for _ in range(num):
        item = int(input())
        itemlist.append(item)
    find = int(input())
    for i in range(len(itemlist)):
        if itemlist[i] == find:
            res.append(str(i + 1))
    if res:
        print("Position:", ",".join((res)))
    else:
        print("Not found")

findposition(int(input()))
