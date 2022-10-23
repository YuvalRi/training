# ex1
def func(n: int):
    '''
    A function which prints all the numbers from 1 to n 
    in seperate lines and print the function's return value
    '''
    for i in range(n):
        print(i)
    return "finished"


# ex2
def fun(n: int):
    '''
    A function which prints 3 different sequences
    '''
    # first required sequence
    print("First sequence:\n", end=" ")
    print(1, end="")
    for i in range(2, n+1, 2):
        print(f", {i}", end="")
    # second required sequence
    print("Second sequence:\n", end=" ")
    print(1, end="")
    for i in range(n+1):
        # converting the first element into '1'
        if i == 0:
            print("Second sequence:\n", 1, end=" ")
        # the other elements are the powerset of 2
        elif 2**i <= (n+1):
            print(2**i, end=" ")
    # first two elements in the required sequence
    n1, n2 = 1, 1
    # check if the number typed is valid
    if n <= 0:
        print("Please enter a positive integer")
    # if the int equals to 1, return 1 only
    elif n == 1:
        print("Fibbonacci sequence upto", n, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Third sequence:\n", end=" ")
        while n1 < (n+1):
            print(n1, end=" ")
            temp = n1 + n2
            n1 = n2
            n2 = temp


# ex3

def pali(n: int):
    '''
    A function that receives a number n
    and returns True if n is a palindrome and False otherwise
    '''
    # a single digit number is a palindrome
    if len(str(n)) == 1:
        return True
    # check if n is a palindrome
    temp = n
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = (rev*10) + rem
        temp = temp // 10
    if n == rev:
        return True
    # n is unnegative, but it is not a palindrome
    else:
        return False

# ex 4 - main program that receives a number from the user between 1-3.
# Each number represents one of the functions above


if __name__ == "__main__":
    var = int(input("Enter a number between 1-3:"))
    match var:
        case 1:
            print(func(100))
        case 2:
            fun(100)
        case 3:
            print(pali(100))
        case other:
            print('No match found')
