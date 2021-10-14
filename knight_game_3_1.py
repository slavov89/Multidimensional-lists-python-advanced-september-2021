def read_matrix():
    nu = int(input())
    matrix_func = []
    for i in range(nu):
        matrix_func.append(list(input()))
    return matrix_func


def knight_moves(row, col, matrix, hits = 0):
    if row + 2 < len(matrix) and col - 1 >= 0:
        if matrix[row + 2][col - 1] == "K":
            hits += 1
    if row + 1 < len(matrix) and col - 2 >= 0:
        if matrix[row + 1][col - 2] == "K":
            hits += 1
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row - 2][col - 1] == "K":
            hits += 1
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == "K":
            hits += 1
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        if matrix[row + 2][col + 1] == "K":
            hits += 1
    if row + 1 < len(matrix) and col + 2 < len(matrix):
        if matrix[row + 1][col + 2] == "K":
            hits += 1
    if row - 2 >= 0 and col + 1 < len(matrix):
        if matrix[row - 2][col + 1] == "K":
            hits += 1
    if row - 1 >= 0 and col + 2 < len(matrix):
        if matrix[row - 1][col + 2] == "K":
            hits += 1
    return row, col, hits


matrix = read_matrix()
removed = 0


while True:
    row_to_clear, col_to_clear, hit_count = 0, 0, 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "K":
                row, col, hits = knight_moves(r, c, matrix)
                if hits > hit_count:
                    row_to_clear, col_to_clear, hit_count = row, col, hits

    if hit_count > 0:
        matrix[row_to_clear][col_to_clear] = 0
        removed += 1
    else:
        break

print(removed)


