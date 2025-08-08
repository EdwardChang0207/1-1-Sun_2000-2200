def f(x):
    return 2*x - 3 
def g(x,y):
    return 2*x + y - 7
def h(x,y,z):
    return 3*x - 2*y + z

i = input().split()
i.reverse()
s = []
for a in i:
    if a == 'f':
        x = s.pop()
        r = f(x)
        s.append(r)
    elif a == 'g':
        x, y = s.pop(), s.pop()
        r = g(x, y)
        s.append(r)
    elif a == 'h':
        x, y, z = s.pop(), s.pop(), s.pop()
        r = h(x, y, z)
        s.append(r)
    else:
        s.append(int(a))
print(s[0])