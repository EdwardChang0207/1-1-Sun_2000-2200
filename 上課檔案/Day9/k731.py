n = int(input())
p = [list(map(int,input().split())) for _ in range(n)]
p.insert(0, [0,0])
v = [[p[i][0]-p[i-1][0],p[i][1]-p[i-1][1]] for i in range(1,len(p))]
l, r, u = 0, 0, 0
for i in range(1, len(v)):
    cross = v[i-1][0]*v[i][1] - v[i-1][1]*v[i][0]
    if cross > 0: l += 1
    elif cross == 0: u += 1
    else: r += 1
print(l,r,u)
