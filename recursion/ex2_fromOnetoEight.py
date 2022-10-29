# ex 2

def natural_numbers_backward(n: int):
    '''
    A recursive function prints first n natural numbers
    in reverse order
    '''
    if n < 1:
        print("Error: please choose a natural number.")
    elif n == 1:
        print(n, end=", ")
    else:
        natural_numbers_backward(n-1)
        print(n, end=", ")


if __name__ == "__main__":
    n = int(input("Please enter a natural number: "))
    natural_numbers_backward(n)
