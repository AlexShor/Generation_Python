n = 4

#matrix = [[int(i) for i in input().split()] for j in range(n)]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [3, 4, 5, 6], [1, 2, 3, 4]]

print(matrix)


left = []
right = []
top = []
bottom = []

for i in range(n):
    for j in range(n):
        if (j < i < n - 1 - j): left.append(matrix[i][j])
        if (j > i > n - 1 - j): right.append(matrix[i][j])
        if (j > i < n - 1 - j): top.append(matrix[i][j])
        if (j < i > n - 1 - j): bottom.append(matrix[i][j])

print(f"Верхняя четверть: {sum(top)}")
print(f"Правая четверть: {sum(right)}")
print(f"Нижняя четверть: {sum(bottom)}")
print(f"Левая четверть: {sum(left)}")