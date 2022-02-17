#### Node Class -- constructor #####

class ListNode:
    def __init__(self, value, ptr):
        self.value = value
        self.ptr = ptr 

### Global Variable HeadNode ### 

HeadNode = None

### Create empty List ###

def InitialiseLinkedList():
    global HeadNode
    node4 = ListNode(40, None)
    node3 = ListNode(30, node4)
    node2 = ListNode(20, node3)
    node1 = ListNode(10, node2)
    HeadNode = node1

#### Delete entire list #### HEAD POINTER TO NULL

def ClearLinkedList():
    global HeadNode
    HeadNode.ptr = None


#### Check if Linked List is empty ### if Head.ptr == None 

def isEmpty():
    return HeadNode.ptr == None

##################################

def printList():
    global HeadNode
    current = HeadNode
    if(current != None):
        while(current.ptr != None):
            print(current.value)
            current = current.ptr
        print(current.value)
    else:
        print("The list is empty")


# printList()


#####################################

def addNode(N, pos):
    global HeadNode
    current = HeadNode
    counter = 1
    newNode = ListNode(N, None)
    if(pos == 0):
        HeadNode = newNode
        newNode.ptr = current
        print("Value", N, "added to position", pos)
    else:
        while(pos > counter):
            current = current.ptr
            counter += 1
        newNode.ptr = current.ptr
        current.ptr = newNode
        print("Value", N, "added to position", pos)

    

# addNode(50,4)
# printList()


#########################################

def DeleteNode(N):
    global HeadNode
    Previous = None
    current = HeadNode
    if(N == current.value):
        HeadNode = current.ptr
    else:
        while((current.ptr != None) and (current.value != N)):
            Previous = current
            current = current.ptr
        if(current.ptr == None and current.value != N):
            print("The value does not appear to be on this List")
        else:
            print("Node deleted with value === ", current.value)
            Previous.ptr = current.ptr
    


# DeleteNode(30)
# printList()

######################### findANode ############

def findNode(N):
    global HeadNode
    current = HeadNode
    while(N != current.value and current.ptr != None):
            current = current.ptr
    if(current.ptr == None):
        print(N, "not found on this LinkList")
    else:
        print("Found value on the list.... value is: ", current.value, " at address: ", current)
    



############### Menu #####################

def Menu():
    print   ("1 --- Create a Linked List\n"
            "2 --- Delete a Linked List\n"
            "3 --- Check if a LInked List is empty\n" 
            "4 --- Print out the values in the list\n"
            "5 --- Find a node in a LInked List\n"
            "6 --- Insert a node in a Linked List\n"
            "7 --- Delete a node from a Linked List\n"
            "99 ---Exit" )

    option = int(input("Select an option "))
    while(option != 99):
        if(option == 1):
            InitialiseLinkedList()
            print(HeadNode)
            #Recursive Call
            Menu()
        if(option == 2):
            ClearLinkedList()
            print(HeadNode.ptr)
            print("Linked List has been deleted")
            Menu()
        if(option == 3):
            if(isEmpty()):
                print("The list is empty")
            else:
                print("The list is not empty")
            Menu()
        if(option == 4):
            printList()
            Menu()
        if(option == 5):
            inputNode = int(input("Please enter the node value to be found "))
            findNode(inputNode)
            Menu()
        if(option == 6):
            NValue = int(input("Enter the value of the node to be inserted "))
            NPos = int(input("Enter the position you want the node to be inserted at "))
            addNode(NValue, NPos)
            Menu()
        if(option == 7):
            DNode = int(input("Enter value of node to be deleted"))
            DeleteNode(DNode)
            Menu()
        else:
            return
    print("Good Bye")

############# END MENU #######################

##### MAIN ######

Menu()



