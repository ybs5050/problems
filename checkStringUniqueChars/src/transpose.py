

n = 11
matrix = [[0 for x in range(n)] for x in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        matrix[i][j] = count
        count += 1

# matrix(y,x) y = vertical, x = horizontal
last = n-1 #last row value position (x coordinate)
total = n-1 #number of levels
level = 0 #current level

for i in matrix:
    print(i)
print("----------------------")

# number of levels = (n-1)/2
while (level < total/2):
    for i in range(level, last):

        #swap top left and top right
        matrix[level][i], matrix[i][last] = matrix[i][last], matrix[level][i]
        #swap top left and bottom right
        #last-+level takes care of inner square
        matrix[level][i], matrix[last][last-i+level] = matrix[last][last-i+level], matrix[level][i]
        #swap top left and bottom left
        matrix[level][i], matrix[last-i+level][level] = matrix[last-i+level][level] ,matrix[level][i]

    level+=1
    last-=1
