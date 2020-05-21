class Node():
    value = None
    left = None
    right = None
    def __init__(self, value):
        self.value = value

class BinaryTree:
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

    def getNodes(self):
        nodesList = []
        parentQueue = Queue()
        childrenQueue = Queue()
        parentQueue.add(self.root)
        while ((not parentQueue.isEmpty()) and (childrenQueue.isEmpty())):
            while (not parentQueue.isEmpty()):
                currentNode = parentQueue.remove().value
                nodesList.append(currentNode)
                if (currentNode.left != None):
                    childrenQueue.add(currentNode.left)
                if (currentNode.right != None):
                    childrenQueue.add(currentNode.right)
            parentQueue = childrenQueue
            childrenQueue = Queue()
        return nodesList