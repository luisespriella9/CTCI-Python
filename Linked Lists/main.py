def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

class ListNode():
    value = None
    nextNode = None
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
            while (iterator.nextNode != None):
                iterator = iterator.nextNode
            iterator.nextNode = tempNode

    def deleteNode(self, value):
        iterator = self.head
        if (self.head.value == value):
            if (self.head.nextNode != None):
                self.head = self.head.nextNode
            else:
                self.head = None
            return
        while (iterator.nextNode != None):
            if (iterator.nextNode.value == value):
                if (iterator.nextNode.nextNode != None):
                    iterator.nextNode = iterator.nextNode.nextNode
                else:
                    iterator.nextNode = None
                break
            iterator = iterator.nextNode

    def printList(self):
        result = ""
        iterator = self.head
        while (iterator != None):
            result += str(iterator.value) + "->"
            iterator = iterator.nextNode
        result += "None"
        return result

# Problem 2.1
def removeDups(list):
    nodePointer = list.head
    #pointer to current node and pointer to check rest of the nodes inside the list
    while nodePointer != None:
        nodeRunner = nodePointer
        while (nodeRunner.nextNode != None):
            if nodeRunner.nextNode.value == nodePointer.value:
                nodeRunner.nextNode = nodeRunner.nextNode.nextNode #skip
            nodeRunner = nodeRunner.nextNode
        nodePointer = nodePointer.nextNode
    return list

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

