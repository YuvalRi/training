# ex 4
# a - python program to concatenate following dictionaries to create a new one

if __name__ == "__main__":
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    for key, value in dic2.items():
        dic1[key] = value
    for key, value in dic3.items():
        dic1[key] = value
    print(dic1)


# b


def mergeDict(dic_a, dic_b):
    '''
    A function which merges between two given dictionaries
    '''
    for key, value in dic_b.items():
        dic_a[key] = value
    return dic_a

# c


def taskC(A, B):
    '''
    A function which concatenate given dictionaries but under
    the conditions explained in the exercise
    '''
    for key in B:
        if key in A.keys():
            lst = [A[key], B[key]]
            A[key] = lst
        else:
            A[key] = B[key]
    return A
