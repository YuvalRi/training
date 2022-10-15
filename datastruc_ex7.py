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
            return selected_words
        else:
            text_list = allText.split('\n')
            selected_words = []
            for i in range(len(lst)):
                selected_words.append(text_list[lst[i]])
            return selected_words


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


def freqFunc(lst: list):
    '''
    A function which convert list of strings to one string
    '''
    new_string = "".join(lst)
    return new_string


def maxCharacter(dict: dict):
    '''
    A function which returns the maximum value in a given dictionary
    '''
    max_value = max(dict, key=dict.get)
    return max_value


def findMedian(dict: dict):
    new_lst = sorted(dict.values())
    if (len(new_lst)) % 2 == 0:
        med1 = new_lst[(len(new_lst))//2]
        med2 = new_lst[(len(new_lst))//2 - 1]
        med = (med1 + med2)/2
        return med
    else:
        med = new_lst[(len(new_lst))//2]
        return med


if __name__ == "__main__":
    # in this case random = True
    a = freqDict(freqFunc(func(7, True, lst=[1, 2, 3, 4, 5, 6, 7])))
    print(a)
    print(maxCharacter(a))
    print(findMedian(a))
    # in this case random = False
    b = freqDict(freqFunc(func(5, False, lst=[1, 2, 3, 4, 5])))
    print(b)
    print(maxCharacter(b))
    print(findMedian(b))

