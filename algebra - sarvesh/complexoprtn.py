import cmath
a=complex(input("Enter the no."))
b=complex(input("Enter the no."))

c=input("Enter the choice:add/sub/mul/div/conju/equal/squrt.")
if(c=="add"):
   print("add",a+b)
elif(c=="sub"):
   print("sub",a-b)
elif(c=="mul"):
   print("mul",a*b)
elif(c=="div"):
   print("div",a/b)
elif(c=="conju"):
   print(complex.conjugate(b))
elif(c=="equal"):
   if(a.real==b.real and a.imag==b.imag):
      print("equal")
   else:
      print("Not equal")
elif(c=="squrt"):
   print(cmath.sqrt(a))
