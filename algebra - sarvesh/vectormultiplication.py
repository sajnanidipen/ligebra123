class Myvector:
    def __init__(self):
        self.vector=None;
    def setvector(self,v):
        self.vector=v
    def getvector(self):
        return self.vector
    def printvector(self):
        print(self.vector)
    def getelement(self,i):
         return self.vector[i];

class vectormat:
    def __init__(self):
        self.matrix=[]
        self.vec=[]
        self.vec2=[]
    def setmatrix(self,m,n):
        for i in range (m):
            l=[]
            print("Started %d row"%i)
            for j in range (n):
                l.append(int(input("enter the values")))
            self.matrix.append(l)
            print(self.matrix)
    def vectorimp(self,l):
        global pp
        pp=l
        for i in range (0,(len(l))):
           r=[]
           for j in range ((len(self.matrix)+1)):
               r.append(l[i]*self.matrix[i][j])
           self.vec.append(r)
        print("vec ",self.vec)
    def Add(self,m,n):
          for i in range (n):
              r=[]
              for j in range (m):
                  r.append(self.vec[j][i])
              self.vec2.append(r)
          print("vec2",self.vec2)
          l=[]
          for i in range(n):
              sum=0
              for j in range (m):
                  sum=sum+self.vec[j][i]
              l.append(sum)
          print(l)

d=Myvector()
v=[]
a=int(input("No of element in vector:"))
for i in range(a):
    v.append(int(input()))
d. setvector(v)
l=d.getvector()
r=vectormat()
m=int(input("No of rows:"))
n=int(input("No of columns:"))
r.setmatrix(m,n)
r.vectorimp(l)
r.Add(m,n)            
        
                
        
        
  
    
