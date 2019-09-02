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

    def delete(self, value):
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

def kth(list):
    midPointer = list.head
    runnerPointer = list.head
    while (runnerPointer.next != None):
        #by the end midPointer will be in the middle. 
        midPointer = midPointer.next
        runnerPointer = runnerPointer.next.next
    

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

