class Matrix:
    def __init__(self):
        self.matrix=[]
        self.a=[[1,2],[3,4]]
        self.b=[[0,0],[0,0]]
        self.c=[[0,0],[0,0]]
    def userInput(self):
        for i in range(0,2):
            for j in range(0,2):
                print("Enter ",i,j," element: ")
                self.a[i][j]=int(input())
    
    def printMatrix(self):
        print(self.a)
    def processData(self):
        if(self.a[1][0]==0):
            print("Its already upper triangular matrix")
        if(self.a[0][1]>0):
            self.b[0][0]=self.a[1][0]*self.a[0][0]
            self.b[0][1]=self.a[1][0]*self.a[0][1]
            self.b[1][0]=self.a[0][0]*self.a[1][0]
            self.b[1][1]=self.a[0][0]*self.a[1][1]
            #print(self.b)
            self.c=self.b
            self.c[1][0]=self.c[0][0]-self.c[1][0]
            self.c[1][1]=self.c[1][1]-self.c[0][1]
            print(self.c)
        else:
            print("Error")

A=Matrix()
A.userInput()
A.printMatrix()
A.processData()
input()

