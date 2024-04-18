'''function'''
def sumnumber(numtext):
    '''solution'''
    res = 0
    for i in numtext:
        res += int(i)
    if len(str(res)) != 1:
        return sumnumber(str(res))
    else:
        return res

print(sumnumber(str(input())))
