    
class GraphNode:
    name = ""
    children = []
    def __init__(self, name):
        self.name = name

    def addEdge(self, child):
        self.children.append(child)

class Graph:
    #implementation of directed graph
    nodes = []

    def addNode(self, name):
        graphNode = graphNode(name)
        self.nodes.append(graphNode)

    def addEdge(self, pointingNodeName, pointerNodeName):
        #find two nodes if they exists, if not then do nothing
        pointerNode = None
        pointingNode = None
        for node in nodes:
            if (node.name == pointingNodeName):
                pointingNode = node
            if (node.name == pointerNodeName):
                pointerNode = node
        if (pointerNode == None or pointingNode == None):
            return
        #add edge from pointing node to the pointer node
        pointingNode.addEdge(pointerNode)

class BinaryNode():
    value = None
    left = None
    right = None

class BinarySearchTree():
    root = None
    #initializing Binary search tree
    def _init_(self):
        self.root = None
    
    def insert(self, value):
        if (self.root == None):
            self.root = BinaryNode()
            self.root.value = value
        else:
            self.insertValue(self.root, value)
    
    def insertValue(self, node, value):
        #recursive
        if (value < node.value):
            if (node.left == None):
                node.left = BinaryNode()
                node.left.value = value
                return
            else:
                self.insertValue(node.left, value)
        elif (value > node.value):
            if (node.right == None):
                node.right = BinaryNode()
                node.right.value = value
                return
            else:
                self.insertValue(node.right, value)
    
    #prints the tree in order
    # left, root, right
    #prints this as a list
    def printInOrder(self):
        l = list()
        return self.inOrder(node = self.root, l = l)
    
    def inOrder(self, node, l):
        if (node.left != None):
            self.inOrder(node.left, l)
        l.append(node.value)
        if (node.right != None):
            self.inOrder(node.right, l)
        return l
    
    def find(self, value):
        return self.findValue(self.root, value)
    
    def findValue(self, node, value):
        if (node.value == value):
            return True
        if (node.left != None and value < node.value):
            return self.findValue(node.left, value)
        if (node.right != None and value > node.value):
            return self.findValue(node.right, value)
        return False
    
    #finds min of tree or subtree
    def findMin(self, node):
        if (node.left == None):
            return node
        else:
            return self.findMin(node.left)
    
    def delete(self, value):
        if (self.root.value == value):
            temporaryNode = self.findMin(self.root.right)
            deleteValue(temporaryNode)
            self.root = temporaryNode
        else:
            if (self.find(value)):
                self.deleteValue(self.root, value)
    
    #keep track of parent
    def deleteValue(self, node, value):
        #base cases
        #leaf, aka no children
        if (node.value == value):
            if (node.left == None and node.right == None):
                return None
            #one children at the left
            elif (node.left != None and node.right == None):
                return node.left
            #one children at the right
            elif (node.left == None and node.right != None):
                return node.right
            else:
                #two children
                temporaryNode = BinaryNode()
                temporaryNode.value = self.findMin(node.right).value
                temporaryNode.left = node.left
                temporaryNode.right = node.right
                self.delete(temporaryNode.value)
                return temporaryNode
        if (value < node.value):
            if (node.left != None):
                if (node.left.value == value):
                    node.left = self.deleteValue(node.left, value)
                else:
                    self.deleteValue(node.left, value)
        elif (value > node.value):
            if (node.right != None):
                if (node.right.value == value):
                    node.right = self.deleteValue(node.right, value)
                else:
                    self.deleteValue(node.right, value)

class BinaryTree():
    root = None
    #initializing binary tree
    
    def _init_(self):
        self.root = None
    
    def printInOrder(self):
        l = list()
        return self.inOrder(node = self.root, l = l)
    
    def inOrder(self, node, l):
        if (node.left != None):
            self.inOrder(node.left, l)
        l.append(node.value)
        if (node.right != None):
            self.inOrder(node.right, l)
        return l
    
    def insert(self, value):
        #insert into binary tree
        if (self.root == None):
            temporaryNode = BinaryNode()
            temporaryNode.value = value
            self.root = temporaryNode
        else:
            self.insertValue(self.root, value)
    '''
        since we are inserting always at the left most end we will have to use a queue and do breadth first search to explore from left to right at the same level
        '''
    def insertValue(self, node, value):
        nodeToInsert = BinaryNode()
        nodeToInsert.value = value
        queue = Queue()
        queue.enqueue(node)
        while (not queue.isEmpty()):
            tempNode = queue.dequeue()
            if (tempNode.value.left == None):
                tempNode.value.left = nodeToInsert
                return tempNode
            elif (tempNode.value.right == None):
                tempNode.value.right = nodeToInsert
                return tempNode
            queue.enqueue(tempNode.value.left)
            queue.enqueue(tempNode.value.right)

    def checkIfBST(self):
        #hard for it to be a BST since it must also be a complete binary tree and somehow all elements had to be added in the perfect way since a binary adds from left to right from level to level
        return self.BST(node = self.root)
    
    def BST(self, node, minimum = None, maximum=None):
        if (minimum == None and maximum != None):
            if (node.value > maximum):
                return False
        elif (minimum != None and maximum == None):
            if (node.value < minimum):
                return False
        elif (minimum != None and maximum != None):
            if (node.value < minimum or node.value > maximum):
                return False
        #do nothing if both equal none, aka root whose min and max should be none
        if (node.left != None and node.right != None):
            if (self.BST(node.left, minimum, node.value) == False or self.BST(node.right, node.value, maximum) == False):
                return False
            else:
                return True
        if (node.left != None):
            self.BST(node.left, minimum, node.value)
        #max is now its root
        if (node.right != None):
            self.BST(node.right, node.value, maximum)
        return True