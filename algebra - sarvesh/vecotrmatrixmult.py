class MyVector:
    def __init__(self):
        self.vector=None
    def setVector(self,v):
        self.vector=v
    def getVector (self):
         return self.vector
    def printVector(self):
        print (self.vector)
    def getElement(self,index):
        return self.vector[index]
class MyMatrix:
    def __init__(self,row,col):
        self.matrix=None
        self.row=row
        self.col=col
    def init_Matrix(self,matrix):
        self.matrix=matrix
    def printMatrix(self):
        print (self.matrix)
    def insertElement(self):
        self.matrix=[]
        for i in range(0,self.row):
            m=[]
            print("enter "+str(i+1)+" row elements")
            for j in range(0,self.col):
                m.append(int(input("Enter elements")))
            self.matrix.append(m)
    def vectmatrixMult(self,v):
        vector=v.getVector()
        print(vector)
        if(len(vector)!=len(self.matrix)):
            return "no. of col of vector is not equal to no. of rows of matrix"
        else:
            newVect=[]
            for i in range(len(vector)):
                vectList=[]
                for j in range(len(self.matrix[0])):
                    vectList.append(vector[i]*self.matrix[i][j])
                newVect.append(vectList)
           # print(newVect)
            data=[]
            sum1=0
            sum2=0
            for i in range(len(vector)):
                for j in range(len(self.matrix[0])):
                    if(j==0):
                        sum1+=newVect[i][j]
                    else:
                        sum2+=newVect[i][j]
            data.append(sum1)
            data.append(sum2)
        #print(data)
        return "Successfully performed multiplication"
    def matvectorMult(self,v):
        vector=v.getVector()
        if(len(vector)!=len(self.matrix[0])):
            return False
        else:
            newVect=[]
            for i in range(len(self.matrix)):
                vectList=[]
                for j in range(len(vector)):
                    vectList.append(vector[j]*self.matrix[i][j])
                newVect.append(vectList)
            print(newVect)
            data=[]
            for i in range(len(self.matrix)):
                sum1=0
                for j in range(len(self.matrix[0])):
                    sum1+=newVect[i][j]
                data.append(sum1)
            print(data)
            return True
print("set matrix row and col size")        
rows=int(input("how many rows:"))
cols=int(input("how many cols:"))
elements=int(input("how many elements in vector:"))
m=MyMatrix(rows,cols)
print("insert elements of your matrix")
m.insertElement()
print("YOUR MATRIX")
m.printMatrix()
v=MyVector()
print("insert elements of your vector")
vecData=[]
for i in range(0,elements):
    vecData.append(int(input("Enter vector elements:")))
v.setVector(vecData)
print("YOUR VECTOR")
v.printVector()
print("--------------------------------------")
print("MULTIPLICATION METHODS")
x=int(input("Enter method(vectmatmult(1)/matvectmult(2)):"))
if(x==1):
    print("VECTOR MATRIX MULTIPLICATION")
    print(m.vectmatrixMult(v))
elif(x==2):
    print("VECTOR MATRIX MULTIPLICATION")
    print(m.matvectorMult(v))
else:
    print("invalid option")
    
