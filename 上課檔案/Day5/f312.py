A1,B1,C1 = map(int,input().split())
A2,B2,C2 = map(int,input().split())
n = int(input())

def f(a,b,c,n):
    return a*n**2 + b*n + c

r = []
for i in range(n+1):
    s1 = f(A1,B1,C1,i)
    s2 = f(A2,B2,C2,n-i)
    r.append(s1+s2)
print(max(r))