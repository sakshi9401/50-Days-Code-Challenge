X = [[56, 23, 13],[34, 65, 46], [77, 98, 9]]
Y = [[91, 85, 97], [16, 35, 24], [31, 24, 17]]
  
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  
for row in range(len(X)):

    for column in range(len(X[0])):
        result[row][column] = X[row][column]+ Y[row][column]
  
for r in result:
    print(r)
