class Node:
    def __init__(self, DataIn):
        self.left = None
        self.right = None
        self.data = DataIn

class BinaryTree:
    def PreOrder(RootIn):
        if RootIn is None:
            return
        else:
            print(RootIn.data + " ", end="", sep="")
            BinaryTree.PreOrder(RootIn.left)
            BinaryTree.PreOrder(RootIn.right)
            return

    def InOrder(RootIn):
        if RootIn is None:
            return
        else:
            BinaryTree.InOrder(RootIn.left)
            print(RootIn.data + " ", end="", sep="")
            BinaryTree.InOrder(RootIn.right)
            return

    def PostOrder(RootIn):
        if RootIn is None:
            return
        else:
            BinaryTree.PostOrder(RootIn.left)
            BinaryTree.PostOrder(RootIn.right)
            print(RootIn.data + " ", end="", sep="")
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

print('Pre-Order:')
BinaryTree.PreOrder(TreeRoot)
print('\nIn-Order:')
BinaryTree.InOrder(TreeRoot)
print('\nPost-Order:')
BinaryTree.PostOrder(TreeRoot)