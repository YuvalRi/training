# ex 4
# a

def mergeDict(dic_a, dic_b):
    '''
    A function which merges between two given dictionaries
    '''
    for key, value in dic_b.items():
        dic_a[key] = value
    return dic_a


if __name__ == "__main__":
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    mergeDict(dic_a=dic1, dic_b=dic2)
    mergeDict(dic_a=dic1, dic_b=dic3)
    print(dic1)

# b

# The function 'mergeDict' from the previous task is relevant


def taskB(A, B):
    for key in B:
        if key in A.keys():
            lst = [A[key], B[key]]
            A[key] = lst
        else:
            A[key] = B[key]
    return A


if __name__ == "__main__":
    A = {1: 20, 2: 50}
    B = {1: 25, 3: 30}
    print(taskB(A, B))

# c
dic4 = {6: 60, 8: 80}
dic5 = {"Ofek": "Yuval", "Gabri": "Avital"}
mergeDict(dic_a=dic4, dic_b=dic5)
if dic4 == {6: 60, 8: 80, "Ofek": "Yuval", "Gabri": "Avital"}:
    print("Excellent!")
else:
    print("There is a problem!")

dic6 = {1: 30, 2: 40}
dic7 = {2: 20, 1: 90}
taskB(dic6, dic7)
if dic6 == {1: [30, 90], 2: [40, 20]}:
    print("Excellent!")
else:
    print("There is a problem!")
