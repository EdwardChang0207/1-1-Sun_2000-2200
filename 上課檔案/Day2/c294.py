a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
l = [a,b,c]
if l[0] > l[1]: l = [l[1],l[0],l[2]]
if l[1] > l[2]: l = [l[0],l[2],l[1]]
if l[0] > l[1]: l = [l[1],l[0],l[2]]
print(l[0],l[1],l[2])
a,b,c = l[0],l[1],l[2]
if a+b <= c: 
    print('No')
else:
    if a**2+b**2 < c**2:
        print('Obtuse')
    elif a**2+b**2 == c**2:
        print('Right')
    else:
        print('Acute')