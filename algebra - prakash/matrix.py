class Matrix:
    def __init__(self,m,n):
        self.a=m
        self.b=n
        self.matrix=[]
        self.matrix2=[]
        self.matrix3=[]
    def display(self):
        for i in range(self.a):
            print("Enter the values for matrix")
            z=[]
            for j in range(self.b):
                r=int(input())
                z.append(r)
            self.matrix.append(z)
        print("row values are",self.matrix)
    def  showcolumn(self):
         for j in range(self.b):
             a=[]
             for k in range(self.a):
                 a.append(self.matrix[k][j])
             print("column values are:",a)
    def transpose(self):
        print("transpose of matrix:")
        for j in range(self.b):
            a=[]
            for k in range(self.a):
                a.append(self.matrix[k][j])
            print(a)
            '''self.matrix2.append(a)
        print(self.matrix2,"\n")'''
    def scalarmult(self,scalar):
        print("multiplication of scalar:")
        for i in range(self.a):
            z=[]
            for j in range(self.b):
                z.append(scalar*self.matrix[i][j])
            self.matrix3.append(z)
            print(self.matrix3)
        
        
d=int(input("enter the no.of rows:"))
e=int(input("enter the no.of columns:"))
a=Matrix(d,e)
a.display()
a.showcolumn()
a.transpose()
a.scalarmult(3)
