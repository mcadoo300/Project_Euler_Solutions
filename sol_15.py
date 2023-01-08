def index_val(i, j, matrix):
    if i == 0 or j == 0:
        return 1
    return matrix[i-1][j] + matrix[i][j-1]


lattice = [[0]*21 for _ in range(21)]
i = 0
j = 0
while i < 21:
    while j < 21:
        lattice[i][j] = index_val(i, j, lattice)
        j += 1
    j = 0
    i += 1
print(lattice[20][20])
