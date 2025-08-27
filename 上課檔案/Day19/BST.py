class Node:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None

def Insert(BST:Node, item):
    if not BST: 
        BST = Node(item)
        return BST
    if BST.data > item:
        BST.Lchild = Insert(BST.Lchild, item)
    elif BST.data < item:
        BST.Rchild = Insert(BST.Rchild, item)
    return BST

def Preorder(BT:Node):
    if not BT: return
    print(BT.data,end=' ')
    Preorder(BT.Lchild)
    Preorder(BT.Rchild)

def Inorder(BT:Node):
    if not BT: return
    Inorder(BT.Lchild)
    print(BT.data, end=' ')
    Inorder(BT.Rchild) 

def Postorder(BT:Node):
    if not BT: return
    Postorder(BT.Lchild)
    Postorder(BT.Rchild)   
    print(BT.data, end=' ')

B = None
l = [16, 7, 21, 40, 18, 6, 3]
for i in range(len(l)):
    B = Insert(B, l[i])

Preorder(B)
print()
Inorder(B)
print()
Postorder(B)