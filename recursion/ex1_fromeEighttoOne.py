# ex 1


def natural_numbers(n: int):
    '''
    A recursive function prints first n natural numbers
    '''
    if n < 1:
        print("Error: please choose a natural number.")
    elif n == 1:
        print(n, end=" ")
    else:
        print(n, end=", ")
        natural_numbers(n-1)


if __name__ == "__main__":
    n = int(input("Please enter a natural number: "))
    natural_numbers(n)
