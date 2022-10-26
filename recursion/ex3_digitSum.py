# ex 3

# option 1 - my implementation 
def digit_count(n: int):
    '''
    A recursive function which returns the digits of a given number
    '''
    count = 1
    if n < 0:
        n = n*(-1)
    if len(str(n)) == 1:
        return count
    elif len(str(n)) > 1:
        count = digit_count(n//10) + 1
    return count

# option 2 - our implementation 

def count_digit(number):
    '''
    A recursive function which returns the digits of a given number
    '''
    if number < 10 and number > -10:
        return 1
    else:
        t = int(number / 10)
        return count_digit(t) + 1


if __name__ == "__main__":
    n = int(input("Please enter a number: "))
    print(digit_count(n))
    print(count_digit(n))

        