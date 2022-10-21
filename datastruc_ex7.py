import random as rnd
from datastruc_ex6 import *

# ex7
# a


def wordSelected(n: int, random: bool, lst: list):
    '''
    A function which returns selected words from the WordData.txt file
    according to conditions explained in the exercise
    '''
    with open('WordData.txt', 'r') as file:
        allText = file.read()
        text_list = allText.split('\n')
        selected_words = []
        if random:
            randomlist = rnd.sample(range(0, len(text_list)), n)
        else:
            randomlist = lst
        for i in range(len(randomlist)):
            selected_words.append(text_list[randomlist[i]])
        return selected_words


# b


def fromLlistToString(lst: list):
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
    '''
    A function which returns the median value of the given dictionary
    '''
    new_lst = sorted(dict.values())
    if (len(new_lst)) % 2 == 0:
        med1 = new_lst[(len(new_lst))//2]
        med2 = new_lst[(len(new_lst))//2 - 1]
        med = (med1 + med2)/2
    else:
        med = new_lst[(len(new_lst))//2]
    return med


def finalFunction(n: int, random: bool, lst: list):
    '''
    A function which returns all required values
    '''
    a = wordSelected(n, random, lst)
    b = fromLlistToString(a)
    c = freqDict(b)
    d = maxCharacter(c)
    e = findMedian(c)
    return c, d, e


if __name__ == "__main__":
    print(
        "The frequency dictionary is:",
        finalFunction(7, True, lst=[1, 2, 3, 4, 5, 6, 7])[0],
        "\nThe most common character is:",
        finalFunction(7, True, lst=[1, 2, 3, 4, 5, 6, 7])[1],
        "\nThe median is:",
        finalFunction(7, True, lst=[1, 2, 3, 4, 5, 6, 7])[2])
    print(
        "The frequency dictionary is:",
        finalFunction(5, False, lst=[1, 2, 3, 4, 5, 6, 7])[0],
        "\nThe most common character is:",
        finalFunction(5, False, lst=[1, 2, 3, 4, 5, 6, 7])[1],
        "\nThe median is:",
        finalFunction(5, False, lst=[1, 2, 3, 4, 5, 6, 7])[2])

