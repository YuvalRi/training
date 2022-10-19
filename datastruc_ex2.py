# ex 2

def smallestElement(lst):
    '''
    A function that recieves a list of integers and returns its smallest element
    '''
    if len(lst) == 0:
        print("Error. Please enter at least one element in the list")
    else:
        smallest = lst[0]
        for ele in lst:
            if ele < smallest:
                smallest = ele
        return smallest


if __name__ == "__main__":
    print(smallestElement([]))
