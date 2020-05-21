class QueueNode:
    value = None
    prev = None

    def __init__(self, value):
        self.value = value

class Queue:
    front = None
    back = None
    
    def _init_(self):
        #these are going to be dummy nodes
        self.front = None
        self.back = None
    
    def add(self, value):
        temporaryNode = QueueNode(value)
        if (self.front == None and self.back == None):
            self.front = temporaryNode
            self.back = temporaryNode
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

    def isEmpty(self):
        if (self.front == None and self.front == None):
            return True
        else:
            return False
