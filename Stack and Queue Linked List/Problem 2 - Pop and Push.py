

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

LinkedListStack1 = LLStack()

LinkedListStack1.PushNode('Michael')
LinkedListStack1.PushNode('Lily')
LinkedListStack1.PushNode('Scarra')
LinkedListStack1.PushNode('Imane')
LinkedListStack1.PushNode('Yvonne')
LinkedListStack1.PushNode('John')
LinkedListStack1.PushNode('Jodi')
LinkedListStack1.PushNode('Syndey')
LinkedListStack1.PushNode('Rachel')
LinkedListStack1.PushNode('Miyoung')
LinkedListStack1.PushNode('Leslie')
LinkedListStack1.PopNode()
LinkedListStack1.PopNode()
LinkedListStack1.PopNode()


LinkedListStack1.TraverseStack()

LinkedListStack1.PeekStack()


