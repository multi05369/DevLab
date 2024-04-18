'''function'''
def thepassword(password):
    '''solution'''
    if 3 <= len(password) <= 20:
        has_upper = any(i.isupper() for i in password)
        has_lower = any(i.islower() for i in password)
        has_number = any(i.isdigit() for i in password)
        has_special = any(i in "!@#$%^&*()_+-=[]{};':\",.<>/?\\" for i in password)
        if has_upper and has_lower and has_number and has_special:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

thepassword(str(input()))
