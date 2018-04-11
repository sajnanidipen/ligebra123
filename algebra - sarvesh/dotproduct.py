x=int(input("enter the scalar a:"))
y=int(input("enter the scalar b:"))
a=[]
b=[]
v=[]
j=int(input("enter the no.of elements in the vector:"))
print("enter the vector a:")
for i in range(j):
    u=int(input());
    a.append(u)
    v.append(None)
print("enter the vector b:")
for i in range(j):
    u=int(input());
    b.append(u)
u=0;
print(a)
print(b)
for i in range(0,(len(a))):
    u=u+(a[i]*b[i])
    a[i]=x*a[i];
    b[i]=y*b[i];
    v[i]=a[i]+b[i]
print("the vector addition au+bv is",v)
print("the dot product of u & v is",u)
