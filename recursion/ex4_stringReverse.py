# ex 4

def stringReverse(str: str):
    '''
    A recursive function which reverses a string
    '''
    if len(str) == 0:
        print("Error! please enter at least one character.")
    elif len(str) == 1:
        return str
    else: 
        return stringReverse(str[-(len(str)-1):]) + str[0]

if __name__ == "__main__":
    str = str(input("Please enter a string: "))
    print(stringReverse(str))
