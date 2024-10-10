from Mymodul import *
b=int(input("Sisesta arv2: "))
summa_3=Summa(3,b,int(input("kolmas arv: ")))
summa_31=Summa(100,100)
print(summa_3)
print(summa_31)
2
from Mymodul import *
try:
    aasta=float(input("Sisestage Aasta: "))
    print(liigaasta(aasta))
except ValueError:
    pass

3
from Mymodul import *
try:
    ruudukülg = int(input("Palun sisestage ruudu küljed: "))
    if ruudukülg != ruudukülg:
        print("Palun sisestage 3 küljet.")
    else:
        perimeeter, pindala, diagonaal = square(ruudukülg)
        print(perimeeter, pindala, round(diagonaal, 2))
except ValueError:
    print("Palun sisestage kehtiv külje pikkus numbrina.")


4
from Mymodul import *
while True:
    try:
        kuu=int(input("kuu number: "))
        break
    except:
        print("viga")
a=season(kuu)
print(a)


6

from Mymodul import *
arv=int(input("Sisestage arvu: "))
print(is_prime(arv))


7

from Mymodul import *
paev=int(input("kirjutage paeva: "))
kuu=int(input("kirjutage kuut: "))
aasta=int(input("kirjutage aasta: "))

print(date(paev, kuu, aasta))

from Mymodul import *
a=float(input("sisestage a raha: "))
aasta=int(input("Sisestage kui palju aastaks: "))

print("teie tagastatud summa on: ",pank(a,aasta))
