#while loop
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# while True: -> 無限迴圈

#for loop
# for index in 範圍:
#     ...
# for sushi in ['鮭魚','鮪魚','玉子燒']:
#     print(sushi)

# for i in 'hello':
#     print(i)

#range(start[init:0], end, interval[init:1]) from start, to end-1, increase interval for each time

# for i in range(1, 10, 1):
#     print(i)

# for i in range(1, 10):
#     print(i)
'''
for i in range(10):
    print(i)

#10 ~ 0
#while
i = 10
while i >= 0:
    print(i)
    i -= 1
#for
for i in range(10,-1,-1):
    print(i)

#continue(skip), break(stop)
for i in range(10):
    if i % 3 == 0: continue
    if i == 8: break
    print(i)

#1 2 3 4 5
a = [int(i) for i in input().split()] #['1','2','3','4','5']
print(a)
a = list(map(int, input().split()))
print(a)

l = [i for i in range(10)]
a = [i**2 for i in l if i%2==0]
print(a)
'''

import sys
for i in sys.stdin:
    print(i)