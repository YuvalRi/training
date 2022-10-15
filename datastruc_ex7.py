import random as rnd

# ex7
# a


def func(n: int, random: bool, lst: list):
    with open('WordData.txt', 'r') as file:
        allText = file.read()
        if random:
            text_list = allText.split('\n')
            randomlist = rnd.sample(range(0, len(text_list)), n)
            selected_words = []
            for i in range(len(randomlist)):
                selected_words.append(text_list[randomlist[i]])
            print(selected_words)
        else:
            text_list = allText.split('\n')
            selected_words = []
            for i in range(len(lst)):
                selected_words.append(text_list[lst[i]])
            print(selected_words)


if __name__ == "__main__":
    func(7, True, lst=[1, 2, 3, 4, 5, 6, 7])
    func(5, False, lst=[1, 2, 3, 4, 5])

# b

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
