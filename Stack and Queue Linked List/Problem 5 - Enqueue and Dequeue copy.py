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

LinkedListStack1 = LLStack()

LinkedListStack1.Enqueue('Yennefer')
LinkedListStack1.Enqueue('Cirilla')
LinkedListStack1.Enqueue('Philippa')
LinkedListStack1.Enqueue('Margarita')
LinkedListStack1.Enqueue('Triss')
LinkedListStack1.Enqueue('Keira')
LinkedListStack1.Enqueue('Sabrina')
LinkedListStack1.Enqueue('Sheala')
LinkedListStack1.Enqueue('Francesca')
LinkedListStack1.Enqueue('Assire')
LinkedListStack1.Enqueue('Fringilla')
LinkedListStack1.Enqueue('Ida')
LinkedListStack1.Dequeue()
LinkedListStack1.Dequeue()


LinkedListStack1.TraverseQueue()
LinkedListStack1.PeekQueue()