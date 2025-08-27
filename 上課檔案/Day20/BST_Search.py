class Node:
    def __init__(self,data):
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

def Search(BST:Node, target, round=1):
    if BST.data == target:
        print(f'found at round {round}')
        return
    elif BST.l and BST.data > target:
        return Search(BST.l, target, round+1)
    elif BST.r and BST.data < target:
        return Search(BST.r, target, round+1)
    print(f'not found at round {round}')
    return

BST = None
l = [20, 15, 27, 10, 18, 30]
for i in l:
    BST = Insert(BST, i)

Search(BST, 10)

