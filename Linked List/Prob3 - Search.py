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

#Search function takes a keyword and where the linked list starts
def Search(Keyword, Head):
    #same system as loop
    SelectedNode = Head
    #except there is a counter to determine what node is currently being red
    i=0
    while (SelectedNode):
        #increments by 1 each loop to signify node number
        i += 1
        #checks the keyword matches the current node data
        if Keyword == SelectedNode.data:
            #prints the keyword and what node it is on through the increment counter
            print('Keyword:', Keyword, 'was found at node:', i)
            #ends the function entirely
            return
        #moves on to the next node
        SelectedNode = SelectedNode.next
    #This will only be printed if the keyword does not match anything on the linked list, otherwise the function will end if it finds the keyword before this point
    print('Keyword:', Keyword, 'not found')

FirstNode = nodes('Geralt', None)
SecondNode = nodes('Ciri', FirstNode)
ThirdNode = nodes('Yennefer', SecondNode)
FourthNode = nodes('Jaskier', ThirdNode)
FifthNode = nodes('Regis', FourthNode)
SixthNode = nodes('Milva', FifthNode)
SeventhNode = nodes('Cahir', SixthNode)
EigthNode = nodes('Yarpen', SeventhNode)
NineNode = nodes('Zoltan', EigthNode)

#Search function, searching for Milva starting from node head "FirstNode"
Search('Milva', FirstNode)