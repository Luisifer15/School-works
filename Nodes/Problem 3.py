class Node:
    def __init__(self, DataIn):
        self.left = None
        self.right = None
        self.data = DataIn

class BinaryTree:
    def InOrder(RootIn):
        if RootIn is None:
            return
        else:
            BinaryTree.InOrder(RootIn.left)
            print(RootIn.data + " ", end="", sep="")
            BinaryTree.InOrder(RootIn.right)
            return

TreeRoot = Node('F')
TreeRoot.left = Node('B')
TreeRoot.left.left = Node('A')
TreeRoot.left.right = Node('D')
TreeRoot.left.right.left = Node('C')
TreeRoot.left.right.right = Node('E')
TreeRoot.right = Node('G')
TreeRoot.right.right = Node('I')
TreeRoot.right.right.left = Node('H')


print('Alphabetical:')
BinaryTree.InOrder(TreeRoot)
