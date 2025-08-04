class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None for _ in range(size)]
    
    def find_val(self, index):
        if index >= self.size:
            return None
        if index < 0:
            return self.data[self.size+index]
        return self.data[index]
    
    def Traversal(self):
        for i in range(self.size):
            print(self.data[i])

    def Maximum(self):
        maximum = 0
        while not(self.data[maximum]): 
            maximum += 1
            if maximum >= self.size:
                return None
        for i in range(1, self.size):
            if not(self.data[i]):
                continue
            if self.data[i] > self.data[maximum]:
                maximum = i
        return i

    def Minimum(self):
        minimum = 0
        while not(self.data[minimum]): 
            minimum += 1
            if minimum >= self.size:
                return None
        for i in range(1, self.size):
            if not(self.data[i]):
                continue
            if self.data[i] < self.data[minimum]:
                minimum = i
        return i

    def Append(self, item):
        for i in range(self.size):
            if not(self.data[i]): 
                self.data[i] = item
                return
        print('FULL')
        return
    
    def Pop(self):
        for i in range(self.size-1, -1, -1):
            if self.data[i]:
                item = self.data[i]
                self.data[i] = None
                return item
        return None
    
    def Remove(self, target):#刪除某個元素
        #if not(target in self.data): return #O(n)
        for i in range(self.size):#O(n)
            if self.data[i] == target:
                self.data[i] = None
                return
        return
a = Array(4)
a.data = [1,2,3,None]
a.Append(4)
print(a.data)
i = a.Pop()
print(i)
print(a.data)