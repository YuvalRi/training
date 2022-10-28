# ex 4

def string_reverse(str: str):
    '''
    A recursive function which reverses a string
    '''
    if len(str) == 0:
        return str
    else: 
        return str[0] + string_reverse(str[1:])

if __name__ == "__main__":
    str = input("Please enter a string: ")
    print(string_reverse(str))
