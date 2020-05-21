class Node():
    value = None
    left = None
    right = None
    def __init__(self, value):
        self.value = value


class BinarySearchTree:
    root = None

    def insert(self, value):
        if type(value) == type([]):
            for val in value:
                self.insertHelper(val)
        else:
                self.insertHelper(value)

    def insertHelper(self, value):
        nodeToInsert = Node(value)
        if (self.root == None):
            self.root = nodeToInsert
            return
        self.insertRecursively(self.root, nodeToInsert)
    
    def insertRecursively(self, node, nodeToInsert):
        if (nodeToInsert.value < node.value):
            #insert left
            if (node.left == None):
                node.left = nodeToInsert
                return
            self.insertRecursively(node.left, nodeToInsert) #traverse left
        elif (nodeToInsert.value > node.value):
            #insert right
            if (node.right == None):
                node.right = nodeToInsert
                return
            self.insertRecursively(node.right, nodeToInsert) #traverse right