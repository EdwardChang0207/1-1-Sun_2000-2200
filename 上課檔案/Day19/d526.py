class Node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

def Insert(BST:Node, item):
    if not BST:
        BST = Node(item)
        return BST
    if BST.data > item:
        BST.l = Insert(BST.l, item)
    elif BST.data < item:
        BST.r = Insert(BST.r, item)
    return BST

def Preorder(BT):
    if not BT: return
    print(BT.data, end=' ')
    Preorder(BT.l)
    Preorder(BT.r)

import sys
for N in sys.stdin:
    N = int(N)
    l = list(map(int, input().split()))
    T = None
    for i in l:
        T = Insert(T, i)
    Preorder(T)

