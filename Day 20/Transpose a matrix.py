matrix = [[10,21],[13,43],[25,16]]
for row in matrix :
    print(row)
trans = [[matrix[j][i] 
        for j in range(len(matrix))] 
            for i in range(len(matrix[0]))]
print("\n")
for row in trans:
    print(row)
