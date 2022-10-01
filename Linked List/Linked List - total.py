
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

#Modified Traverse code
def Total(Head):
    #Declare empty sum variable
    Sum = 0
    #Start from the top, temp will be the selector
    SelectedNode = Head
    #Loops while temp still contains something
    while (SelectedNode):
        #Increments the sum variable with the converted integer value of the currently selected node
        Sum += int(SelectedNode.data)
        #Print the current selector's data
        print(SelectedNode.data)
        #Updates the temp variable to the next node
        SelectedNode = SelectedNode.next
    #prints Total
    print(Sum)

#Inserting data to the linked list's head, previous node is stated as none
FirstNode = nodes('10', None)
#Inserts data in the second node, The previous node is also specified to change the previous node's "Next" variable to the current one
SecondNode = nodes('10', FirstNode)
#So on and so forth
ThirdNode = nodes('10', SecondNode)
FourthNode = nodes('10', ThirdNode)
FifthNode = nodes('10', FourthNode)
SixthNode = nodes('10', FifthNode)
SeventhNode = nodes('10', SixthNode)
EigthNode = nodes('10', SeventhNode)
NineNode = nodes('10', EigthNode)

#Calls the total function to scroll through the entire list and summing up every node's value
Total(FirstNode)