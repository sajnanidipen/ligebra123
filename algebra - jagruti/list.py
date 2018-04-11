class X:
    def __init__(self,n):
        self.x=n
    def display(self):
        print(self.x)
    def getSq(self):
        y=self.x * self.x
        obj=X(4)
        return obj
ob1=X(2)
ob1.display()
ob2=ob1.getSq()
ob2.display()
