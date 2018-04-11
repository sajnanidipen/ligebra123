v=[]
x1=[]
j=int(input("enter the no.of elements in the vector:"))
j1=int(input("enter the no.of vectors:"))
for k in range(j1):
    x=int(input("enter the scalar :"))
    a=[]
    for i in range(j):
        u=int(input())
        a.append(u*x)
    v.append(a)
print("the vector addition au+bv is",v)

for i in range(j1):
    u=0
    for j2 in range(j):
        u=u+v[j2][i]
    print(u)
    x1.append(u)
print(x1)
