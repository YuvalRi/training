# ex 5

def spidermanSteps(n: int):
    '''
    A recursive function which returns how many ways
    spiderman can climb a building
    '''
    if n < 1:
        print("Error! Please enter a natural number.")
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return spidermanSteps(n-2) + spidermanSteps(n-1)


if __name__ == "__main__":
    # we can see that from building of height 3, the ways equal to the sum
    # of the 2 previous option of height (as Fibonacci sequence)
    print(spidermanSteps(1))
    print(spidermanSteps(2))
    print(spidermanSteps(3))
    print(spidermanSteps(4))
    print(spidermanSteps(5))
    print(spidermanSteps(6))

