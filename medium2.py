def matrix_add(A, B):
    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(A)):  
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result

A = [[1,2,3],[4,5,6]]
B = [[7,8,9],[1,2,3]]

print(matrix_add(A,B))
