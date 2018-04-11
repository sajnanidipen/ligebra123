class MyMatrix:
    def __init__(self):
        self.a=[[1,2,3],
                [4,5,6]]
        self.b=[[],[],[]]
    def display(self):
        for i in range(0,2):
            for j in range(0,3):
                print(self.a[i][j])
    def displayrow(self,n):
        for i in range(0,3):
            i=n-1
            print(self.a[i][j])
    def displaycol(self,n):
        for i in range(0,2):
            j=n-1
            print(self.a[i][j])
    def transpose(self):
        for i in range(0,3):
            for j in range(0,2):
                print(self.a[j][i])
                
    def scalarmultp(self,n):
        for i in range(0,2):
            for j in range(0,3):
                print(n*self.a[i][j])
        
q=MyMatrix()
q.display()
q.displayrow(2)
q.displaycol(3)
q.transpose()

        
            
        
