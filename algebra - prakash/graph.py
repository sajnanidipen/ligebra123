from tkinter import *
import cmath
master = Tk()
c=complex(input("enter the complex no:"))
w = Canvas(master, width=400, height=400,bg="yellow")
w.pack()
w.create_line(200, 0, 200, 400,fill="red")
w.create_line(0, 200, 400, 200, fill="red")
d=20
x=c.real
y=c.imag
r=200+x*d
r1=200-y*d
w.create_oval(r,r1,r+5, r1+5, outline="gray",fill="gray", width=2)
w.create_line(200,200,r+5, r1+5,fill="black")
#reflection
c1=c*(-1)
x1=c1.real
y1=c1.imag
r11=200+x1*d
r12=200-y1*d
w.create_oval(r11,r12,r11+5, r12+5, outline="black",fill="white", width=2)
w.create_line(200,200,r11+5, r12+5,fill="black")
#scaling
a=float(input("enter the scaling value:"))
c2=c*(a)
x2=c2.real
y2=c2.imag
r13=200+x2*d
r14=200-y2*d
w.create_oval(r13,r14,r13+5, r14+5, outline="blue",fill="blue", width=2)
w.create_line(200,200,r13+5, r14+5,fill="black")
#rotation
b=int(input("enter the degree of rotation:"))
j=(-1)**0.5
if(b==90):
    c3=c*(j)
elif(b==180):
    c3=c*(j*j)
elif(b==270):
    c3=c*(j*j*j)
elif(b==360):
    c3=c*(j*j*j*j)
else:
    print("invalid")
x3=c3.real
y3=c3.imag
r15=200+x3*d
r16=200-y3*d
w.create_oval(r15,r16,r15+5, r16+5, outline="black",fill="black", width=3)
w.create_line(200,200,r15+5, r16+5,fill="black")
mainloop()
