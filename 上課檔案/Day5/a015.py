r, c = map(int, input().split())
m = [list(map(int, input().split())) for i in range(r)]
a = []
for i in range(c):
    col = []
    for j in range(r):
        col.append(m[j][i])
    a.append(col)
for row in a:
    print(*row) #* for all