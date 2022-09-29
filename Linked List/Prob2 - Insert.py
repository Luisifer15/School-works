class nodes:
    def __init__(self, DataIn, PrevNode):
        self.data = DataIn
        self.next = None
        if PrevNode != None:
            PrevNode.next = self

def Traverse(Head):
    SelectedNode = Head
    while (SelectedNode):
        print(SelectedNode.data)
        SelectedNode = SelectedNode.next

#Insert function will require the new Data and a node, the data will be inserted after the given node
def Insert(DataIn, PrevNode):
    #the previous node's next address is saved in a new variable called PrevNext
    PrevNext = PrevNode.next 
    #Inserts a new data using the node class, the previous node's next address is overwritten which is why it was saved to a new variable prior, will cause an infinite loop otherwise 
    Inserted = nodes(DataIn, PrevNode)
    #the original Previous Node's (pre-overwrite) next address is transfered to the newly inserted next address
    Inserted.next = PrevNext


FirstNode = nodes('Geralt', None)
SecondNode = nodes('Ciri', FirstNode)
ThirdNode = nodes('Yennefer', SecondNode)
FourthNode = nodes('Jaskier', ThirdNode)
FifthNode = nodes('Regis', FourthNode)
SixthNode = nodes('Milva', FifthNode)
SeventhNode = nodes('Cahir', SixthNode)
EigthNode = nodes('Yarpen', SeventhNode)

#Inserts the data 'Triss' after the Third Node
Insert('Triss', ThirdNode)

Traverse(FirstNode)