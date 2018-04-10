import math as m
class MyVector:
    def __init__(self):
        self.u=[]
        self.v=[]
    def input(self):
        for i in range(0,3):
            print("Enter values for vector u:")
            a=int(input(""))
            self.u.append(a)
        for i in range(0,3):
            print("Enter values for vector v:")
            a=int(input(""))
            self.v.append(a)

    def norm(self):
        return self.v[0]**2+self.v[1]**2+self.v[2]**2

    def orthproj(self):
        c=[]
        for i in range(0,3):
            b=((self.u[0]*self.v[0]+self.u[1]*self.v[1]+self.u[2]*self.v[2])/self.norm())*self.v[i]
            c.append(b)
        return c
a=MyVector()
a.input()
a.orthproj()
