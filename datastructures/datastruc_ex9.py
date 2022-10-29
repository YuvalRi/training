# ex 9

def dimenstionaList(m: int, n: int):
    '''
    A function which recieves 2 integers
    and returns a 2-dimensional list of size mXn
    '''
    list1 = []
    lists = []
    for i in range(m):
        lists.append(list1)
    for i in range(m):
        for j in range(m):
            lists[j] = [i*j for i in range(n)]
    return lists


if __name__ == "__main__":
    print(dimenstionaList(4, 5))
    print(dimenstionaList(18, 5))
    print(dimenstionaList(2, 3))
