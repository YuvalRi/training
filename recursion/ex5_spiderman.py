# ex 5

def spiderman_steps(n: int):
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
        return spiderman_steps(n-2) + spiderman_steps(n-1)


if __name__ == "__main__":
    # we can see that from building of height 3, the ways equal to the sum
    # of the 2 previous option of height (as Fibonacci sequence)
    print(spiderman_steps(1))
    print(spiderman_steps(2))
    print(spiderman_steps(3))
    print(spiderman_steps(4))
    print(spiderman_steps(5))
    print(spiderman_steps(6))
