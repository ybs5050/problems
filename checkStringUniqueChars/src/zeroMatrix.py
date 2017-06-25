n = 5
matrix = [[0 for x in range(n)] for x in range(n)]
count = 0;
row = [False for x in range(n)]
column = [False for x in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = count
        count += 1
matrix[n-1][n-1] = 0
for i in matrix:
    print(i)

for i,j in enumerate(range(n)):
    for j,k in enumerate(range(n)):
        if matrix[i][j] is 0:
            # save row and column of zeros
             row[i] = True
             column[j] = True

for i,j in enumerate(range(n)):
    for j,k in enumerate(range(n)):
        # when in the same column or row
        if(row[i] or column[j]):
            matrix[i][j] = 0

print("===========================")
for i in matrix:
    print(i)
