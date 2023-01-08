import math


# function to populate on cycle in the matrix
def loop_cycle(i, j, loop_c, matrix):
    center = math.ceil(len(matrix[0])/2) - 1
    # step right in matrix
    j += 1
    matrix[i][j] = matrix[i][j-1] + 1
    while i < center + loop_c:
        i += 1
        matrix[i][j] = matrix[i-1][j] + 1
    matrix[i][j] = matrix[i-1][j] + 1
    # second print


    while j > center - loop_c:
        j -= 1
        matrix[i][j] = matrix[i][j+1] + 1
    matrix[i][j] = matrix[i][j+1] + 1

    # 3rd print


    while i > center - loop_c:
        i -= 1
        matrix[i][j] = matrix[i+1][j] + 1
    matrix[i][j] = matrix[i+1][j] + 1
    # 4th print

    while j < center + loop_c:
        j += 1
        matrix[i][j] = matrix[i][j-1] + 1

    return matrix


def sum_diagonal(p_matrix):
    d_sum = 0
    num_col = len(p_matrix[0])
    for rowp in range(num_col):
        if rowp == (num_col -1-rowp):
            d_sum += p_matrix[rowp][rowp]
        else:
            d_sum += p_matrix[rowp][rowp]
            d_sum += p_matrix[rowp][num_col-1-rowp]
    return d_sum


def populate_matrix(size):
    n = size

    center_k = math.ceil(n / 2) - 1

    i_k = center_k
    j_k = center_k

    loop_count = 1

    matrix_k = [[0] * size for _ in range(size)]

    matrix_k[i_k][j_k] = 1

    while i_k > 0:
        matrix_k = loop_cycle(i_k, j_k, loop_count, matrix_k)
        loop_count += 1
        i_k -= 1
        j_k += 1
    return matrix_k


matrix_t = populate_matrix(1001)

print(sum_diagonal(matrix_t))
