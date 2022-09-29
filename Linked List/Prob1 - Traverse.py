
#Establish node points for containing data
class nodes:
    #The node will require a data input which is stored in dataIn upon calling
    def __init__(self, DataIn, PrevNode):
        #The data given is dataIn is saved in the .data variable of the node
        self.data = DataIn
        #Creates an empty .next variable to be filled in later
        self.next = None
        #Checks if the PrevNode entry is not 'None' which is reserved for the head
        if PrevNode != None:
            #If the head is verified as not a Head node, it changes the previous node's "next" address as the current one
            PrevNode.next = self

#Traverse function will print out everything in the list, needs the first node to be specified
def Traverse(Head):
    #Start from the top, temp will be the selector
    SelectedNode = Head
    #Loops while temp still contains something
    while (SelectedNode):
        #Print the current selector's data
        print(SelectedNode.data)
        #Updates the temp variable to the next node
        SelectedNode = SelectedNode.next

#Inserting data to the linked list's head, previous node is stated as none
FirstNode = nodes('Geralt', None)
#Inserts data in the second node, The previous node is also specified to change the previous node's "Next" variable to the current one
SecondNode = nodes('Ciri', FirstNode)
#So on and so forth
ThirdNode = nodes('Yennefer', SecondNode)
FourthNode = nodes('Jaskier', ThirdNode)
FifthNode = nodes('Regis', FourthNode)
SixthNode = nodes('Milva', FifthNode)
SeventhNode = nodes('Cahir', SixthNode)
EigthNode = nodes('Yarpen', SeventhNode)
NineNode = nodes('Zoltan', EigthNode)

#Calls the traverse function to scroll through the entire list
Traverse(FirstNode)