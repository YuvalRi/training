from datastructures.datastruc_ex6 import freqDict

# ex 8


def createdFrom(dict: dict, s: str):
    '''
    A function which returns True if the received string can be created from
    the characters available in the given dictionary and False otherwise
    '''
    for c in s:
        if c not in dict.keys() or dict[c] == 0:
            return False
        else:
            dict[c] -= 1
    return True


if __name__ == "__main__":
    print(createdFrom(freqDict("yuvalritsker"), s="value"))
    print(createdFrom(freqDict("yuvalritsker"), s="batumi"))
    print(createdFrom(freqDict("yuvalritsker"), s="yrrr"))
