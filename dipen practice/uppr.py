class Metrix():
    def __init__(self):
        self.mat1=[[1,2],[3,4]]

    def uppr(self):
        r1=self.mat1[0][0]
        r2=self.mat1[0][1]
        r3=self.mat1[1][0]
        r4=self.mat1[1][1]
        self.mat1[1][0]=self.mat1[1][0]-3*r1
        self.mat1[1][1]=self.mat1[1][1]-3*r2
        print(self.mat1)

k=Metrix()
k.uppr()
