a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
IM = True
if a and b == c:
    IM = False
    print('AND')

if a or b == c:
    IM = False
    print('OR')

if (a or b) and (not(a and b)) == c:
    IM = False
    print('XOR')

if IM:
    print('IMPOSSIBLE')