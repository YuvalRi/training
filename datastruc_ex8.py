import math

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
    lst = []
    for c in s:
        lst.append(c)
    new_lst = lst.copy()
    for s in lst:
        if s in dict.keys() and dict[s] > 0:
            dict[s] = dict[s] - 1
            t = new_lst.index(s)
            new_lst.pop(t)
    if len(new_lst) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(createdFrom(freqDict("yuvalritsker"), s="value"))
    print(createdFrom(freqDict("yuvalritsker"), s="batumi"))
    print(createdFrom(freqDict("yuvalritsker"), s="yrrr"))
