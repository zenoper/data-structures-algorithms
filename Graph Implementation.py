class Graph():
    def __init__(self) -> None:
        self.numberOfNodes = 0
        self.adjacentList = {}

    
    def addVertex(self, node):
        self.adjacentList.update({node : []})
        self.numberOfNodes += 1


    def addEdge(self, node1, node2):
        if node1 in self.adjacentList.get(node2):
            return None
        else:
            self.adjacentList.get(node2).append(node1)

        if node2 in self.adjacentList.get(node1):
            return None
        else:
            self.adjacentList.get(node1).append(node2)    

        # self.adjacentList.update({node1 : None})
        # self.adjacentList.update({node2 : None})

    def showConnection(self):
        pass


myGraph = Graph()

myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addEdge(1, 0)
myGraph.addEdge(1, 2)
myGraph.addEdge(0, 2)
myGraph.addEdge(0, 3)
myGraph.addEdge(3, 2)
myGraph.addEdge(0, 1)

print(myGraph.adjacentList)
print(myGraph.numberOfNodes)

