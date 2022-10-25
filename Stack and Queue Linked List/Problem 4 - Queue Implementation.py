class LLnode:
    def __init__(self, DataIn):
        self.data = DataIn
        self.next = None

class LLStack:
    def __init__(self):
        self.Head = None

    def Enqueue(self, DataIn):
        if self.Head != None:
            PushedNode = LLnode(DataIn)
            PushedNode.next = self.Head
            self.Head = PushedNode
            #print('Insert Success')
        else:
            self.Head = LLnode(DataIn)
            #print('Insert head success')

    def Dequeue(self):
        if self.Head != None:
            SelectedNode = self.Head
            while (SelectedNode):
                if self.Head.next == None: 
                    Output = self.Head.data
                    self.Head = None
                    return Output
                elif SelectedNode.next.next == None:
                    Output = SelectedNode.next.data
                    SelectedNode.next = None
                    return Output
                else:
                    SelectedNode = SelectedNode.next
        else:
            print('There is nothing to Dequeue')
            return None

    def PeekQueue(self):
        if self.Head != None:
            SelectedNode = self.Head
            while (SelectedNode):
                if SelectedNode.next == None:
                    print(SelectedNode.data)
                    return SelectedNode.data
                else:
                    SelectedNode = SelectedNode.next
        else:
            print('There is nothing in the queue')
            return None

    def TraverseQueue(self):
        if self.Head != None:
            SelectedNode = self.Head
            while (SelectedNode):
                print(SelectedNode.data)
                SelectedNode = SelectedNode.next
        else:
            print('Stack empty')
