import math

def LinearSearch(l, target):
    for i in range(len(l)):
        if l[i] == target:
            print(f'found at round {i+1}')
            return
    print(f'not found at round {len(l)}')
    return

def BinarySearch(upper, lower, target, l):
    mid = math.ceil((upper+lower)/2)
    print(f'upper:{upper}, lower:{lower}, mid:{mid}')
    if l[mid] == target:
        print('found')
        return
    elif upper <= lower:
        print('not found')
        return
    elif l[mid] > target:
        return BinarySearch(mid-1, lower, target, l)
    elif l[mid] < target:
        return BinarySearch(upper, mid+1, target, l)
    
l = [1,3,5,7,9]
# LinearSearch(l, 4)
BinarySearch(len(l)-1, 0, 4, l)
'''
r=1
upper = 4, lower = 0 -> mid = 2
upper = 4, lower = 3 -> mid = 4
upper = 4, lower = 4
'''
