
class mymatrix:
    def __init__(self):
        self.a=int(input("enter no of row:"))
        self.n=int(input("enter no of columns:"))
        self.m=[]
        self.l=int(input("Enter vector length"))
        self.v=[]
    def acceptmatrix(self):
        for i in range(self.a):
            t=[]
            print("enter elements for each row")
            for j in range(self.n):
                b=int(input())
                t.append(b)
            self.m.append(t)
        print(self.m)

    def acceptVector(self):
        'n=int(input("enter vector length:"))'
        print("enter elements for Vector")
        for i in range(self.l):
            j=int(input("i:element\t"))
            self.v.append(j)
        print(self.v)



    def matrixvector(self):
        v1= self.v
        m1= self.m
        v2=[]
        
        if(self.l== self.n):
            for i in range(self.a):
                v=[]
                for j in range(self.n):
                  if(i==0):
                    v.append(v1[j]*m1[i][j])
                  elif(i==1):  
                    v.append(v1[j]*m1[i][j])
                  elif(i==2):
                    v.append(v1[j]*m1[i][j])
                v2.append(v)
            print(v2)
            s=0;s1=0;s2=0;newV=[]
            for i in range(self.a):
                for j in range(self.n):
                    if (i==0):
                        s+=v2[i][j]
                    elif(i==1):
                        s1+=v2[i][j]
                    elif(i==2):
                        s2+=v2[i][j]
                    else:
                        none
                   
            newV.append(s) 
            newV.append(s1)
            newV.append(s2)
        else:
          print("matrix vector does not exist")
        print(newV)
                    
        
               
            
                        
m=mymatrix()
print(" accepting matrix")
m.acceptmatrix()
print("accepting vector")
m.acceptVector()
print("Matrix Vector")
m.matrixvector()






