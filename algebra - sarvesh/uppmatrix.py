class Matrix:
    def __init__(self):
        self.matrixs=[]
        self.matrix2=[[None,None],[None,None]]
        self.matrix=[]
    
    def insert(self):
         print("Enter the values for matrix")
         for i in range(2):
             l=[]
             for j in range(2):
                 l.append(int(input()))
             self.matrixs.append(l)
         for j in range(2):
            for i in range(2):
                print(i,"+",j)
                if(j==0):
                    self.matrix2[j][i]=self.matrixs[j][i]*self.matrixs[1][0]
                elif(j==1):
                    self.matrix2[j][i]=self.matrixs[j][i]*self.matrixs[0][0]
    def uppermatrix(self):
        self.matrixs[1][0]=self.matrix2[1][0]-self.matrix2[0][0]
        self.matrixs[1][1]=self.matrix2[0][1]-self.matrix2[1][1]
        print(self.matrixs)
    def transpose(self):
        for j in range(2):
            a=[]
            for k in range(2):
                a.append(self.matrixs[k][j])
            self.matrix.append(a)
        print("transpose of matrix:",self.matrix)
        

m=Matrix()
m.insert()
m.uppermatrix()
m.transpose()
