from datastruc_ex6 import freqDict

# ex 10

# a
# option 1


def cyclicShift(str1: str, str2: str):
    '''
    A function which recieves 2 strings and returns
    True is str2 is a "cyclic shift" of str1 and False otherwise
    '''
    if freqDict(str1) != freqDict(str2):
        return False
    temp = str1 + str1
    if (temp.count(str2) > 0):
        return True
    else:
        return False

# option 2


def rotate(str: str, d: int):
    '''
    A function which returns a new string shifted by d length
    '''
    first = str[0: len(str)-d]
    second = str[len(str)-d:]
    return second + first


def cyclicShift2(str1: str, str2: str):
    '''
    A function which recieves 2 strings and returns
    True is str2 is a "cyclic shift" of str1 and False otherwise
    '''
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if rotate(str1, i) == str2:
            return True
    return False

# b


def get_shifts(str1: str, str2: str):
    '''
    A function which returns the number of shifts
    required to reach str2 from str1
    '''
    for i in range(len(str1)):
        if rotate(str1, i) == str2:
            return i
    return -1


if __name__ == "__main__":
    # 5 examples of option 1
    print(cyclicShift(str1="happy", str2="ppyha") is True)
    print(cyclicShift(str1="happy", str2="pypha") is False)
    print(cyclicShift(str1="YYY", str2="YYYY") is False)
    print(cyclicShift(str1="OFEK", str2="OFEK") is True)
    print(cyclicShift(str1="", str2="OFEK") is False)
    # 5 examples of option 2
    print(cyclicShift2(str1="happy", str2="ppyha") is True)
    print(cyclicShift2(str1="happy", str2="pypha") is False)
    print(cyclicShift2(str1="YYY", str2="YYYY") is False)
    print(cyclicShift2(str1="OFEK", str2="OFEK") is True)
    print(cyclicShift2(str1="", str2="OFEK") is False)
    # 3 examples of b
    print(get_shifts("ofek", "kofe") == 1)
    print(get_shifts("kofe", "ofek") == 3)
    print(get_shifts("Alon", "ofek") == -1)
