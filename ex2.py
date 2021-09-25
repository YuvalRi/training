#reversed user's first and last name

def rev(x): #the required function, x represents a string 
    st = x.split(" ") #splitting the string (x) into list (data items)
    r = reversed(st) #changing the items order as requested in the question
    return(" ".join(r)) #joining all items together into one string 
    
if __name__ == "__main__":
    x = input("please enter your first name and last name: ")
    print(rev(x))