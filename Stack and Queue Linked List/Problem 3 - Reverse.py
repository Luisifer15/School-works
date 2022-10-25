

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
                print(SelectedNode.data, sep="",end='')
                SelectedNode = SelectedNode.next
            print('\n')
        else:
            print('Stack empty')

    def ReverseStack(self):
        Reverse = LLStack()
        if self.Head != None:
            SelectedNode = self.Head
            while (SelectedNode):
                Reverse.PushNode(SelectedNode.data)
                SelectedNode = SelectedNode.next
            Reverse.TraverseStack()
        else:
            print('Stack empty')



LinkedListStack1 = LLStack()
LinkedListStack1.PushNode('/')
LinkedListStack1.PushNode('/')
LinkedListStack1.PushNode('N')
LinkedListStack1.PushNode('O')
LinkedListStack1.PushNode('.')
LinkedListStack1.PushNode('F')
LinkedListStack1.PushNode('U')
LinkedListStack1.PushNode('T')
LinkedListStack1.PushNode('U')
LinkedListStack1.PushNode('R')
LinkedListStack1.PushNode('E')
LinkedListStack1.PushNode('_')


LinkedListStack1.TraverseStack()
LinkedListStack1.ReverseStack()


