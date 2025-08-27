class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.rear = None
    def enqueue(self, item):
        item = Node(item)
        if not self.rear:
            self.head = item
            self.rear = item
            return
        self.rear.next = item
        self.rear = self.rear.next
    def dequeue(self):
        if not self.head and not self.rear:
            print('Empty')
            return None
        item = self.head.data
        self.head = self.head.next
        return item