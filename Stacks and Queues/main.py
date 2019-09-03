def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

class StackNode():
    value = None
    nextNode = None

#problem 3.2 Stack Min -> Stack where push(), pop() and min() all operate in O(1) time
class Stack():
    top = None
    min = None
    
    def __init__(self):
        self.top = None
        self.min = None
    
    def push(self, value):
        temporaryNode = StackNode()
        temporaryNode.value = value
        if (self.top == None):
            self.top = temporaryNode
            self.min = value
        else:
            temporaryNode.nextNode = self.top
            self.top = temporaryNode
        if (value < self.min):
            self.min = value

    def pop(self):
        if (self.top != None):
            topValue = self.top.value
            if (self.top.nextNode != None):
                self.top = self.top.nextNode
            else:
                self.top = None
            if (topValue == self.min):
                self.updateMin()

    def printStack(self):
        iterator = stack.top
        resultingStack = "top -> "
        while (iterator != None):
            resultingStack += str(iterator.value) + " -> "
            iterator = iterator.nextNode
        resultingStack += "None"
        return resultingStack

    def peak(self):
        return self.top.value

    def updateMin(self):
        nodePointer = self.top
        min = None
        if (nodePointer!= None):
            min = nodePointer.value
        while (nodePointer != None):
            if (min < nodePointer.value):
                min = nodePointer.value
        self.min = min
                

class QueueNode:
    value = None
    prev = None

class Queue:
    front = None
    back = None
    
    def _init_(self):
        #these are going to be dummy nodes
        self.front = None
        self.back = None
    
    def add(self, value):
        temporaryNode = QueueNode()
        temporaryNode.value = value
        if (self.front == None and self.back == None):
            self.front = temporaryNode
            self.back = temporaryNode
            '''
                prev for both of these will point to none
                so front and back will point to the same unti another one is added and will take the place of the back
                '''
        else:
            self.back.prev  = temporaryNode
            self.back = temporaryNode

    def remove(self):
        if (self.front != None):
            if (self.front == self.back):
                tempNode = self.front
                self.front = None
                self.back = None
            else:
                tempNode = self.front
                self.front = self.front.prev
            return tempNode
        return None

    def printQueue(self):
        iterator = self.front
        l = list()
        while (iterator!=None):
            l.append(iterator.value.value)
            iterator = iterator.prev
        return l

    def isEmpty(self):
        if (self.front == None and self.front == None):
            return True
        else:
            return False

if __name__ == "__main__":
    print("Test Stack min")
    stack = Stack()
    print("push 2")
    stack.push(2)
    print("* Stack: ", stack.printStack())
    print("* min: ", str(stack.min))
    print("push 3")
    stack.push(3)
    print("* Stack: ", stack.printStack())
    print("* min: ", str(stack.min))
    print("push 4")
    stack.push(4)
    print("* Stack: ", stack.printStack())
    print("* min: ", str(stack.min))
    print("push 1")
    stack.push(1)
    print("* Stack: ", stack.printStack())
    print("* min: ", str(stack.min))
    print("push 5")
    stack.push(5)
    print("* Stack: ", stack.printStack())
    print("* min: ", str(stack.min))
