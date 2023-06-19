# mtx = [[int(i) for i in input().split()] for j in range(int(input()))]
mtx = [[4, 9, 2], [8, 1, 6], [3, 5, 7]]
# mtx = [['.'] * 8 for j in range(8)]

check = True
s = sum(mtx[0])

if sorted(sum(mtx, [])) != [i + 1 for i in range(len(mtx)**2)]: check = False

if check:
    for i in range(len(mtx)):
        if sum(mtx[i]) != s:
            check = False
            break
        if sum([mtx[j][i] for j in range(len(mtx))]) != s:
            check = False
            break

if check:
    if sum([mtx[i][i] for i in range(len(mtx))]) != s: check = False
    if sum([mtx[i][len(mtx)-i-1] for i in range(len(mtx))]) != s: check = False

if check: print('YES')
else: print('NO')