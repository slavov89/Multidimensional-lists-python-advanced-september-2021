matrix = input().split("|")
new_list = []
result = []
for i in range(len(matrix)-1, -1, -1):
    new_list.append(matrix[i].split(" "))
    elements = matrix[i].split()            # another solution
    result += elements                      # another solution

print(*result)                              # another solution

new_list_2 = []
for i in range(len(new_list)):
    for k in range(len(new_list[i])):
        if new_list[i][k] == "":
            pass
        else:
            new_list_2.append(new_list[i][k])

print(*new_list_2)