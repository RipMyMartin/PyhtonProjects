﻿from math import * # не правильный порядок
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #float
S=a**2
print("Ruudu pindala",round(S, 2)) #round + ковычка
P=4*a
print("Ruudu ümbermõõt", round(P,2 )) # round + ковычка
di=a*sqrt(2) # удалить  math
print("Ruudu diagonaal", round(di,2)) #round + ковычка
print()
print("Ristküliku karakteristikud") #лишния скопка
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # float + ковычки
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # float + ковычки
S=b*c
print("Ristküliku pindala", S) #
P=2*(b+c) #*
print("Ristküliku ümbermõõt", P)
di=sqrt(b*2+c*2) #удалить math.
print("Ristküliku diagonaal", round(di, 2)) #не закрыта скопка
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus =>')) #float + ковычки
d=2*r # * + удалить скопки после пи
print("Ringi läbimõõt"+ str(d)) #str
S=pi*r**2 #* + удалить скопки после пи
print("Ringi pindala", round(S ,2))
C=2*pi*r #*  
print("Ringjoone pikkus", round(C,2)) #не закрыта скопка
