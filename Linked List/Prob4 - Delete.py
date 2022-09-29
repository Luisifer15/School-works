
class nodes:
    def __init__(self, DataIn, PrevNode):
        self.data = DataIn
        self.next = None
        if PrevNode != None:
            PrevNode.next = self

#Modified Traverse function, skips the original head node if deleted by the function
def Traverse(Head):
    if Head.data == None:
        SelectedNode = Head.next
    else:
        SelectedNode = Head
    while (SelectedNode):
        print(SelectedNode.data)
        SelectedNode = SelectedNode.next

#Delete function takes two inputs, the node to be deleted and the head node of the linked list
def Delete(DelNode, Head):
    #Combs the entire linked list
    SelectedNode = Head
    #If the Node to be deleted matches the head node, it will clear the data, important for the traverse function
    if DelNode == Head:
        Head.data = None
    #Proceeds to this otherwise
    else:
        #usual traversing loop
        while (SelectedNode):
            #checks if the node to be deleted matches the selected node's next address
            if DelNode == SelectedNode.next:
                #changes the currently selected node's next address to the node after the deleted node
                SelectedNode.next = SelectedNode.next.next
                #Prints a success message and prints the entire list right after
                print('Delete Successful!, Here is the new linked list: ')
                Traverse(FirstNode)
                return
            #looping procedure
            SelectedNode = SelectedNode.next
        #Will only be executed if the DelNode given is not on the node
        print('Node not found')

#Random variable for debugging the not found message because the compiler does not accept nonvariables
RandomVar = 'Vilgefortz'
FirstNode = nodes('Geralt', None)
SecondNode = nodes('Ciri', FirstNode)
ThirdNode = nodes('Yennefer', SecondNode)
FourthNode = nodes('Jaskier', ThirdNode)
FifthNode = nodes('Regis', FourthNode)
SixthNode = nodes('Milva', FifthNode)
SeventhNode = nodes('Cahir', SixthNode)
EigthNode = nodes('Yarpen', SeventhNode)
NinthNode = nodes('Zoltan', EigthNode)

#Execute delete function, format: (Node to be deleted, head node of the linked list to scour)
Delete(FifthNode, FirstNode)

