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

s = Stack(3)
for i in range(4):
    s.push(i)
print(s.data)

i = s.pop()
print(i)
print(s.data)