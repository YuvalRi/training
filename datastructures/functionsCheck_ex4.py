from datastruc_ex4 import mergeDict, taskC

# ex 4 - checking the created functions (c + d)


if __name__ == "__main__":

    A = {1: 20, 2: 50}
    B = {1: 25, 3: 30}
    print(taskC(A, B))

    dic4 = {6: 60, 8: 80}
    dic5 = {"Ofek": "Yuval", "Gabri": "Avital"}
    mergeDict(dic_a=dic4, dic_b=dic5)
    if dic4 == {6: 60, 8: 80, "Ofek": "Yuval", "Gabri": "Avital"}:
        print("Excellent!")
    else:
        print("There is a problem!")

    dic6 = {1: 30, 2: 40}
    dic7 = {2: 20, 1: 90}
    taskC(dic6, dic7)
    if dic6 == {1: [30, 90], 2: [40, 20]}:
        print("Excellent!")
    else:
        print("There is a problem!")
