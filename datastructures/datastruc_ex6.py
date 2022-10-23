# ex6

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


if __name__ == "__main__":
    print(freqDict("yuvalritsker"))
    print(freqDict("ofekshmuel"))
    print(freqDict("chugokujin"))
