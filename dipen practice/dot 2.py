x=int(input("Enter Scalar a:"))
y=int(input("Enter Scalar b:"))
a=[]
b=[]
v=[]

j=int(input("Enter No. of Elements in Vector"))
print("Enter Elements for Vector a")
for i in range(j):
    u=int(input())
    a.append(u)
    v.append(None)
print("Enter Elements for Vector b")
for i in range(j):
    u=int(input())
    b.append(u)
u=0
print(a)
print(b)

for i in range(0,(len(a))):
    u=u+(a[i]*b[i])
    a[i]=x*a[i]
    b[i]=y*b[i]
    v[i]=a[i]+b[i]
print("vector addition au+bv is:",v)
print("dot product:",u)
