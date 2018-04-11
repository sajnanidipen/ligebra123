class MyMatrix:
    def __init__(self,m,n):
        self.a=m
        self.b=n
        self.mat1=[]
        self.mat2=[]
    def display(self):
        for i in range(self.a):
            print("Enter the values for matrix")
            z=[]
            for j in range(self.b):
                r=int(input())
                z.append(r)
            self.mat1.append(z)
        print("row values are:",self.mat1)

    def showcolumn(self):
        for j in range(self.b):
            a=[]
            for k in range(self.a):
                a.append(self.mat1[k][j])
            print("Column values:",a)

    def transpose(self):
        print("transpose:")
        for j in range(self.b):
            a=[]
            for k in range(self.a):
                a.append(self.mat1[k][j])
            print(a)
    def scalarM(self,sc1):
        print("scalar:")
        for i in range(self.a):
            z=[]
            for j in range(self.b):
                z.append(sc1*self.mat1[i][j])
            self.mat2.append(z)
            print(self.mat2)
    
            

    
d=int(input("Enter No. of Rows:"))
e=int(input("Enter No. of Columns:"))


k=MyMatrix(d,e)
k.display()
k.showcolumn()
k.transpose()
f=int(input("Enter Value of Scalar:"))
k.scalarM(f)
