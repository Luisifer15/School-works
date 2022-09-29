
#Establish node points for containing data
class node:
    #The node will require a data input which is stored in dataIn upon calling
    def __init__(self, DataIn):
        #The data inputted is dataIn is saved in the .data variable of the node
        self.data = DataIn
        #Creates an empty .next variable to be filled in later
        self.next = None

#Establish the linked list
class linkedList:
    #Starts off with an empty head
    def __init__(self):
        self.HeadNode = None
    #Creates a traverse function to print out everything in the list
    def Traverse(self):
        #Start from the top, temp will be the selector
        temp = self.HeadNode
        #Loops while temp still contains something
        while (temp):
            #Print the current selector's data
            print(temp.data)
            #Updates the temp variable to the next node
            temp = temp.next

def insertAfter(prev_node, new_data):
 
    # 1. check if the given prev_node exists
 
    # 2. Create new node &
    # 3. Put in the data
        new_node = node(new_data)
 
    # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
 
    # 5. make next of prev_node as new_node
        prev_node.next = new_node



#Initialize linked list
List = linkedList()

#Inserting data to the linked list's head
List.HeadNode = node('Geralt')

#Inserts data in the second node
SecondNode = node('Ciri')
#Links the head node to the second node and so on
List.HeadNode.next = SecondNode
ThirdNode = node('Yennefer')
SecondNode.next = ThirdNode
FourthNode = node('Jaskier')
ThirdNode.next = FourthNode
FifthNode = node('Regis')
FourthNode.next = FifthNode
SixthNode = node('Milva')
FifthNode.next = SixthNode
SeventNode = node('Cahir')
SixthNode.next = SeventNode

insertAfter(ThirdNode, 'Triss')
#Calls the traverse function to scroll through the entire list
List.Traverse()