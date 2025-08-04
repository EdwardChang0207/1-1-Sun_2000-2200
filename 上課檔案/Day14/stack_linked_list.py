class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        if not self.top:
            self.top = Node(item)
        else:
            n = Node(item)
            n.next = self.top
            self.top = n
            
    def pop(self):
        if not self.top: return None
        item = self.top.data
        self.top = self.top.next
        return item
    