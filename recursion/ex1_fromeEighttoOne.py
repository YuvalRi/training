# ex 1


def naturalNumbers(n: int):
    '''
    A recursive function prints first n natural numbers
    '''
    if n < 1:
        print("Error: please choose a natural number.")
    elif n == 1:
        print(n, end = " ")
    else:
        print(n, end = ", ")
        naturalNumbers(n-1)


if __name__ == "__main__":
    n = int(input("Please enter a natural number: "))
    naturalNumbers(n)
