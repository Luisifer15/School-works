
StackList = []
StackSize = None
ReversedStr = ""

class stack:
    def Init(Limit):
        global StackSize
        if Limit > 0:
            StackSize = int(Limit)
        else:
            print('Invalid Limit (Cannot be 0 or lower)')
            exit()
            

    def Push(Data):
        if StackSize == None:
            print("Stack not initialized")
        elif len(StackList) == StackSize:
            print("Stack overflow! cannot add element: " + Data)
        else:
            StackList.append(Data)


    def Pop():
        if StackSize == None:
            print("Stack not initialized")
        elif len(StackList) == 0:
            print("Stack already empty")
        else:
            return StackList.pop(len(StackList) - 1)


    def Peek():
        if StackSize == None:
            print("Stack not initialized")
        elif len(StackList) == 0:
            print("Stack is empty")
        else:
            print(StackList[len(StackList) - 1])


    def Traverse():
        if StackSize == None:
            print("Stack not initialized")
        elif len(StackList) == 0:
            print("Stack is empty")
        else:
            for i in range(len(StackList)):
                print(StackList[i])

    #Defines a custom function for reversing a given string
    def Reverse(InputStr):
        if StackSize == None:
            print("Stack not initialized")
        else:
            #Globalizes the ReversedStr to be accessed in this function
            global ReversedStr
            #Starts a for loop that goes through and pushes each character of the string to the stack
            for i in range(len(InputStr)):
                stack.Push(InputStr[i])
            #Starts another for loop that pops the stack and adds the popped element character to the ReversedStr string (which will result in a reversed text due to it starting at the end of the stack which is the last saved letter for the previous loop)
            for i in range(len(InputStr)):
                ReversedStr += stack.Pop()
            #Prints the entered string but reversed
            print(ReversedStr)


#string variable to be inputted to the function
str_sample = 'Did Hannah see bees? Hannah did.'

#Initializes stack with the size of the exact length of the string (!!THIS IS IMPORTANT!!)
stack.Init(len(str_sample))

#Calls the reverse command with the string variable input
stack.Reverse(str_sample)
