#input: list of integers, output: minimum element of that list 
def min (lst): #required function
    lst.sort() #sorting the given list (increased order) and then extracting the element in the first index
    return lst[0]

if __name__ == "__main__":
    lst2 = [5,2,3,4,1] #example
    print(min(lst2))