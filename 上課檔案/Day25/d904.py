import math
c, n = map(int, input().split())
m = [int(input()) for _ in range(n)]
m.sort()
d = [math.inf]*(c+1)
d[0] = 0
for i in m:
    for j in range(i,c+1):
        d[j] = min(d[j], d[j-i]+1)
print(d[c])
