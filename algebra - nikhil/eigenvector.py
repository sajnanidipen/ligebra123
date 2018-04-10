class Eigen:
    def __init__(self):
        self.matrix=[]
        self.a =[]
        self.q=[]
        self.d=0
        self.dt=0
        root1=0
        root2=0
    def userInput(self):
        for i in range(row):
            l=[]
            for j in range(column):
                print("Enter ",i,j," element: ")
                l.append(int(input()))
            self.a.append(l)
        print(self.a)
    
    def IdentityMatrix(self,row,column):
        for i in range(row):
            l=[]
            for j in range(column):
                if i==j:
                    l.append(1)
                else:
                    l.append(0)
            self.q.append(l)
        print(self.q)

    def sumOfDiagonalE(self,row,column):
        for i in range(row):
            for j in range(column):
                if i==j:
                    self.d=self.d+(self.a[i][j])
        self.d=self.d*(-1)
        print(self.d)
        return self.d

    def Determinate(self):
        self.dt=self.a[0][0]*self.a[1][1]-self.a[1][0]*self.a[0][1]
        print(self.dt)
        return self.dt

    def eigenValue(self,row,column):
        r1=row
        c1=column
        b=self.sumOfDiagonalE(r1,c1)
        c=self.Determinate()
        root1=((-1*(b)+(b*b-4*1*(c))**0.5)/2)
        root2=((-1*(b)-(b*b-4*1*(c))**0.5)/2)
        print("lambda  value 1: " ,root1)
        print("lambda value 2: "  ,root2)


row=int(input("enter the no. of rows:"))
column=int(input("enter the no.of columns:"))
e=Eigen()
e.userInput()
print("------------Identity matrix--------------")
e.IdentityMatrix(row,column)                             
print("------------Sum of diagonal --------------")
e.sumOfDiagonalE(row,column)
print("------------Determinate --------------")
e.Determinate()
e.eigenValue(row,column)
