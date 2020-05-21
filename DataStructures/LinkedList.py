class ListNode():
    value = None
    next = None
    
    def __init__(self, value):
        self.value = value

class LinkedList():
    head = None
    
    def _init_(self):
        self.head = None

    def appendToTail(self, value):
        tempNode = ListNode(value)
        tempNode.value = value
        if (self.head == None):
            self.head = tempNode
        else:
            iterator = self.head
            while (iterator.next != None):
                iterator = iterator.next
            iterator.next = tempNode

    def printList(self):
        result = ""
        iterator = self.head
        while (iterator != None):
            result += str(iterator.value) + "->"
            iterator = iterator.next
        result += "None"
        return result