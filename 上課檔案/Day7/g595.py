n = int(input())
h = list(map(int,input().split()))
r = 0
for i in range(len(h)):
    if h[i] == 0: #如果遇到斷掉的
        #決定修補高度
        #記錄成本
        if i == 0: r += h[i+1]
        elif i == len(h)-1: r += h[i-1]
        else: r += min(h[i+1],h[i-1])
print(r)