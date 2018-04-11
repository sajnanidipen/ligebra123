class Vector:
    def __init__(self):
        self.vector=[None]
    def setVector(self,v):
        self.vector=v
        
    def getVector(self,v):
         return self.vector

    def printVector(self):
        print(self.vector)

    def getElement(self,index):
        return self.vector[index]  

class  myMatrix:
    def __init__(self):
        self.alist=[]
        self.m=[[0,0,0],[0,0,0],[0,0,0]]
        self.v=[[0,0,0],[0,0,0],[0,0,0]]
        self.multvalue=[]
    def userInput(self):
        for i in range(0,3):
            for j in range(0,3):
                print("Enter ",i,j," element: ")
                self.m[i][j]=int(input())

    def printMatrix(self):
        print(self.m)

    def createVector(self):
        for j in range(0,3):
            print("Enter ",j," element: ")
            self.v[j]=int(input())
    def printVector(self):
        print(self.v)
    def vectorMultiplication(self):
        for i in range(3):
            l=[]
            for j in range(3):
                l.append(self.v[i]*self.m[i][j])
            self.multvalue.append(l)
        
        print(self.multvalue) 
        newlist=[]
        sum1=0
        sum2=0
        sum3=0
        for i in range(3):
            for j in range(3):
                if(j==0):
                    sum1+=self.multvalue[i][j]
                elif(j==1):
                    sum2+=self.multvalue[i][j]
                elif(j==2):
                    sum3+=self.multvalue[i][j]
                    #self.multvalue[i]=self.multvalue[i-1]+self.multvalue[j]
        newlist.append(sum1)
        newlist.append(sum2)
        newlist.append(sum3)
        
        print(newlist)
    def printVecMult(self):
        print(self.multvalue) 
            
A=myMatrix()
A.userInput()
print ("Matrix values: ")
A.printMatrix()
A.createVector()
print("Vector matrix values:")
A.printVector()
A.vectorMultiplication()
print("VECTOR MULTIPLICATION")
A.printVecMult()  

    
        
