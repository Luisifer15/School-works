#Starts an empty list
StackList = []
#Sets an empty variable to be used to determine stack limit
StackSize = None

#Decalres custome class named "stack"
class stack:

    #Defines a custom function for initializing stacks with the input as the stack limit; Without the limit, the code determines the Stack list as non existant
    def Init(Limit):
        #Globalized the variable StackSize in order to have the access inside the custom function
        global StackSize
        #Checks if the limit entered is greater than zero
        if Limit > 0:
            #Sets limit
            StackSize = int(Limit)
        #Zero and below will not be accepted and the program will close
        else:
            print('Invalid Limit (Cannot be 0 or lower)')
            exit()
            
    #Defines a custom function for pushing elements at the end of the stack
    def Push(Data):
        #Checks if the stack limit is currently undeclared which will be considered as an uninitialized stack
        if StackSize == None:
            print("Stack not initialized")
        #Checks if the current StackList length matches the limit which will be a stack overflow
        elif len(StackList) == StackSize:
            print("Stack overflow! cannot add element: " + Data)
        else:
        #If the the failchecks are successful, the entered data will be inserted in the stack
            StackList.append(Data)

    #Defines a custom function for popping the last added element in the stack
    def Pop():
        #Checks if the stack limit is currently undeclared which will be considered as an uninitialized stack
        if StackSize == None:
            print("Stack not initialized")
        #Checks if the stack is currently empty, nothing to pop
        elif len(StackList) == 0:
            print("Stack already empty")
        #If the failchecks are successful, the most recent element will be popped; the length of the stacklist minus one is essential for accessing the index number of the element in the list as the indexing starts with 0 for the very first element
        else:
            return StackList.pop(len(StackList) - 1)

    #Defines a custom function for peeking the last added element without popping
    def Peek():
        #Checks if the stack limit is currently undeclared which will be considered as an uninitialized stack
        if StackSize == None:
            print("Stack not initialized")
        #Checks if the stack is currently empty
        elif len(StackList) == 0:
            print("Stack is empty")
         #If the failchecks are successful, the most recent element will be printed; the function can also be used to return the last element for copying or other external uses
        else:
            print(StackList[len(StackList) - 1])
            return StackList[len(StackList) - 1]

    #Defines a custom function for printing the entire stack's contents
    def Traverse():
        #Checks if the stack limit is currently undeclared which will be considered as an uninitialized stack
        if StackSize == None:
            print("Stack not initialized")
        #Checks if the stack is currently empty
        elif len(StackList) == 0:
            print("Stack is empty")
        #If the failchecks are successful, a forloop starts for printing each elements
        else:
            for i in range(len(StackList)):
                print(StackList[i])

#Initializes stack with the size of 5
stack.Init(5)

#Pushes elements to the stack
stack.Push("V")
stack.Push("Johnny Silverhand")
stack.Push("Panam")
stack.Push("Judy")
stack.Push("Alt Cunningham")

#Tries to push a 6th element but will return a stack overflow due to the stack size being limited to only 5
stack.Push("Jackie Welles")

#Shows all contents of a stack
stack.Traverse()

#Pops the last element in the stack (Alt Cunningham)
stack.Pop()

#Peeks the new element after the pop (in this case, its now Judy since Alt Cunningham has been popped)
stack.Peek()