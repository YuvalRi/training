#program to sum all elements in a list
if __name__ == "__main__":
    lst = [] #defining empty list which contain the elements the user will enter, then we want to sum all elements in this list.
    x = int(input("Please enter number of elements: ")) #total number of elements in our cute list

    for i in range(x): #we want to insert an element for each index in the list. if x equal to 2, we want the user to insert 2 elemnts.
        e = int(input("Enter element:")) #we want that each element will be a type of integer
        lst.append(e) #adding each element (e) to the our list (lst)

    print("Sum of elements in the given list is: ", sum(lst)) #required output