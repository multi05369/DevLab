'''function'''
def easyfizzbuzz(num):
    '''solution'''
    if num % 3 == 0 and num % 2 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 2 == 0:
        print("Buzz")

easyfizzbuzz(int(input()))
