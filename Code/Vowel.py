'''function'''
def deletevowel(text):
    '''solution'''
    res = ""
    for i in text:
        if i in "aeiouAEIOU":
            pass
        else:
            res += i
    print(res)

deletevowel(input())
