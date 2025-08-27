class Queue:
    def __init__(self,size):
        self.size = size
        self.data = [None for _ in range(size)]
        self.head = 0
        self.rear = 0
    
    def enqueue(self, item):
        if self.rear == self.size:
            print('Full')
            return
        self.data[self.rear] = item
        self.rear += 1
    
    def dequeue(self):
        if self.head == self.rear:
            print('Empty')
            return None
        item = self.data[self.head]
        self.head += 1
        return item

q = Queue(5)
for i in range(6):
    q.enqueue(i)

print(q.data)