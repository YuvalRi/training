#program to print first n natural numbers using recursion

def natural_recursive(n):
    if n <= 0:
         return "Error: input must be positive!"
    elif n == 1:
        print(n, end = " ")
    else:
        print(n, end = ", ")
        natural_recursive(n-1)


def natural_backward(n):
    if n <= 0:
        return "Error: input must be positive!"
    elif n == 1:
        print(n, end = " ")
    else:
        natural_backward(n-1)
        print(n, end = ", ")

import math
def count_digit(number):
    if number < 10 and number > -10:
        return 1
    else:
        t = int(number / 10)
        return count_digit(t) + 1

    
if __name__ == "__main__":
    #natural_recursive(8)
    #natural_backward(8)
    print(count_digit(987632))
 





