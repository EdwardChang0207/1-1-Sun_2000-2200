a,b,c=input().split()
a,b,c= int(a), int(b), int(c)
l=[a,b,c]
if l[0] > l[1]: l = [l[1],l[0],l[2]]
if l[1] > l[2]: l = [l[0],l[2],l[1]]
if l[0] > l[1]: l = [l[1],l[0],l[2]]
print(l[0],l[1],l[2])
d,e,f=l[2]**2,l[1]**2,l[0]**2
if l[2]>=(l[1]+l[0]):
    print('No')
else:
    if d==(e+f):
        print('Right')
    elif d>(e+f):
        print('Obtuse')
    else:
        print('Acute')