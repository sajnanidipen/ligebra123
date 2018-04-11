class Node:
    def __init__(self,node):
        self.node=node
        self.status=None
    def setStatus(self,status):
        self.status=status
    def getStatus(self):
        return self.status
    def getNode(self):
        return self.node
class Graph:
    def __init__(self,size):
        self.size=size
        self.listOfVerticesObj=[]
        self.listOfVertices=[]
        self.adjMat=[[0 for i in range(size)] for i in range(size)]
    def initGraphElements(self):
        for i in  range(self.size):
            n=int(input("Enter Elements:"))
            self.listOfVerticesObj.append(Node(n))
            self.listOfVertices.append(n)
    def connEdges(self,v1,v2):
        if(v1 and v2 in self.listOfVertices):
            self.adjMat[self.listOfVertices.index(v1)][self.listOfVertices.index(v2)]=1
            return True
        return False
    def printAdj(self):
        for i in self.adjMat:
            x=''
            for j in i:
                x+=str(j)+" "
            print(x)
            
graph=Graph(int(input("How many vertices:")))
graph.initGraphElements()
x=int(input("How many edges:"))
for i in range(x):
    if(graph.connEdges(int(input("Enter v1:")),int(input("Enter v2:")))):
        print("Successfully connected")
    else:
        print("vertices doesn't exists")
        
graph.printAdj()          
