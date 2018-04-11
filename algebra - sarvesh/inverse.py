#write a program to enter a matrix and check wheather it is invertible

class matrix:
	def __init__(self,data):
		self.matrix=data
		self.d=None
		self.tra=[]
		self.inv=[[None,None,None],[None,None,None],[None,None,None]]
		self.co=[[None,None,None],[None,None,None],[None,None,None]]
	
	
	def Inverse(self):
		for i in range(3):
			for j in range(3):
				self.inv[i][j]=(self.tra[i][j])*(self.d)
		print(self.inv)		
	def cofactor(self):
		self.co[0][0]=self.matrix[1][1]*self.matrix[2][2]-self.matrix[1][2]*self.matrix[2][1]
		self.co[0][1]=(-1)*self.matrix[1][0]*self.matrix[2][2]-self.matrix[1][2]*self.matrix[2][0]	
		self.co[0][2]=self.matrix[1][0]*self.matrix[2][1]-self.matrix[1][1]*self.matrix[2][0]	

		self.co[1][0]=(-1)*self.matrix[0][1]*self.matrix[2][2]-self.matrix[0][2]*self.matrix[2][1]
		self.co[1][1]=self.matrix[0][0]*self.matrix[2][2]-self.matrix[0][2]*self.matrix[2][0]	
		self.co[1][2]=(-1)*self.matrix[0][0]*self.matrix[2][1]-self.matrix[0][1]*self.matrix[2][0]	

		self.co[2][0]=self.matrix[0][1]*self.matrix[1][2]-self.matrix[0][2]*self.matrix[1][1]
		self.co[2][1]=(-1)*self.matrix[0][0]*self.matrix[1][2]-self.matrix[0][2]*self.matrix[1][0]	
		self.co[2][2]=self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]	
		print(self.co)
		for i in range(3):
			l=[]
			for j in range(3):
				l.append(self.co[j][i])
			self.tra.append(l)
			
							

	def setData(self):
		print("Enter Matrix element:")
		for i in range(3):
			list1=list()
			for j in range(3):
				list1.append(int(input()))
			print(list1)
			self.matrix.append(list1)

	def deter(self):
		print(self.d)
		for i in range(len(self.matrix)):
			if(len(self.matrix)!=3 ):
				return None
	
		self.d=self.matrix[0][0]*(self.matrix[1][1]*self.matrix[2][2]-self.matrix[1][2]*self.matrix[2][1])-self.matrix[0][1]*	(self.matrix[1][0]*self.matrix[2][2]-self.matrix[1][2]*self.matrix[2][0])+self.matrix[0][2]*(self.matrix[1][0]*self.matrix[2][1]-self.matrix[1][1]*self.matrix[2][0])
		print(self.d)

		
Matrix=[]	
m=matrix(Matrix)
m.setData()	
m.deter()
m.cofactor()
m.Inverse()

