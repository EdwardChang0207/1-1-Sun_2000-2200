#1->10
'''
#loop
for i in range(1, 11):
    print(i, end=',')
#recursive
def f(start, end):
    print(start, end=',')
    if start == end: return
    return f(start+1, end)
#等差數列第n項 n:int, d(公差), a0(首項)
n, d, a0 = 5, 2, 0
#loop
for i in range(n):
    a0 += d
print(a0)
#recursive
def f(n, d, a0):
    if n == 0: return a0
    return f(n-1, d, a0+d)
print(f(5,2,0))
#等比級數 n, r(公比), a0(首項)
ans = 0
n, r, a0 = 5, 3, 2
#loop
for i in range(n):
    ans += a0
    a0 *= r
print(ans)
#recursive
def f(n, r, a0, ans=0):
    if n == 0: return ans
    ans += a0
    return f(n-1, r, a0*r, ans)
print(f(5,3,2))

#sum 1->n
ans = 0
n = 10
#loop
for i in range(1, n+1):
    ans += i
print(ans)

#recursion
def sum(start, end):
    if start > end: return 0
    return sum(start+1, end) + start
print(sum(1,10))

#階乘
ans = 1
n = 10
#loop
for i in range(1, n+1):
    ans *= i
print(ans)

#recursion
def f(n):
    if n == 0: return 1
    return n*f(n-1)
print(f(10))
'''

#指數
x, n = 2, 10
ans = 1
for i in range(n):
    ans *= x
print(ans)

def f(x, n):
    if n == 0: return 1
    if n == 1: return x
    return f(x, n-1) * x

print(f(2,10))
#二項式係數
def Bin(n,m):
    if n == m: return 1
    if m == 1: return n
    return Bin(n-1,m-1)+Bin(n-1,m)

print(Bin(4,2))