'''function'''
def calculategradetwo(score):
    '''solution'''
    if 0 <= score <= 100:
        if score >= 90:
            print("A")
        elif 85 <= score <= 89:
            print("B+")
        elif 80 <= score <= 84:
            print("B")
        elif 75 <= score <= 79:
            print("C+")
        elif 70 <= score <= 74:
            print("C")
        elif 65 <= score <= 69:
            print("D+")
        elif 60 <= score <= 64:
            print("D")
        else:
            print("F")
    elif score > 100:
        print("Error : Value must be less than or equal to 100.")
    else:
        print("Error : Value must be greater than or equal to 0.")

calculategradetwo(int(input()))
