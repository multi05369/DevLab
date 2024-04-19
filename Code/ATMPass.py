'''function'''
def atmpass(text):
    '''solution'''
    res = ""
    passwd = 0
    for i in text:
        if not i.isdigit():
            i = "_"
        res += i

    for i in res.split("_"):
        if i.isdigit():
            passwd += int(i)
    print(f"{passwd:04d}")

atmpass(input())
