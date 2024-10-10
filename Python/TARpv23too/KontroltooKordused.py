﻿from random import *
from webbrowser import MacOSX
while True:
    try:
        K=int(input("Mitu kotleti sul on?  "))
        if K>0:
            break
    except ValueError:
        print("vale tüüp")
pann=0
while True:
    try:
        M=int(input("Mitu kotleti ühel pannil?  "))
        if M>0:
            break
    except ValueError:
        print("vale tüüp")
while K>0:
    k-=M 
    pann+=1 
    print(f"Praetud: {pann}")
    if K>M:
        K-=M 
        pann+=1
        print(f"praetud: {pann} tk")
print(f"Täispannid: {pann}")
print()


N=25
kesk1=0
kesk2=0
for i in range(N):
    h1=randint(1,5)
    h2=randint(1,5)
    kesk1+=h1
    kesk2+=h2
kesk1/=N
kesk2/=N 
print(f"kekmine hinne 1 klassis on{kesk1}")
print(f"kekmine hinne 2 klassis on{kesk2}")



while True:
    try:
        mitu=int(input("mitu tk:"))
        if 1<=mitu<10:
            break
    except ValueError:
        print("vale tüüp")

for i in range(mitu):
    print(' /V\ '.center(10,' '),end=" ")



from math import fabs
from random import *
sum_num =0
sum_km =0
for i in range(12):
    num=randint(1000,10000)
    km=randint(1,1000)
    sum_num+=num
    sum_km+=km
    print(f"{i+1}.maakond.\nElanikud: {num}.pindala: {km}\n kokku:{sum_num},{sum_km}")
vastus=sum_num/sum_km
print(f"Keskmine: {vastus:.3f}")

#3 variant

#1


try:
    n = int(input("Sisesta number vahemikus 1 kuni 9: "))  # Küsime kasutajalt sisendit arvu n jaoks
    if n < 1 or n > 9:
        print("Vale sisend. Palun sisestage number vahemikus 1 kuni 9.")  # Kui sisestatud number ei ole vahemikus 1 kuni 9, prindime veateate
    else:
        for _ in range(n):
            print("   -----  ")
            print("  |  O  | ")
            print("  !  -  ! ")
            print("  !  -  ! ")
except ValueError:
    print("Vale sisend. Palun sisestage täisarv.")  # Käitleme vea, kui sisestatud väärtus pole täisarv
print()



#2
n = int(input("Sisestage arv n: "))  # Küsime kasutajalt sisendit arvu n jaoks
võimsus = int(input("Sisestage astendaja: "))  # Küsime kasutajalt sisendit astendaja jaoks

maksimaalne_väärtus = n ** võimsus  # Arvutame maksimaalse võimaliku väärtuse
võimsused = (i ** võimsus for i in range(1, int(maksimaalne_väärtus ** (1/võimsus)) + 1))  # Genereerime astmed

print("Arvu", n, "astmed, mitte rohkem kui", n, "^", võimsus, ":", *võimsused)  # Prindime välja arvu astmed
print()



#3
import random

õpilaste_arv = random.randint(1, 10)  # Juhuslik õpilaste arv vahemikus 1 kuni 10
hinded = ()

# Loob igale õpilasele juhuslikud hinded
for _ in range(õpilaste_arv):
    hinnete_arv = random.randint(1, 5)  # Juhuslik arv hinnanguid vahemikus 1 kuni 5
    õpilase_hinded = (random.randint(1, 5) for _ in range(hinnete_arv))  # Juhuslikud hinded 1 kuni 5
    for hinne in õpilase_hinded:
        hinded += (hinne,)  # Lisab igale õpilasele juhuslikud hinded ilma extend() funktsiooni, kandiliste sulgudeta ja ilma listita

# Keskmise hinnete arvutamine
if hinded:
    summa = 0
    for hinne in hinded:
        summa += hinne
    keskmine_hinne = summa // len(hinded)  # Kasuta täisarvu jagamist keskmiseks hindeks
    print("Füüsika keskmine hinne", õpilaste_arv, "õpilased:", keskmine_hinne)
else:
    print("Keskmise tulemuse arvutamiseks puuduvad andmed.")
print()





#4
algne_kingitus = 1  # Algne kingitus
lävi = 100  # Lävi, millest suuremad kingitused ei tohiks ületada

kokku_kingitus = algne_kingitus  # Muutuja kokku kingituste summa hoidmiseks
vanus = 1  # Muutuja, mis esindab vanust ehk sünnipäeva numbrit

while kokku_kingitus <= lävi:
    kokku_kingitus += vanus  # Lisame iga järgmise aasta kingituse summale juurde
    vanus += 1  # Suurendame vanust iga järgmise aasta võrra

print("Kingitus ületab 100 dollarit", vanus, ". sünnipäevaks.")
print()


#5
# Määrame algväärtused
eelmine, praegune = 0, 1

# Trükime välja esimesed kaks numbrit
print(eelmine, praegune, end=" ")

# Määrame, mitu numbrit jadas soovime trükkida
n = 8

# Genereerime järgmised numbrid ja trükime need välja
for _ in range(n):
    järgmine_num = eelmine + praegune
    print(järgmine_num, end=" ")
    eelmine, praegune = praegune, järgmine_num
print()


﻿#15
for j in range(0,10,1):
    for i in range(0,10,1):
        print(i, end="   ")
    print()





