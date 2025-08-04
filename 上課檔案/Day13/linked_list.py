class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def Append(self,item):
        if not(self.head):
            self.head = Node(item)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(item)
        return
    
    def Traversal(self, node):
        if not node: return
        print(node.data)
        return self.Traversal(node.next)
    
    def Pop(self, node):
        if not(self.head): #邊界條件 edge condition
            return None
        if not(self.head.next):
            item = self.head.data
            self.head = None
            return item
        if not(node.next.next):
            item = node.next.data
            node.next = None
            return item
        return self.Pop(node.next)

    def Find_val(self, n, cur=0):#找n-th val
        if not self.head: return None
        node = self.head
        cur = 1
        while n > cur:
            if not node.next:
                return None
            node = node.next
            cur += 1
        return node.data
    
    def Insert(self, n, item):
        if not self.head:
            if n != 0: return
            else: 
                self.head = Node(item)
                return
            
        if n == 0:
            i = Node(item)
            i.next = self.head
            self.head = i
            return
        
        node = self.head
        while n > 1:
            node = node.next
            n -= 1

        i = Node(item)
        if node.next:
            j = node.next
            node.next = j
            j.next = i
        else:
            node.next = i
        return
    
    def Sum(self):
        s = 0
        if not self.head: return s
        node = self.head
        while node:
            s += node.data
            node = node.next
        return s
    
    def Maximum(self):
        if not self.head: return None
        maximum = self.head.data
        node = self.head
        while node:
            if maximum < node.data:
                maximum = node.data
            node = node.next
        return maximum

    def Minimum(self):
        if not self.head: return None
        minimum = self.head.data
        node = self.head
        while node:
            if minimum > node.data:
                minimum = node.data
            node = node.next
        return minimum


l = Linked_list()
l.Append(1)
l.Append(2)

# print(l.head.data)
# print(l.head.next.data)
# i = l.Pop(l.head)
# print(i)
# l.Traversal(l.head)
l.Insert(0, 4)
l.Traversal(l.head)
print(l.Sum())
print(l.Maximum())
print(l.Minimum())