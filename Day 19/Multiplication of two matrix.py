A = [[2, 1, 13],
    [2, 15, 6],
    [7, 18, 9]]
 
B = [[15, 8, 12, 25],
    [63, 17, 4, 0],
    [5, 52, 19, 15]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
 
for i in range(len(A)):
 
    for j in range(len(B[0])):
 
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)
