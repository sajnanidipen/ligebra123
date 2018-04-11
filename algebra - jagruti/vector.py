a=[1,2,4,5]
b=[3,5,6,8]
u=[None,None,None,None]
v=[None,None,None,None]
for i in range(0,len(a)):
    u[i]=a[i]+b[i]
    v[i]=a[i]*b[i]
print(u)
print(v)

t=[None,None,None,None]
for i in range(0,3):
    t[i]=((u[i]*a[i])+(v[i]*b[i]))
print("t=" ,t)
uv=[None,None,None,None]
for i in range(0,len(a)):
    uv[i]=u[i]*v[i]
print("uv=",uv)
