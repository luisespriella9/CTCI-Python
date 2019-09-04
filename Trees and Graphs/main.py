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

    def isEmpty(self):
        if (self.front == None and self.front == None):
            return True
        else:
            return False

class Node():
    value = None
    left = None
    right = None
    def __init__(self, value):
        self.value = value

class BinaryTree:
    root = None

    def insert(self, value):
        nodeToInsert = Node(value)
        if (self.root == None):
            self.root = nodeToInsert
            return
        nodeQueue = Queue()
        nodeQueue.add(self.root)
        while (not nodeQueue.isEmpty()):
            node = nodeQueue.remove().value #this will be a tree Node
            if (node.left == None):
                node.left = nodeToInsert
                return
            elif (node.right == None):
                node.right = nodeToInsert
                return
            nodeQueue.add(node.left)
            nodeQueue.add(node.right)

class BinarySearchTree:
    root = None

    def insert(self, value):
        nodeToInsert = Node(value)
        if (self.root == None):
            self.root = nodeToInsert
            return
    
    def insertRecursively(self, node, nodeToInsert):
        if (nodeToInsert.value < node.value):
            #insert left
            if (node.left == None):
                node.left = nodeToInsert
            self.insertRecursively(node.left, nodeToInsert) #traverse left
        else:
            #insert right
            if (node.right == None):
                node.right = nodeToInsert
            self.insertRecursively(node.right, nodeToInsert) #traverse right

# Problem 4.1
def routeBetweenNodes(graph, nodeAName, nodeBName):
    #check if route between nodes
    nodeA = None
    nodeB = None
    for node in nodes:
        if (node.name == nodeAName):
            nodeA = node
        if (node.name == nodeBName):
            nodeB = node
    if (nodeA == None or nodeB == None):
        return False
    #check from nodeA to nodeB
    if (nodeB in nodeA.children):
        return True
    if (nodeA in nodeB.children):
        return True
    return False

if __name__ == "__main__":
    print("Test Route Between Nodes")