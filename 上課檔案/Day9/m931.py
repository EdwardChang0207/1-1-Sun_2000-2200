n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
f, s = [0,0], [0,0]

for atk, dfn in a:
    if atk**2 + dfn**2 > f[0]**2 + f[1]**2:
        s = f
        f = [atk, dfn]
    elif atk**2 + dfn**2 > s[0]**2 + s[1]**2:
        s = [atk, dfn]

print(*s)