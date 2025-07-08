def flip(matrix:list):
    matrix.reverse()
    return matrix

def rotate(matrix:list):
    #AT
    new = []
    for i in range(len(matrix[0])):
        col = []
        for j in range(len(matrix)):
            col.append(matrix[j][i])
        new.append(col)
    new = flip(new)
    return new

R, C, M = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(R)]
k = list(map(int,input().split()))
k.reverse()
for i in k:
    if i == 0:
        B = rotate(B)
    else:
        B = flip(B)

print(len(B), len(B[0]))
for row in B:
    print(*row)