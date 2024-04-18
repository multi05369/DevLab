'''function'''
def reversetext(text):
    '''solution'''
    for i in reversed(text):
        print(i, end="")

reversetext(str(input()))
