class  linearCombination:
    def __init__(self):
        #Linear Combination form
        #kv1+kv2+kv3=w
        self.Vectors=[[3,2,-2],[1,-2,3],[2,3,4]]
        self.w=[[11],[-9],[0]]
    def SameRow(self,i,x,value):#This Function for Dividing the diagonal row with diagonal value
        for j in range(len(self.Vectors)):
            if(x!=j):
                self.Vectors[i][j]=self.Vectors[i][j]/value
    def TempList(self,i):#Getting  the Temp List With The Value of row of that diagonal 
        l=[None for i in range(len(self.Vectors))]
        for j in range(len(self.Vectors)):
            l[j]=self.Vectors[i][j]
        return l
    def DiffRow(self,i,j):#This function for make non diagonal rows value zero
            Temp=self.TempList(i)
            for i1 in range(len(self.Vectors)):
                w=self.w[i][0]
                for j1 in range(len(self.Vectors)):
                    if(j==j1 and i!=i1):
                        Single=1
                        r=self.Vectors[i1][j1]#get the value other then that diagonal rows where j of diagonal row equal to that of other non digonal
                        l=[x*r for x in Temp]#multipling  all values of Temp list with r 
                        l1=Temp[j1]
                        if(Single==1):
                            #Excut only one Time
                            w1=self.w[i1][0]
                            w=w*r
                            w1=w1*l1
                            self.w[i1][0]=w1-w
                        Single=Single+1
                        for x2 in range(len(self.Vectors)):
                            self.Vectors[i1][x2]=l1*self.Vectors[i1][x2]-l[x2]
    def Identity(self):#This Function For Dividing Only Digonal Values
        #Only for Digonal division
        for i in range(len(self.Vectors)):
                       Value=self.Vectors[i][i]
                       self.Vectors[i][i]=self.Vectors[i][i]/Value
                       self.w[i][0]=self.w[i][0]/Value
                       self.SameRow(i,i,Value)
                       self.DiffRow(i,i)                                    
        print("Final Vector",self.Vectors)
        print("w value:",self.w)               
l=linearCombination()
l.Identity()
         


                        
