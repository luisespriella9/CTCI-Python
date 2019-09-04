def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

class GraphNode:
    name = ""
    children = None

    def __init__(self, name):
        self.name = name
        self.children = [];

    def addEdge(self, child):
        self.children.append(child)

class Graph:
    #implementation of directed graph
    nodes = []

    def addNode(self, name):
        graphNode = GraphNode(name)
        self.nodes.append(graphNode)

    def addEdge(self, pointingNodeName, pointerNodeName):
        #find two nodes if they exists, if not then do nothing
        pointerNode = None
        pointingNode = None
        for node in self.nodes:
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
    for node in graph.nodes:
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

# Problem 4.2
def minimalTree(sortedArray):
    #start from middle of array to create a balanced BST
    bst = BinarySearchTree()
    bst.root = minimalTreeRecursivelySolve(sortedArray)
    return bst
    
#recursive method to solve problem 4.2
def minimalTreeRecursivelySolve(sortedArray):
    if (len(sortedArray) == 0):
        return None
    mid = int(len(sortedArray)/2)
    node = Node(sortedArray[mid])
    node.left =  minimalTreeRecursivelySolve(sortedArray[:mid])
    node.right =  minimalTreeRecursivelySolve(sortedArray[mid+1:])
    return node

#test useful functions

#traverse tree in order, return values in order
def inOrder(bst):
    return inOrderRecursively(bst.root, "").strip()

def inOrderRecursively(node, result):
    if (node == None):
        return ""
    #left
    if (node.left != None):
        result = inOrderRecursively(node.left, result)
    #root
    result += " " + str(node.value)
    #right
    if (node.right != None):
        result = inOrderRecursively(node.right, result)
    return result

def height(bst):
    return heightRecursively(bst.root)

def heightRecursively(node):
    if (node == None):
        return 0
    return 1 + max(heightRecursively(node.left), heightRecursively(node.left))

if __name__ == "__main__":
    print("Test Route Between Nodes")
    #lets build a graph
    graph = Graph()
    graph.addNode("A")
    graph.addNode("B")
    graph.addNode("C")
    graph.addNode("D")
    graph.addNode("E")
    graph.addEdge("E", "A")
    graph.addEdge("A", "B")
    graph.addEdge("B", "C")
    graph.addEdge("B", "D")
    graph.addEdge("C", "D")
    check(routeBetweenNodes(graph, "E", "A"), True)
    check(routeBetweenNodes(graph, "E", "B"), False)
    check(routeBetweenNodes(graph, "B", "D"), True)
    check(routeBetweenNodes(graph, "D", "C"), True)
    check(routeBetweenNodes(graph, "C", "A"), False)
    check(routeBetweenNodes(graph, "D", "E"), False)
    check(routeBetweenNodes(graph, "B", "A"), True)

    print("---------------------------------")
    print("Test Minimal Tree by checking height and inorder result")
    sortedArray = [i for i in range(1, 8)]
    bst = minimalTree(sortedArray)
    check(height(bst), 3)
    check(inOrder(bst), "1 2 3 4 5 6 7")