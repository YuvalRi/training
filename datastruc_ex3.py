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
    if s != "" and s[0] == s[-1]:
        return True


def numofString(lst: list):
    '''
    A function which returns the number of string which follows the conditions above
    '''
    counter = 0
    for i in lst:
        if checkLen(i) and firstandLast(i):
            counter = counter + 1
    print(counter)


if __name__ == "__main__":
    lst = ["", "aa", "Yuval", "11", "1451", "OfekO", "LocaL"]
    numofString(lst)
