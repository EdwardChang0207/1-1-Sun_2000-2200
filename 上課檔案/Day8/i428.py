n = int(input())
p = [list(map(int, input())) for i in range(n)]
d = []

for i in range(1, n):
    x1, y1 = p[i] 
    x2, y2 = p[i-1]
    d.append(abs(x1-x2) + abs(y1-y2))

print(max(d),min(d))