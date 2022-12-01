# Creating BST class
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


    # Function to insert in BST
    def insert(self, data):
        # if value is lesser than the value of the parent node
        if data < self.data:
            if self.leftChild:
                # if we still need to move towards the left subtree
                self.leftChild.insert(data)
            else:
                self.leftChild = BinarySearchTree(data)
                return
        # if value is greater than the value of the parent node        
        else:
            if self.rightChild:
                # if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = BinarySearchTree(data)
                return


    # Function to search in BST
    def search(self, val):
        # if value to be searched is found
        if val==self.data:
            return str(val)+" is found in the BST"
        # if value is lesser than the value of the parent node
        elif val < self.data:

            # if we still need to move towards the left subtree
            if self.leftChild:
                # print(self.data)
                return self.leftChild.search(val)
            else:
                return str(val)+" is not found in the BST"
        # if value is greater than the value of the parent node
        else:
            # if we still need to move towards the right subtree
            if self.rightChild:
                # print(self.data)
                return self.rightChild.search(val)
            else:
                return str(val)+" is not found in the BST" 
       
            
    # function to print a BST
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.data)
        if self.rightChild:
            self.rightChild.PrintTree()
            
            
            
# Creating Binary Tree class
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


    def insert(self, data):
        if not self:
            root = BinaryTree(data)
            return
        q = []
        q.append(self)
    
        # Do level order traversal until we find
        # an empty place.
        while (len(q)):
            self = q[0]
            q.pop(0)
    
            if (not self.leftChild):
                self.leftChild = BinaryTree(data)
                break
            else:
                q.append(self.leftChild)
    
            if (not self.rightChild):
                self.rightChild = BinaryTree(data)
                break
            else:
                q.append(self.rightChild)


    # search will only serve as a helper function to execute ifExists
    def search(self, val):
        if self.ifExists(node=self, val=val):
            return str(val)+" is found in the Binary Tree"
        else:
            return str(val)+" is not found in the Binary Tree"
    
    
    # Function to search in Binary Tree. 
    def ifExists(self, node, val):
        # Preorder traversal
        # Check first if node exists
        if node == None:
            return False
        
        # Check data if matching
        if node.data == val:
            return True
        
        # If not, check left subtrees
        res1 = self.ifExists(node.leftChild, val)
        
        # If found, stop and return
        if res1:
            return True
        
        # Else, continue to right subtree
        res2 = self.ifExists(node.rightChild, val)
        
        return res2
    
      
    def PrintTree(self):
        # Inorder
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.data)
        if self.rightChild:
            self.rightChild.PrintTree()