class MyMatrix:
     def __init__(self,mat):
          self.X=[[0,0,0],[0,0,0],[0,0,0]]
          self.mat=mat

     def det(self):
          if len(self.mat)!=3 or len(self.mat[0])!=3:
               return None
          else:
               self.de=(self.mat[0][0]*(self.mat[1][1]*self.mat[2][2]-self.mat[1][2]*self.mat[2][1])) - (self.mat[0][1]*(self.mat[1][0]*self.mat[2][2]-self.mat[1][2]*self.mat[2][0])) + (self.mat[0][2]*(self.mat[1][0]*self.mat[2][1]-self.mat[1][1]*self.mat[2][0]))
               return self.de
     def invert(self):
          if self.de==0:
               print("No Inverse Exist")
               return None
     def cofac(self):
          self.X=[]
          self.a=((self.mat[1][1]*self.mat[2][2]-self.mat[1][2]*self.mat[2][1])) 
          self.b=-((self.mat[1][0]*self.mat[2][2]-self.mat[1][2]*self.mat[2][0]))
          self.c=((self.mat[1][0]*self.mat[2][1]-self.mat[1][1]*self.mat[2][0]))
          self.d=-((self.mat[0][1]*self.mat[2][2]-self.mat[0][2]*self.mat[2][1]))
          self.e=((self.mat[0][0]*self.mat[2][2]-self.mat[0][2]*self.mat[2][0]))
          self.f=-((self.mat[0][0]*self.mat[2][1]-self.mat[0][1]*self.mat[2][0]))
          self.g=((self.mat[0][1]*self.mat[1][2]-self.mat[0][2]*self.mat[1][1]))
          self.h=-((self.mat[0][0]*self.mat[1][2]-self.mat[0][2]*self.mat[1][0]))
          self.i=((self.mat[0][0]*self.mat[1][1]-self.mat[0][1]*self.mat[1][0]))
          self.X.append([self.a,self.b,self.c])
          self.X.append([self.d,self.e,self.f])
          self.X.append([self.g,self.h,self.i])
          print (self.X)
     def transpose(self):
          self.Y=self.X
          for i in range(0,3):
            for j in range(0,3):
                self.Y[i][j]=(self.X[j][i])
          print(self.Y)
    
mat = []

for j in range(0,3):
     a=int(input("Enter 1 "))
     b=int(input("Enter 2 "))
     c=int(input("Enter 3 "))
     mat.append([a,b,c])
print(mat)
A=MyMatrix(mat)
print(A.det())
print(A.invert())
#A.swap(mat)
A.cofac()
A.transpose()
#A.adj()
