def swap(a, b):
    return b, a
def SelectionProblem(l: list, k: int):
    print(f'k:{k}')
    if len(l) <= 5:
        return sorted(l)[k-1] #如果只有一列，直接排序後return k-1項

    # Step1: 分組，每組最多 5 個
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
    #排序
    for i in range(len(groups)):
        for j in range(len(groups)-i-1):
            if len(groups[j+1]) != 5: continue
            if groups[j][2] > groups[j+1][2]:
                groups[j], groups[j+1] = swap(groups[j], groups[j+1])

    print(*groups, sep='\n')
    # Step2: 找每組中位數
    medians = [g[len(g)//2] for g in groups if len(g) == 5]

    # Step3: 找 median of medians
    mm = SelectionProblem(medians, (len(medians)+1)//2)
    print(f'mm:{mm}')
    s1 = []  # 左上
    s2 = []  # 右下
    if len(medians) == 1: 
        mid_group = 0
    elif len(medians) % 2 == 0: 
        mid_group = len(medians)//2 - 1
    else: 
        mid_group = len(medians)//2
    print(f'mid_group:{mid_group}')
    for i in range(len(groups)):
        # print(f'i:{i}, j:{j}')
        if i <= mid_group:
            for j in range(3):
                if i == mid_group and j == 2: continue
                s1.append(groups[i][j])
        if i >= mid_group:
            if len(groups[i])<3: continue
            for j in range(2, len(groups[i])):
                if i == mid_group and j == 2: continue
                s2.append(groups[i][j])

    print(f's1:{s1}')
    print(f's2:{s2}')

    l = []
    idx_mm = 1
    for g in groups:
        for i in g:
            if i < mm: idx_mm += 1
            l.append(i)
    
    if k == idx_mm:
        return mm
    elif k < idx_mm: #刪s2
        l = [i for i in l if (i not in s2) and (i != mm) ]
        return SelectionProblem(l, k)
    else:
        l = [i for i in l if (i not in s1) and (i != mm)]
        return SelectionProblem(l, k - len(s1) - 1)  

l = [21, 7, 14, 8, 35, 60, 2, 52, 45, 18, 23, 31, 72, 63, 1, 50, 27, 33, 19, 9, 4, 16, 47, 36, 40]
x = SelectionProblem(l, 10)
print(sorted(l))
print(x) 