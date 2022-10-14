# ex 2

def smallestElement(lst):
    '''
    function that recieves a list of integers and returns its smallest element
    '''
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest


if __name__ == "__main__":
    print(smallestElement([-1, -5, -99, 100, -1500]))
