class Metrix():
    def __init__(self,m,n):
        self.a=m
        self.b=n
        self.mat1=[]
        self.mat2=[]
        
    def insert(self):
        for i in range(self.a):
            print("Enter Values:")
            z=[]
            for j in range(self.b):
                r=int(input())
                z.append(r)
            self.mat1.append(z)
        print("Insertion Success")
        
    def showrow(self):
        print("Row Values:",self.mat1)

    def showcol(self):
        for j in range(self.b):
            a=[]
            for k in range(self.a):
                a.append(self.mat1[k][j])
            print("column values:",a)

    def trans(self):
        print("Transpose:")
        for j in range(self.b):
            a=[]
            for k in range(self.a):
                a.append(self.mat1[k][j])
            print(a)

    def scalarM(self,sc1):
        print("Scalar:")
        for i in range(self.a):
            a=[]
            for j in range(self.b):
                a.append(sc1*self.mat1[i][j])
            self.mat2.append(a)
            print(self.mat2)

    def uppermatrix(self):
        self.mat1[1][0]=self.mat2[1][0]-self.mat2[0][0]
        self.mat1[1][1]=self.mat2[0][1]-self.mat2[1][1]
        print(self.mat1)
            
d=int(input("Rows:"))
e=int(input("Columns:"))


k=Metrix(d,e)      
k.insert()
k.showrow()
k.showcol()
k.trans()
f=int(input("Enter Scalar Value:"))
k.scalarM(f)
k.uppermatrix()

