def checkLen(str):
    return len(str) > 2

def func2(str):
    """
    The function checks if the last character equals to the first
    """
    return str != "" and str[0] == str[-1]
    
if __name__ == "__main__":
    counter = 0
    lst = ["", "aa", "Yuval", "11", "1451", "OfekO"]
    for i in lst:
        if func2(i) and checkLen(i): 
            counter = counter + 1
    print(counter)


