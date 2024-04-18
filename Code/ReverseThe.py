'''function'''
def reversetext(text):
    '''solution'''
    word = text.split(" ")
    for i in reversed(word):
        print(i, end=" ")

reversetext(input())
