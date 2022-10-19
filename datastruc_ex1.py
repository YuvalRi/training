# ex1

def elementSum(lst: list):
    '''
    A function that recieves a list and returns the sum of its elements
    '''
    lst_sum = 0
    for i in range(len(lst)):
        lst_sum += lst[i]
    return lst_sum


if __name__ == "__main__":
    print(elementSum([1, 2]))
