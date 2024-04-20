'''function'''
import ast
def lencheck(text1, text2):
    '''solution'''
    res1 = len(text1)
    res2 = len(text2)
    if res2 > res1:
        res1, res2 = res2, res1
    print(res1)
    print(res2)

lencheck(str(input()), str(input()))
