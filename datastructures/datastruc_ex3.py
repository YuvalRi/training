# ex 3

def checkLen(s: str):
    '''
    A function which checks if the given string is larger than 2
    '''
    if len(s) > 2:
        return True


def firstandLast(s: str):
    '''
    A function which checks if both first and last characters are the same
    '''
    if len(s) == 0:
        print("Error: the given string is empty!")
    elif s[0] == s[-1]:
        return True


def numofString(lst: list):
    '''
    A function which returns the number of string which follows the conditions above
    '''
    counter = 0
    for st in lst:
        if checkLen(st) and firstandLast(st):
            counter = counter + 1
    print(counter)


if __name__ == "__main__":
    lst = ["", "aa", "Yuval", "11", "1451", "OfekO", "LocaL"]
    numofString(lst)
