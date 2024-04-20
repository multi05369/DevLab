'''function'''
def plusreverse(num1, num2):
    '''solution'''
    res = num1 + num2
    for i in reversed(str(res)):
        print(i, end="")

plusreverse(int(input()), int(input()))
