import random as rnd
from datastruc_ex6 import freqDict

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
            new_lst = rnd.sample(range(0, len(text_list)), n)
        else:
            new_lst = lst
        for i in range(len(new_lst)):
            selected_words.append(text_list[new_lst[i]])
        return selected_words


# b


def fromListToString(lst: list):
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


def dataFunction(n: int, rand: bool, lst: list):
    '''
    A function which returns all required values
    '''
    dictofreq = freqDict(fromListToString(wordSelected(n=n,
                                                       random=rand,
                                                       lst=lst)))
    print(f'The frequency dictionary is: {dictofreq}\
    \nThe most common character is: {maxCharacter(dictofreq)}\
    \nThe median value is: {findMedian(dictofreq)}')
    #print(
        #f'''The frequency dictionary is: {dictofreq}
        #The most common character is: {maxCharacter(dictofreq)}
        #The median value is: {findMedian(dictofreq)}''')


if __name__ == "__main__":
    dataFunction(7, True, lst=[1, 2, 3, 4, 5, 6, 7])
    dataFunction(5, False, lst=[1, 2, 3, 4, 5])
