# ex 2

def naturalNumbers_backward(n: int):
    '''
    A recursive function prints first n natural numbers
    in reverse order
    '''
    if n < 1:
        print("Error: please choose a natural number.")
    elif n == 1:
        print(n, end = ", ")
    else:
        naturalNumbers_backward(n-1)
        print(n, end = ", ")

    
if __name__ == "__main__":
    n = int(input("Please enter a natural number: "))
    naturalNumbers_backward(n)
