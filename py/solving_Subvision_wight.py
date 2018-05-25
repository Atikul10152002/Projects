
from __future__ import print_function
a = int(input("a-weight "))
b = int(input("b-weight "))
c = int(input("c-weight "))

average = a+b+c

Ax = input("Ax ")
Ay = input("Ay ")
Acord = (Ax,Ay)

Bx = input("Bx ")
By = input("By ")
Bcord = (Bx, By)

Cx = input("Cx ")
Cy = input("Cy ")
Ccord = (Cx, Cy)

print("#"*20)
print((a*int(Acord[0]))+(b*int(Bcord[0]))+(c*int(Ccord[0])),"/", average)
print((a*int(Acord[1]))+(b*int(Bcord[1]))+(c*int(Ccord[1])),"/", average)
