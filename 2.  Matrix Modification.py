def read_matrix():
    rows = int(input())

    matrix_func = []

    for row in range(rows):
        matrix_func.append([int(x) for x in input().split(" ")])

    return matrix_func


matrix = read_matrix()

command = input()

while command != "END":
    command = command.split()
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if len(matrix) > row >= 0 and len(matrix[0]) > col >= 0:
        if command[0] == "Add":
            matrix[row][col] += value
        elif command[0] == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()

for i in range(len(matrix)):
    print(*matrix[i])
