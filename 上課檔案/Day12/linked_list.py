class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

def find_val(a, n):
    if not(a): return None #O(1)
    if n == 0: return a.data #O(1)
    if a.next: #O(1)
        return find_val(a.next, n-1)
    else:
        print('index out of range')#O(1)
        return None #O(1)
    
# print(find_val(a, 2))
#Total = O(n)

#Traversal
def Traversal(a):
    if not(a): return None #O(1)
    print(a.data)#O(1)
    if a.next: return Traversal(a.next)#O(1)

# Traversal(a)
#Total = O(1) * n = O(n)

def Maximum(a):
    if a.next: #O(1)
        return max(a.data, Maximum(a.next))#O(1)
    else: return a.data

# print(Maximum(a))
#Total = (O(1)+O(1))*n = O(n)

def Sum(a):
    if not(a): #O(1)
        return None #O(1)
    if a.next: #O(1)
        return a.data + Sum(a.next) #O(1) + O(1)
    else: return a.data #O(1)

# print(Sum(a))
#Total = O(1) * n = O(n)

#Append
def Append(a, item):
    if a.next:#O(1)
        a.next = Append(a.next, item)#O(1)
    else:
        a.next = Node(item)#O(1)
    return a#O(1)

a = Append(a, 4)
#Total = O(1) * n = O(n)
Traversal(a)

#Pop
def Pop(a):
    if not a: return None
    if not a.next.next:
        item =  a.next.data
        a.next = None
        return item
    if a.next:
        return Pop(a.next)
    else:
        return a.data
    
i = Pop(a)
print(i)

def Insert(node, item, t, n=0):
    if t == n:
        i = Node(item)
        i.next = node.next
        node.next = i
        return node
    else:
        return Insert(n.next, item, t, n+1)

    
# a = Insert(a, 2, 4)



