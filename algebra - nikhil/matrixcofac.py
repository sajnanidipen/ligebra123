class matrix:
    def __init__(self):
        self.alist=[ ]
    def insert(self):
        for i in range(3):
            for j in range (3):
                self.alist[i][j]=int(input("Enter  the element:"))
                print(self.alist)
    def determ(self):
        if(len(self.alist)!=3 or len(self.alist[0])!=3):
            return None
        else:
            d=self.alist[0][0]*(self.alist[1][1]*self.alist[2][2]-self.alist[1][2]*self.alist[2][1])
            print(d)
            if(d==0):
                print("The Matrix is not invertible")



m=matrix()
m.insert()
m.determ()












            
     









        








    
