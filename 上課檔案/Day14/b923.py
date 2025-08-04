class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [None for _ in range(size)]
        self.top = -1

    def push(self, item):
        if self.top == self.size-1:
            print('Full')
            return
        self.top += 1
        self.data[self.top] = item
        
    def pop(self):
        if self.top == -1: 
            print("Empty")
            return None
        item = self.data[self.top]
        self.top -= 1
        return item
    
n = int(input())
s = Stack(10000)
for _ in range(n):
    i = list(map(int, input().split()))
    if i[0] == 1:
        s.pop()
    elif i[0] == 2:
        print(s.data[s.top])
    else: 
        s.push(i[1])