import math
import cmath
a=complex(input("Enter 1st Value:"))
b=complex(input("Enter 2nd Value:"))


while(True):
    c=input("Enter the choice: add/sub/mult/div/conju/equal/sqrt\n")
    if(c=="add"):
        print("Add:",a+b)
    elif(c=="sub"):
        print("Sub:",a-b)
    elif(c=="mult"):
        print("Mult:",a*b)
    elif(c=="div"):
        print("Div:",a/b)
    elif(c=="conju"):
        print(complex.conjugate(b))
    elif(c=="equal"):
        if(a.real==b.real and a.imag==b.imag):
            print("Equal")
        else:
            print("Not Equal")
    elif(c=="sqrt"):
        print(cmath.sqrt(a))
    else:
        print("Invalid Choice")
