class Node:
    def __init__(self, data):
        self.Lchild = None
        self.data = data
        self.Rchild = None

def DLR(BT:Node):
    if not BT: return
    print(BT.data)
    if BT.Lchild: DLR(BT.Lchild)
    if BT.Rchild: DLR(BT.Rchild)

def LDR(BT:Node):
    if not BT: return
    if BT.Lchild: LDR(BT.Lchild)
    print(BT.data)
    if BT.Rchild: LDR(BT.Rchild)

def LRD(BT:Node):
    if not BT: return
    if BT.Lchild: LRD(BT.Lchild)
    if BT.Rchild: LRD(BT.Rchild)
    print(BT.data)