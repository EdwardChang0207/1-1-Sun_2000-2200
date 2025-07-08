l = [i for i in range(10)]
print(l[:6])
print(l[:7:2])
print(len(l))
if l: print(1)

l.append(10)
l.append(1)
l.append(1)

print(l)
print(l.count(1))
print(l.index(5))
l.insert(2, 4)
print(l)

i = l.pop(2)
print(i)
print(l)

l.insert(0,3)
l.remove(3)
print(l)

l.reverse()
print(l)

l.sort()
print(l)

l = [
    ['','',''],
    ['','',''],
    ['','','']
]