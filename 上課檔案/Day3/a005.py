t = int(input())
for i in range(t):
    #處理一個數列的方法
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    if a[1]-a[0] == a[2]-a[1]:#等差
        print(a[0],a[1],a[2],a[3],a[3]+a[1]-a[0])
    else:#等比
        print(a[0],a[1],a[2],a[3],a[3]*(a[1]//a[0]))