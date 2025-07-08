#input
n = int(input())
s = list(map(int, input().split()))
#score排序 -> print
s.sort()
print(*s)
#分case -> print
#(1)best case all>=60
if s[0] >= 60:
    print('best case')
    print(s[0])
#(2)worst case
elif s[-1] < 60:
    print(s[-1])
    print('worst case')
#(3)normal case
else:
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])
            break