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
def partition(list, partitionValue):
    if (list.head == None):
        return "Error, Empty list"
    partitionLeftPointer = list.head
    partitionRightPointer = list.head
    partitionPointer = list.head
    #find first two partitioning elements
    while (partitionLeftPointer.value >= partitionValue):
        if (partitionLeftPointer.next == None):
            #do not go any further
            break
        partitionLeftPointer = partitionLeftPointer.next 
    while (partitionRightPointer.value < partitionValue):
        if (partitionLeftPointer.next == None):
            #do not go any further
            break
        partitionRightPointer = partitionRightPointer.next 
    newHeadPointer = partitionLeftPointer #keep track of new list head
    rightPartitionHead = partitionRightPointer
    while (partitionPointer != None):
        if (partitionPointer.value < partitionValue):
            if (partitionPointer != partitionLeftPointer):
                partitionLeftPointer.next = partitionPointer
                partitionLeftPointer = partitionPointer
        else:
            if (partitionPointer != partitionRightPointer):
                partitionRightPointer.next = partitionPointer
                partitionRightPointer = partitionPointer
        partitionPointer = partitionPointer.next
    partitionLeftPointer.next = rightPartitionHead #combine two partitions
    partitionRightPointer.next = None #make sure it stops here
    partitionedList = LinkedList()
    partitionedList.head = newHeadPointer
    return partitionedList.printList()

# Problem 2.4
def sumLists(firstList, secondList):
    firstNodePointer = firstList.head
    secondNodePointer = secondList.head
    newSumList = LinkedList()
    carryValue = 0
    while (firstNodePointer!=None or secondNodePointer != None): #both must equal none
        instantSum = 0 #keep track of sum
        instantSum += carryValue
        if (firstNodePointer != None):
            instantSum += firstNodePointer.value
            firstNodePointer = firstNodePointer.next 
        if (secondNodePointer != None):
            instantSum += secondNodePointer.value
            secondNodePointer = secondNodePointer.next
        if (instantSum >= 10):
            carryValue = 1
            newSumList.appendToTail(instantSum % 10)
        else: 
            carryValue = 0
            newSumList.appendToTail(instantSum)
    resultAsString = ""
    newListPointer = newSumList.head
    while (newListPointer != None):
        resultAsString = str(newListPointer.value) + resultAsString
        newListPointer = newListPointer.next
    return str(newSumList.printList()) + " : " + str(resultAsString)

if __name__ == "__main__":
    print("Test Remove Dups")
    list = LinkedList()
    list.appendToTail(5)
    list.appendToTail(9)
    list.appendToTail(5)
    list.appendToTail(3)
    removeDups(list)
    check(list.printList(), "5->9->3->None")

    print("---------------------------------")
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

    print("---------------------------------")
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

    print("---------------------------------")
    print("Test partition")
    list = LinkedList()
    list.appendToTail(3)
    list.appendToTail(5)
    list.appendToTail(8)
    list.appendToTail(5)
    list.appendToTail(10)
    list.appendToTail(2)
    list.appendToTail(1)
    print("current list: ", list.printList())
    print("partition around 5: ", partition(list, 5))

    print("---------------------------------")
    print("Test Sum Lists")
    list1 = LinkedList()
    list1.appendToTail(7)
    list1.appendToTail(1)
    list1.appendToTail(6)
    list2 = LinkedList()
    list2.appendToTail(5)
    list2.appendToTail(9)
    list2.appendToTail(2)
    print("7->1->6")
    print("+")
    print("5->9->2")
    print("=")
    print(sumLists(list1, list2))
    print("---------")
    list1 = LinkedList()
    list1.appendToTail(2)
    list1.appendToTail(1)
    list1.appendToTail(0)
    list1.appendToTail(1)
    list2 = LinkedList()
    list2.appendToTail(5)
    list2.appendToTail(9)
    list2.appendToTail(2)
    print("2->1->0->1")
    print("+")
    print("5->9->2")
    print("=")
    print(sumLists(list1, list2))