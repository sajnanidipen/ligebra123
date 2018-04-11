class Projection:
    def __init__(self,ele):
        self.e=ele
        self.matix=[[0 for k in range(ele)]for j in range(2)]
    def initial(self):
        for i in range(2):
            print("enter %d vector"%(i))
            for j in range(self.e):
                self.matix[i][j]=input(int())
    def Multi(self):
        sum=0
        for i in range(self.e):
            sum=sum+self.matix[0][i]*self.matix[1][i]
        return sum
    def nome(self,k):
        sum=0
        for i in range(self.e):
            sum=sum+self.matix[k][i]**2
        return sum
    def display(self,div,k):
        l=[]
        for i in range(self.e):
            l.append(div*self.matix[k][i])
        return l
    def ortho(self):
        stt=int(input("Enter option (v on u)1//(u  on v)2:"))
        mul=self.Multi()
        nome=self.nome(stt-1)
        print("multi",mul)
        print("norm",nome)
        div=float(mul)/float(nome)
        print("div",div)
        print("final",self.display(div,(stt-1)))
        
ele= int(input("Enter No of element"))       
pro=Projection(ele)
pro. initial()
pro.ortho()
