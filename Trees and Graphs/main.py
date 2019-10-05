def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

def check2(result, list):
    #this is to check whether the answer is correct to the result we are expecting
    for x in list:
        if (result == x):
            print("Correct")
            return None
    print("Issue Found")

class GraphNode:
    name = ""
    children = []

    def __init__(self, name):
        self.name = name
        self.children = [];

    def addEdge(self, child):
        self.children.append(child)

class Graph:
    #implementation of directed graph
    nodes = []

    def __init__(self):
        self.nodes = []

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

    def removeNode(self, name):
        pointer = 0
        #remove node
        for i in range(len(self.nodes)):
            if (self.nodes[i].name == name):
                pointer = i
        #remove value from other nodes
        for i in range(len(self.nodes)):
            for c in range(len(self.nodes[i].children)):
                if (name == self.nodes[i].children[c].name):
                    del self.nodes[i].children[c]
                    break
        del self.nodes[pointer]

    def print(self):
        nodes = []
        for node in self.nodes:
            print("node " + str(node.name) + " : ", [x.name for x in node.children])
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
    #start from the middle value, follow up with left and right sides
    mid = int(len(sortedArray)/2)
    node = Node(sortedArray[mid])
    node.left =  minimalTreeRecursivelySolve(sortedArray[:mid])
    node.right =  minimalTreeRecursivelySolve(sortedArray[mid+1:])
    return node

# Problem 4.3
def listOfDepths(binaryTree):
    if (bst.root == None):
        return []
    #breadth first search to iterate throught tree
    root = binaryTree.root
    #we will have two queues. One for current depth nodes and the second for children of these nodes. 
    nodeQueue = Queue()
    nodeQueue.add(root) #add root of tree to queue
    allLists = []
    while (not nodeQueue.isEmpty() or not childrenQueue.isEmpty):
        depthList = LinkedList()
        childrenQueue = Queue()
        while (not nodeQueue.isEmpty()):
            removedNode = nodeQueue.remove().value
            depthList.appendToTail(removedNode.value)
            if (removedNode.left != None):
                childrenQueue.add(removedNode.left)
            if (removedNode.right != None):
                childrenQueue.add(removedNode.right)
        allLists.append(depthList)
        nodeQueue = childrenQueue
    return [list.printList() for list in allLists]

# Problem 4.4
def checkBalanced(binaryTree):
    #check if binary tree is balanced
    return checkBalancedRecursively(binaryTree.root)

# Needed for problem 4.5. recursively check balance for each node
def checkBalancedRecursively(node):
    if (node == None):
        return
    if (abs(heightRecursively(node.left)-heightRecursively(node.right))>1):
        return False
    if (checkBalancedRecursively(node.left) == False or checkBalancedRecursively(node.right) == False):
        return False
    return True

# Problem 4.5
def validateBst(binaryTree):
    #validate if Binary tree is Binary search tree
    return validateBstRecursively(binaryTree.root, None, None)

# Needed for problem 4.5. recursively solve validate BST
def validateBstRecursively(node, min, max):
    if (node == None):
        return True
    if (min != None and max != None):
        #check that number is in between min and max
        if (node.value < min or node.value > max):
            return False
    elif (min != None and max == None):
        #check that number is greater than min
        if (node.value < min):
            return False
    elif (min == None and max != None):
        #check that number is less than max
        if (node.value > max):
            return False
    return (validateBstRecursively(node.left, min, node.value) and validateBstRecursively(node.right, node.value, max))

# Problem 4.6
def successor(binarySearchTree, nodeValue):
    if (binarySearchTree.root == None):
        return None
    elif (binarySearchTree.root.value == nodeValue):
        return getMin(binarySearchTree.root.right)
    return successorRecursive(binarySearchTree.root, nodeValue, True, binarySearchTree.root)

def successorRecursive(curNode, targetNodeValue, left, parent):
    if (curNode == None):
        return None
    if (curNode.value == targetNodeValue):
        if (left == True):
            if (curNode.right == None):
                return parent.value
            return getMin(curNode.right)
        else:
            return getMin(curNode.right)
    elif (curNode.value < targetNodeValue):
        return successorRecursive(curNode.right, targetNodeValue, False, curNode)
    else:
        return successorRecursive(curNode.left, targetNodeValue, True, curNode)
    

#needed for problem 4.6
def getMin(node):
    if (node == None):
        return None
    if (node.left == None):
        return node.value
    return getMin(node.left)

# Problem 4.7
def buildOrder(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.addNode(project)
    for dependency in dependencies:
        if (len(dependency) < 2):
            return "ohh noo"
        #dependency is tuple where the second item is dependent on the first
        graph.addEdge(dependency[1], dependency[0])
    output = []
    while (len(graph.nodes)>0):
        for node in graph.nodes:
            if (len(node.children) == 0):
                output.append(node.name)
                graph.removeNode(node.name)
    return output
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
    leftHeight = heightRecursively(node.left)
    rightHeight = heightRecursively(node.right)
    return 1 + max(leftHeight, rightHeight)

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

    print("---------------------------------")
    print("Test List of depths")
    binaryTree = BinaryTree()
    binaryTree.insert("I")
    binaryTree.insert("D")
    binaryTree.insert("O")
    binaryTree.insert("L")
    binaryTree.insert("i")
    binaryTree.insert("K")
    binaryTree.insert("E")
    check([listOfDepths(bst)], [['4->None', '2->6->None', '1->3->5->7->None']])
    check([listOfDepths(binaryTree)], [['I->None', 'D->O->None', 'L->i->K->E->None']])
    check(checkBalanced(binaryTree), True)
    check(checkBalanced(bst), True)
    binarySearchTree = BinarySearchTree()
    binarySearchTree.insert(5)
    binarySearchTree.insert(6)
    binarySearchTree.insert(7)
    binarySearchTree.insert(8)
    check(checkBalanced(binarySearchTree), False)

    print("---------------------------------")
    print("Test Validate Bst")
    check(validateBst(bst), True)
    binaryTree = BinaryTree()
    binaryTree.insert(5)
    binaryTree.insert(2)
    binaryTree.insert(8)
    binaryTree.insert(1)
    binaryTree.insert(6)
    binaryTree.insert(7)
    binaryTree.insert(9)
    check(validateBst(binaryTree), False)

    print("---------------------------------")
    print("Test Successor")
    print(successor(bst, 1))
    print(successor(bst, 2))
    print(successor(bst, 3))
    print(successor(bst, 4))
    print(successor(bst, 5))
    print(successor(bst, 6))
    print(successor(bst, 7))

    print("---------------------------------")
    print("Test Build Order")
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    check2(buildOrder(projects, dependencies), [['f', 'e', 'a', 'b', 'd', 'c'], ['e', 'f', 'a', 'b', 'd', 'c'], ['f', 'e', 'b', 'a', 'd', 'c'], ['e', 'f', 'b', 'a', 'd', 'c']])