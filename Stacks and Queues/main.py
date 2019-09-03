def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

class StackNode():
    value = None
    nextNode = None

class Stack():
    top = None
    
    def __init__(self):
        self.top = None
    
    def push(self, value):
        temporaryNode = StackNode()
        temporaryNode.value = value
        
        if (self.top == None):
            self.top = temporaryNode
        else:
            temporaryNode.nextNode = self.top
            self.top = temporaryNode

    def pop(self):
        if (self.top != None):
            if (self.top.nextNode != None):
                self.top = self.top.nextNode
            else:
                self.top = None

    def printStack(self):
        iterator = stack.top
        l = list()
        while (iterator != None):
            l.append(iterator.value)
            iterator = iterator.nextNode
        return l

    def peak(self):
        return self.top.value

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