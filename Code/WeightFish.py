'''function'''
def weightfish():
    '''solution'''
    numlist = []
    while True:
        num = int(input())
        if num == 0:
            break
        numlist.append(num)
    condition = input().lower()

    if condition == "min":
        for i in range(len(numlist)):
            min_index = i
            for j in range(i+1, len(numlist)):
                if numlist[j] < numlist[min_index]:
                    min_index = j
            numlist[i], numlist[min_index] = numlist[min_index], numlist[i]
    elif condition == "max":
        for i in range(len(numlist)):
            max_index = i
            for j in range(i+1, len(numlist)):
                if numlist[j] > numlist[max_index]:
                    max_index = j
            numlist[i], numlist[max_index] = numlist[max_index], numlist[i]

    for num in numlist:
        print(num, end=" ")

weightfish()
