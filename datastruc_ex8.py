# ex 8


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
