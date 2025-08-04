import sys
sys.setrecursionlimit(10**6)
def A(m,n):
    if m == 0: return n+1
    if (m > 0) and (n == 0):
        return A(m-1, 1)
    if (m > 0) and (n > 0):
        return A(m-1, A(m, n-1))
    
m, n = map(int, input().split())
print(A(m,n))