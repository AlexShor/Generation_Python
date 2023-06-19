# mtx = [[int(i) for i in input().split()] for j in range(int(input()))]
# mtx = [[4, 9, 2], [8, 1, 6], [3, 5, 7]]
# mtx = [['.'] * 8 for j in range(8)]
# mtx = [[int(i) for i in input().split()] for j in range(n)]

n, m = 3, 2
mtxA = [[2, 5],
        [6, 7],
        [1, 8]]
n2, m2 = 2, 3
mtxB = [[1, 2, 1],
        [0, 1, 0]]

mtxC = [[0] * m2 for j in range(n)]

for i in range(n):
    for j in range(m2):
        for g in range(m):
            mtxC[i][j] += mtxA[i][g] * mtxB[g][j]


for row in mtxC: print(*row)

# for i in range(n):
#     for j in range(m):
#         print(str(mtxC[i][j]).ljust(3), end='')
#     print()



