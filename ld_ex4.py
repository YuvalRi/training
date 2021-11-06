#exercise 4 - concatenating following dictionaries to create a new one

def taskA(A,B):
    for key in B:
        A[key] = B[key]
    return A

def taskB(A,B):
    for key in B:
        if key in A.keys():
            lst = [A[key], B[key]]
            A[key] = lst
        else:
            A[key] = B[key]
    return A

if __name__ == "__main__":
    A = {1:20, 2:50}
    B = {1:25, 3:30}
    print(taskB(A,B))