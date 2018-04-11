x=int(input("Enter Scalar a:"))
y=int(input("Enter Scalar b:"))
a=[]
b=[]
v=[]
      
j=int(input("Enter No. of elements in vector:"))
print("Enter the vector a:")
for i in range(j):
    u=int(input())
    a.append(u)
    v.append(None)
print("Enter the vector b:")
for i in range(j):
    u=int(input())
    b.append(u)
u=0
print(a)
print(b)

for i in range(0,(len(a))):
      u=u+(a[i]*b[i])
      a[i]=x*a[i]
      b[i]=y*a[i]
      v[i]=a[i]+b[i]
print("vector addition au+bv =",v)
print("dot product of u & v is",v)
