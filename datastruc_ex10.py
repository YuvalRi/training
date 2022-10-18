# ex 10

def freqDict(s: str):
    '''
    A function which creates a frequency dictionary from a string
    '''
    all_freq = {}
    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq


def cyclicShift(str1: str, str2: str):
    '''
    A function which recieves 2 strings and returns
    True is str2 is a "cyclic shift" of str1 and False otherwise
    '''
    temp = ''
    if freqDict(str1) != freqDict(str2):
        return False
    temp = str1 + str1
    if (temp.count(str2) > 0):
        return True
    else:
        return False


if __name__ == "__main__":
    cyclicShift(str1="happy", str2="ppyha")
    cyclicShift(str1="happy", str2="pypha")
    cyclicShift(str1="YYY", str2="YYYY")
    cyclicShift(str1="OFEK", str2="OFEK")
    cyclicShift(str1="", str2="OFEK")

