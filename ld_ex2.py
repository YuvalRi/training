#input: list of integers, output: minimum element of that list 
lst = [] #empty list 
def min (lst): #required function
    lst.sort() #sorting the given list (increased order) and then extracting the element in the first index
    return(lst[0])

if __name__ == "__main__":
    print(lst[0])