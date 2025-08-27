def SelectionProblem(l:list, k:int):
    print(f'k:{k}')
    if len(l) <= 5: return sorted(l)[k-1]
    groups = []
    g = []
    for i in range(len(l)):
        g.append(l[i])
        if len(g) == 5:
            g.sort()
            groups.append(g)
            g = []
    if g:
        g.sort()
        groups.append(g)
    print(*groups,sep='\n')
    medians = [g[len(g)//2] for g in groups if len(g) == 5]

    mm = SelectionProblem(medians, (len(medians)+1)//2)

    L,R = [], []

    for i in l:
        if i < mm: L.append(i)
        elif i > mm: R.append(i)
    print(f'L:{L}')
    print(f'R:{R}')
    
    idx_mm = len(L)+1
    print(f'idx:{idx_mm}')
    if idx_mm == k: return mm
    elif idx_mm > k: return SelectionProblem(L, k)
    else: return SelectionProblem(R, k-len(L)-1)

l = [21, 7, 14, 8, 35, 60, 2, 52, 45, 18, 23, 31, 72, 63, 1, 50, 27, 33, 19, 9, 4, 16, 47, 36, 40]
x = SelectionProblem(l, 10)
print(sorted(l))
print(x) 