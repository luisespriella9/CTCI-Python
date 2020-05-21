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