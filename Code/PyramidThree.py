'''function'''
def pyramid(num):
    '''solution'''
    for i in range(1, num + 1):
        for _ in range(i, num):
            print("", end=" ")
        for _ in range(1, i):
            print("*", end="")
        for _ in range(i, 0, -1):
            print("*", end="")
        print()
    for i in range(num - 1, 0, -1):
        for _ in range(i, num):
            print("", end=" ")
        for _ in range(1, i + 1):
            print("*", end="")
        for _ in range(i - 1, 0, -1):
            print("*", end="")
        print()

pyramid(int(input()))
