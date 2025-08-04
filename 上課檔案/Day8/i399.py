l = list(map(int, input().split()))
s = set(l)
print(max([l.count(i) for i in s]), end=' ')
l = [i for i in s]
l.reverse()
print(*l)