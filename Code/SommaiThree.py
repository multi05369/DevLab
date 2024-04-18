'''function'''
def sommaithree(num):
    '''solution'''
    customer = {}
    for _ in range(num):
        name = input()
        born = int(input())
        gender = input()
        customer[name] = {'Born' : born, 'Gender' : gender}
    print("--Customers Information--")
    for i, j in customer.items():
        print(f"{i} (age : {2017 - int(j['Born'])})")

sommaithree(int(input()))
