class ortho:
    def __init__ (self):
        self.a=1
        self.u=[]
        self.v=[]
        self.r=[]
    def createVector_u(self):
        for i in range(a):
            self.u.append(int(input("Enter  the vector:")))
            print(self.u)
    def createVector_v(self):
        for i in range(a):
            self.v.append(int(input("Enter  the vector:")))
            print(self.v)
    def norm(self):
        sum2=0
        for i in range(a):
            sum2=sum2+(self.v[i]**2)
        print(sum2)
        self.projection(sum2)

    def projection(self,sum2):
        sum1=0
        for i in range(a):
            sum1=(self.u[i]*self.v[i])
        result=(sum1/sum2)
        for i in range(a):
            self.r.append(self.v[i]*result)
    def print(self):
        print(self.r)
o=ortho()
a=int(input("enter the length :"))
print("u  vector")
o.createVector_u()
print("v  vector")
o.createVector_v()
print("norm")
o.norm()
print("projection")
o.print()
