def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

class ListNode():
    value = None
    next = None
class LinkedList():
    head = None
    
    def _init_(self):
        self.head = None

    def appendToTail(self, value):
        tempNode = ListNode()
        tempNode.value = value
        if (self.head == None):
            self.head = tempNode
        else:
            iterator = self.head
            while (iterator.next != None):
                iterator = iterator.next
            iterator.next = tempNode

    def remove(self, value):
        iterator = self.head
        if (self.head.value == value):
            if (self.head.next != None):
                self.head = self.head.next
            else:
                self.head = None
            return
        while (iterator.next != None):
            if (iterator.next.value == value):
                if (iterator.next.next != None):
                    iterator.next = iterator.next.next
                else:
                    iterator.next = None
                break
            iterator = iterator.next

    def printList(self):
        result = ""
        iterator = self.head
        while (iterator != None):
            result += str(iterator.value) + "->"
            iterator = iterator.next
        result += "None"
        return result

# Problem 2.1
def removeDups(list):
    nodePointer = list.head
    #pointer to current node and pointer to check rest of the nodes inside the list
    while nodePointer != None:
        nodeRunner = nodePointer
        while (nodeRunner.next != None):
            if nodeRunner.next.value == nodePointer.value:
                nodeRunner.next = nodeRunner.next.next #skip
            nodeRunner = nodeRunner.next
        nodePointer = nodePointer.next
    return list

# Problem 2.2
def kth(list, k):
    midPointer = list.head
    runnerPointer = list.head
    length = 0
    #calculate length, midPointer will be in position length/2-1 starting from position 0. 
    while (runnerPointer != None):
        #by the end midPointer will be in the middle. 
        if (runnerPointer == None):
            break
        elif (runnerPointer.next == None):
            length+=1
            break
        else:
            length += 2
        midPointer = midPointer.next
        runnerPointer = runnerPointer.next.next
    midNodePosition = length/2-1
    finalNodePosition = length-1
    if (length-1-k < 0):
        return "Not Possible to find"
    elif (length-1-k > midNodePosition): 
        #check if to the right of middle. Iterate right from middle
        iterations = int(length-1-midNodePosition-k)
        for i in range(iterations):
            midPointer = midPointer.next
        return midPointer.value
    else:
        #to the left of middle. Iterate right from head
        iterations = int(length-1-k)
        pointerFromHead = list.head
        for i in range(iterations):
            pointerFromHead = pointerFromHead.next
        return pointerFromHead.value

# Problem 2.3
def deleteMiddleNode(list):
    previousToMidNode = list.head
    runnerPointer = list.head
    while (runnerPointer != None):
        #by the end midPointer will be in the middle. 
        if (runnerPointer.next == None):
            break
        elif(runnerPointer.next.next == None):
            runnerPointer = runnerPointer.next
            break
        if runnerPointer != list.head:
            #delay by one
            previousToMidNode = previousToMidNode.next
        runnerPointer = runnerPointer.next.next
    if (previousToMidNode != None):
        if (previousToMidNode.next != None and previousToMidNode.next != runnerPointer):
            #check if middle node, then remove
            previousToMidNode.next = previousToMidNode.next.next
    return list.printList()

# Problem 2.4
def partition():
    print("partition")

if __name__ == "__main__":
    print("Test Remove Dups")
    list = LinkedList()
    list.appendToTail(5)
    list.appendToTail(9)
    list.appendToTail(5)
    list.appendToTail(3)
    removeDups(list)
    check(list.printList(), "5->9->3->None")

    print("Test return Kth to last")
    check(kth(list, 1), 9) #list from previous test
    list = LinkedList()
    list.appendToTail(0)
    list.appendToTail(1)
    list.appendToTail(2)
    list.appendToTail(3)
    list.appendToTail(4)
    list.appendToTail(5)
    list.appendToTail(6)
    check(kth(list, 2), 4)
    check(kth(list, 4), 2)

    print("Test delete middle node")
    print("current list: ", list.printList())
    print("delete middle node: ", deleteMiddleNode(list))
    print("delete middle node: ", deleteMiddleNode(list))
    print("delete middle node: ", deleteMiddleNode(list))
    print("delete middle node: ", deleteMiddleNode(list))
    print("delete middle node: ", deleteMiddleNode(list))
    print("delete middle node: ", deleteMiddleNode(list))
    list = LinkedList()
    list.appendToTail("a")
    list.appendToTail("b")
    list.appendToTail("c")
    list.appendToTail("d")
    list.appendToTail("e")
    list.appendToTail("f")
    print("current list: ", list.printList())
    print("delete middle node: ", deleteMiddleNode(list))

    print("Test partition")
