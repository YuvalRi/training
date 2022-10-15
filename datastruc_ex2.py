# ex 2

def smallestElement(lst):
    '''
    function that recieves a list of integers and returns its smallest element
    '''
    if len(lst) == 0:
        print("Error. Please enter at least one element in the list")
    else:
        smallest = lst[0]
        for i in lst:
            if i < smallest:
                smallest = i
        return smallest


if __name__ == "__main__":
    print(smallestElement([]))
