class Eigen:
    def __init__(self):
        self.matrix=[]
        self.m=[]
        self.l=None
        self.k=None
    def userMatrix(self):
        for i in range(2):
            i = i+1
            l=[]
            print("enter the %d row values:"%(i))
            for j in range(2):
                l.append(int(input()))
            self.matrix.append(l)
    def sumdiagonal(self):
        sum=0
        for i in range(2):
            for j in range(2):
                if(i==j):
                    sum=sum+ self.matrix[i][j]
        return sum

    def determinant(self):
        sum=self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]
        return sum
    def eigenvalue(self):
        a=1
        b=-1*self.sumdiagonal()
        c=self.determinant()
        x=b**2-4*a*c
        if(x<0):
            print("negative root not allow")
            return 0
            
        else:
            z=(-b+(x)**0.5)/2*a
            zz=(-b-(x)**0.5)/2*a
            self.m.append(z)
            self.m.append(zz)
            print("Eigen values is",self.m[0]," , ",self.m[1])
            return 1
    def Vector(self,l):
        l1=[]
        x=1;
        l1.append(x)
        x2=-1*l[0][0]/l[0][1]
        l1.append(x2)
        print("Final Vector:-",l1)
    def rowSame(self,l):
        a=l[1][0]
        l[1][0]=(l[0][0]/a)*l[1][0] 
        l[1][1]=((l[1][1])/(a)*(l[0][0]))#[(a-l),b][c,d]=>[(a-l),b][(a-l)*c/c,(a-l)*d/c]
        print("Same Rows:-",l)
        self.Vector(l)
    def SubMatrix(self):
        return [i for i in self.matrix]        
    def MainApi(self):
        print(self.matrix)
        self.l=self.cal()
        self.k=self.cal()
        x=self.l[0][0]-(self.m[0]);x1=self.l[1][1]-(self.m[0])
        y=self.k[0][0]-(self.m[1]);y1=self.k[1][1]-(self.m[1])
        self.l[0][0]=x
        self.l[1][1]=x1
        print("//",self.l)
        self.rowSame(self.l)
        self.k[0][0]=y;self.k[1][1]=y1
        print("//",self.k)
        self.rowSame(self.k)        
   
a=Eigen()
a.userMatrix()
value=a.eigenvalue()
if(value==1):
    a.recursse()          

