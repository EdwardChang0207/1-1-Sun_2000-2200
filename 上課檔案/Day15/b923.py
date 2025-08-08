n = int(input())
s = []
for _ in range(n):
    l = input().split()
    if l[0] == '1':#pop
        s.pop()
    elif l[0] == '2':#print(s[top])
        print(s[-1])
    else:#push
        s.append(l[1])