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

class vectorimp:
    def __init__(self):
        self.matrix=[]
    
    def setmatrix(self):
        for i in range (2):
            l=[]
            for j in range (2):
                l.append(int(input("enter the values")))
            self.matrix.append(l)
    def vectormult(self):
        for i in range (len(self.vector)):
            for j in range (len(self.vector)):
