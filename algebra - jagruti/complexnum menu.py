import cmath;
a = complex(input("Enter 1st Number:"))
b = complex(input("Enter 2nd Number:"))
print("Add/Sub/Mul/Div:")
while True:
    x =input("choose:")
    if x=="Add":
        print(a+b)
    elif x == "Sub":
        print(a-b)
    elif x == "Mul":
         print(a*b)
    elif x == "Div":
        print(a/b)
    elif x == "Con":
        i = input("Enter A or B:")
        if i == "A":
            print("A:",a.conjugate())
        elif i == "B":
            print("B:",b.conjugate())
        else:
            print("A:",a.conjugate())
            print("B:",b.conjugate())
    elif x == "Sqrt":
        print("A:",cmath.sqrt(a))
        print("B:",cmath.sqrt(b))
    else:
        print("Invalid Choice!")
        break
'''    
2081/7851/5593

y = print("Subtraction",a-b)
m = print("Multiplication",a*b)
n = print("Division",a/b)
p = print("Conjugate",a.conjugate(), b.conjugate())
d = print("Equality",a=b)
'''
