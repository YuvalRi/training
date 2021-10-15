#input: list of strings, output: number of strings which satisfy 2 conditions:
# 1. The length of the string is larger than 2.
# 2. The first and last character are the same.
#def checkLenTwo(lst): #function for statement 1.
    #newlst = []
    #for i in lst:
        #if (len(i)) > 2:
            #newlst.append(i)
    #return(len(newlst))

#if __name__ == "__main__":
    #lst2 = ["dog","cat", "be"] #example
    #print(checkLenTwo(lst2))

#def checkFirstLast(list): #function for statement 2
    #newlst2 = []
    #for i in list:
        #if i[0] == i[-1]:
            #newlst2.append(i)
    #return(len(newlst2))

#if __name__ == "__main__":
    #lst3 = ["dog","cat", "be", "aba", "ccc", "dad"] #example
    #print(checkFirstLast(lst3))

def fun(lst4):
    newlst3 = []
    for i in lst4:
        if len(i) > 2 and i[0] == i[-1]: #2 required statements 
            newlst3.append(i)
    return(len(newlst3))

if __name__ == "__main__":
    lst3 = ["dog","cat", "be", "aba", "dad", "bb", "141"] #example
    print(fun(lst3))


