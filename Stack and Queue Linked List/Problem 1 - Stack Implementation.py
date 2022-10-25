 

class LLnode:
    def __init__(self, DataIn):
        self.data = DataIn
        self.next = None

class LLStack:
    def __init__(self):
        self.Head = None

    def PushNode(self, DataIn):
        if self.Head != None:
            PushedNode = LLnode(DataIn)
            PushedNode.next = self.Head
            self.Head = PushedNode
            #print('Insert Success')
        else:
            self.Head = LLnode(DataIn)
            #print('Insert head success')

    def PopNode(self):
        if self.Head != None:
            ZombieNode = self.Head
            self.Head = self.Head.next
            ZombieNode.next = None
            #print('Pop Success')
            return ZombieNode.data
        else:
            print('There is nothing to pop')
            return None

    def PeekStack(self):
        if self.Head != None:
            print(self.Head.data)
            return self.Head.data
        else:
            print('Stack empty')
            return None

    def TraverseStack(self):
        if self.Head != None:
            SelectedNode = self.Head
            while (SelectedNode):
                print(SelectedNode.data)
                SelectedNode = SelectedNode.next
        else:
            print('Stack empty')


