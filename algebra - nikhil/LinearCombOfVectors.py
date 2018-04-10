class MyVector:
    def __init__(self):
        self.v=[]
        self.w=[]
        
    def EnterVector(self):
        for i in range(3):
            l1=[]
            print("Enter values for vector ",i)
            for j in range(3):
              r=int(input("Enter elements"))
              l1.append(r)
            self.v.append(l1)
        for i in range(3):
            a=int(input("Enter values for constant"))
            self.w.append(a)

    def Display(self):
        print(self.v," [k1 , k2 , k3] = ",self.w)
    
        
    def LinearComb(self):
        for i in range(0,3):
            self.v[0][i]=self.v[0][i]/self.v[0][0]
        self.w[0]=self.w[0]/self.v[0][0]
        for j in range(0,3):
            self.v[1][j]=self.v[1][j]-self.v[1][0]*self.v[0][j]
        self.w[1]=self.w[1]-self.w[1]*self.w[0]
        for j in range(0,3):
            self.v[2][j]=self.v[2][j]-self.v[2][0]*self.v[0][j]
            print(self.v[2][j])
        self.w[2]=self.w[2]-self.w[2]*self.w[0]
        for i in range(0,3):
            self.v[1][i]=self.v[1][i]/self.v[1][1]
        self.w[1]=self.w[1]/self.v[1][1]
        for i in range(0,3):
            self.v[2][i]=self.v[2][i]/self.v[2][2]
        self.w[2]=self.w[2]/self.v[2][2]
        
        
        
v=MyVector()
v.EnterVector()
v.Display()
v.LinearComb()
v.Display()
