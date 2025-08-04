n = int(input())
#重複做n次
for _ in range(n):
    #檢查一個對聯
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    r = ''
    #檢查A規則
    for l in [l1,l2]:
        if l[1] == l[3] or l[1] != l[5]:
            r += 'A'
            break
    #檢查B規則
    if l1[-1] == 0 or l2[-1] == 1:
        r += 'B'
    #檢查C規則
    for i in range(1, 5, 2):
        if l1[i] == l2[i]:
            r += 'C'
            break
    if not(r): print('None')
    else: print(r)