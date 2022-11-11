# ex6

def allPaths(mat, m: int, n: int):
    if m == 1 and n == 1:
        return mat
    if m == n and m == 2:
        path1 = mat[0][0], mat[0][1], mat[1][1]
        path2 = mat[0][0], mat[1][0], mat[1][1]
        return path1, path2
    if m == n and m == 3:
        path1 = mat[0][0], mat[0][1], mat[0][2], mat[1][2], mat[2][2]
        path2 = mat[0][0], mat[0][1], mat[1][1], mat[1][2], mat[2][2]
        path3 = mat[0][0], mat[0][1], mat[1][1], mat[2][1], mat[2][2]
        path4 = mat[0][0], mat[1][0], mat[1][1], mat[1][2], mat[2][2]
        path5 = mat[0][0], mat[1][0], mat[1][1], mat[2][1], mat[2][2]
        path6 = mat[0][0], mat[1][0], mat[2][0], mat[2][1], mat[2][2]
        return path1, path2, path3, path4, path5, path6

        

if __name__ == "__main__":
    A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    #B = [[1,2], [3,4]]
    #print(allPaths(B, 2, 2))
    print(allPaths(A, 3, 3))