#program to print first n natural numbers using recursion

def natural_recursive(n):
    if n <= 0:
         return "Error: input must be positive!"
    elif n == 1:
        print(n, end = " ")
    else:
        print(n, end = ", ")
        natural_recursive(n-1)
    
    
if __name__ == "__main__":
    natural_recursive(8)


