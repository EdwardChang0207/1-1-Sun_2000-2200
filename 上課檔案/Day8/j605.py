k = int(input())
r = [list(map(int,input().split())) for _ in range(k)]
h_t, h_s = -1, -1
w = 0
for t, s in r:
    if s > h_s:
        h_t = t
        h_s = s
    if s == -1: w+= 1

total = h_s-k-w
print(total, h_t)