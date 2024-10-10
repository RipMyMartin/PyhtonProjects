import random
import time

while True:
    try:
        raha = int(input("Sisestage kui palju raha te tahate kaotada: "))
        if raha <=0:
            print("Te olete sisestanud negatiivse arvu või nulli, sisestage positiivse numberi:  ")
        else:
            break
    except ValueError:
        print("Te olete sisetanud midagi muud, sisestage number ")

print("Tere tulemast kasiinosse!")
print("Siin kasiinos on mäng, kus võitmine on võimatu.")

while raha >= 10:
    print(f"\nTeil on hetkel {raha} eurot.")
    while True:
        try:
            panus = int(input("Palun sisestage oma panus (vähemalt 10 eurot): "))
            if panus < 10:
                raise ValueError("Panus peab olema vähemalt 10 eurot!")
            if panus > raha:
                raise ValueError("Teil pole piisavalt raha selle panuse tegemiseks!")
            break
        except ValueError:
            print("Te olete sisetanud midagi muud, sisestage number ")
            
    print("Pöörutan ratast...")
    time.sleep(1)  
    varv = random.randint(1, 10)
    for frame_number in range(5):
        if frame_number == 0:
            print("|   |   |   |", end="\r")
        elif frame_number == 1:
            print("| {} |   |   |".format(varv), end="\r")
        elif frame_number == 2:
            print("| {} | {} |   |".format(varv, varv), end="\r")
        elif frame_number == 3:
            print("| {} | {} | {} |".format(varv, varv, varv), end="\r")
        elif frame_number == 4:
            print("| {} | {} | {} |".format(varv, varv, varv), end="\r")
        time.sleep(0.5)  
        
    print()

    if varv == 10:
        print("Te võitsite!")
        raha += panus
    else:
        print("Te kaotasite!")

print("Teil ei ole piisavalt raha, et mängida. Aitäh mängimast! Teie järel olev summa on", raha, "eurot.")




raha = [100]

print("Tere tulemast kasiinosse!")
print("Siin kasiinos on mäng, kus võitmine on võimatu.")

while True:
    print("\nKas soovite mängida? (j/e)")
    vastus = input().lower()
    
    if vastus != 'j':
        print("Aitäh mängimast! Nägemist!")
        break
    
    print("Pöörutan ratast...")
    print("Õnne teile!")

    # Genereerime juhusliku numbri 1 kuni 10
    tulemus = random.randint(1, 10)

    # Kuna see on "võimatu" mäng, siis alati kaotate
    print("Teie number on:", tulemus)
    print("Te kaotasite! Proovige uuesti.")
    
    if tulemus == 10:
        print("Teie number: ", tulemus)
        print("Te võitsite! Kas tahate mängida uuesti?")
    

        


#14
#Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

    #Väljasta linnad eraldi ridadena.
    #Järjesta need tähestikulisse järjekorda.
    #Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
    #Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
    #Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna", kus linnade arv leitakse vastava funktsiooni abil. 

# Algsete linnade järjend
linnad = ["Amsterdam", "Berliin", "Madrid", "Pariis", "Rooma", "Stockholm"]

while True:
    # Väljastame linnad eraldi ridadena
    print("Linnad:")
    for i in range(len(linnad)):
        print(linnad[i])

    # Sorteerime linnad tähestikulises järjekorras
    linnad.sort()

    # Kasutaja sisestab kaks uut Euroopa pealinna
    uus_linn1 = input("Sisesta esimene uus Euroopa pealinn: ")
    uus_linn2 = input("Sisesta teine uus Euroopa pealinn: ")

    # Lisame uued linnad järjendisse
    linnad.append(uus_linn1)
    linnad.append(uus_linn2)

    # Sorteerime linnad uuesti tähestikulises järjekorras
    linnad.sort()

    # Esitame linnade nimed tähestikulises järjekorras koos järjekorranumbritega
    print("Linnade nimed tähestikulises järjekorras:")
    for i in range(len(linnad)):
        print(f"{i + 1}. {linnad[i]}")

    # Arvutame linnade arvu ja väljastame kokkuvõtteva lause
    linnade_arv = len(linnad)
    print(f"Meie järjendis on {linnade_arv} Euroopa pealinna.")

    # Küsime kasutajalt, kas ta soovib jätkata
    jätkamine = input("Kas soovid veel linnu lisada? (jah/ei): ")
    if jätkamine.lower() != "jah":
        break

#9
# Numbrite sisestamine kasutajalt
numbers = []
print("Sisesta numbrid ükshaaval (sisesta 'stop', et lõpetada):")

while True:
    kasutaja = input("Sisesta number või 'stop': ")
    if kasutaja.lower() == 'stop':
        break
    try:
        number = int(kasutaja)
        numbers.append(number)
    except ValueError:
        print("Palun sisesta ainult numbrid või 'stop'.")

# Kasvav sorteerimine
sort_kasvavas = sorted(numbers)
print("Kasvav sorteerimine:", sort_kasvavas)

# Kahanev sorteerimine
sort_kahanevas = sorted(numbers, reverse=True)
print("Kahanev sorteerimine:", sort_kahanevas)



#18
import random

print("Tere tulemast kasiinosse!")
print("Siin kasiinos on mäng, kus võitmine on võimatu.")

while True:
    print("\nKas soovite mängida? (jah/ei)")
    vastus = input().lower()
    
    if vastus != 'jah':
        print("Aitäh mängimast! Nägemist!")
        break
    
    print("Pöörutan ratast...")
    print("Õnne teile!")

    # Genereerime juhusliku numbri 1 kuni 10
    tulemus = random.randint(1, 10)

    # Kuna see on "võimatu" mäng, siis alati kaotate
    print("Teie number on:", tulemus)
    print("Te kaotasite! Proovige uuesti.")














































#from random import *
##6
#nimekirja1=[]
#nimekirja=[]
#n=int(input(" Nimekirja suurus: "))
#for i in range(n):





#numbrid = [10, 20, 30, 40, 50]

#if numbrid:
#    maksimum = max(numbrid)
    
#    if len(numbrid) == 0:
#        print("Loend on tühi")
#    else:
#        kasutu_number = maksimum / len(numbrid)
        
#        maksimumi_indeks = numbrid.index(maksimum)
#        numbrid[maksimumi_indeks] = kasutu_number
        
#        print("Kasutu number:", kasutu_number)
#        print("Loend pärast asendamist:", numbrid)
#else:
#    print("Loend on tühi")

   









#from random import *
#from string import * 
#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida)
#kogus=int(input("Mitu elemendi vahetame oma vahel "))
#if len(rida)//2>kogus:
#    for i in range(kogus):
#        a=rida[i]
#        rida[i]=rida[len(rida)-i-1]
#        rida[len(rida)-1-i]=a
#print(rida)



#    # Sorteerime linnad uuesti tähestikulises järjekorras
#    linnad.sort()

#    # Väljastame linnad koos järjekorranumbritega
#    print("Euroopa pealinnad tähestikulises järjekorras:")
#    for i, linn in enumerate(linnad, 1):
#        print(f"{i}. {linn}")

#    # Arvutame linnade arvu ja väljastame kokkuvõtteva lause
#    linnade_arv = len(linnad)
#    print(f"Meie järjendis on {linnade_arv} Euroopa pealinna.")

#    # Küsime kasutajalt, kas ta soovib jätkata
#    jätkamine = input("Kas soovid veel linnu lisada? (jah/ei): ")
#    if jätkamine.lower() != "jah":
#        break









#indeksid=["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", 
#        "Ida-Virumaa, Lääne-Virumaa, Jõgevama", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
#        , "Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa",
#       "Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    try:
#        indeks=int(input("Sisesta oma indeks: "))
#        indeks_elemendide_arv=len(str(indeks))
#        if indeks_elemendide_arv==5:
#            print("5numbriline indeks")
#            break
#        else:
#            print("On vaj 5numbriline anv(Indeks)")


#    except:
#        print("Vale andmetüüp! ")
#arv1=indeks//10000
#print(arv1)
#symbolid=list(str(indeks))
#print(f"Sa elad piirkonnas {indeksid[int(symbolid[0])-1]}")









##from string import *
##from venv import create
###1
##vokaalid = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü', 'õ']
##konsonandid = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
##markid=punctuation
##v=k=m=t=0
##tekst=input("Sisesta sõna või lause: ").lower()
##tekst_list=list(tekst)
##for taht in tekst_list:
##    if taht in vokaalid:
##        v+=1
##    elif taht in konsonandid:
##        k+=1
##    elif taht in markid:
##        m+=1
##    else:
##        t+=1
##print("Vokaalid:", v)
##print("konsonandid:", k)
##print("kirjavähemärgid:", m)
##print("Tühikud:", t)

##2
##nimed=[]
##for i in range(5):
##    nimi=input("Sisestage nimi: ").capitalize()
##    nimed.append(nimi)

##print("Loetelu oli: ", nimed)
##nimed.sort()
##print("Loetelu sorteeritud: ", nimed)
##for n in range(len(nimed)):
##    print(n+1,".",nimed[n],sep=" ")

##print("Viimasena oli lisatud: ", nimed[-1])

##nimekogum = []
##for i in range(5):
##    nimi = input("Sisestage nimi: ").capitalize()
##    nimekogum.append(nimi)

##nimekogum.sort()
##print("Nimed tähestikulises järjekorras:", nimekogum)
##viimane_lisatud = nimekogum[-1]
##print("Viimati lisatud nimi:", viimane_lisatud)

##opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']
##unikaalsed_opilased = []

##for nimi in opilased:
##    if nimi not in unikaalsed_opilased:
##        unikaalsed_opilased.append(nimi)

##print("Unikaalsed nimed:", unikaalsed_opilased)

##vanused = [25, 30, 35, 40, 45]
##min_vanus = min(vanused)
##max_vanus = max(vanused)
##summa = sum(vanused)
##keskmine = summa / len(vanused)

##print("Vähim vanus:", min_vanus)
##print("Suurim vanus:", max_vanus)
##print("Vanuste kogusumma:", summa)
##print("Vanuste keskmine:", keskmine)




#nimed=[]
#for i in range(5):
#    nimi=input("Sisestage nimi: ").capitalize()
#    nimed.append(nimi)

#print("Loetelu oli: ", nimed)
#nimed.sort()
#print("Loetelu sorteeritud: ",nimed)
#for n in range(len(nimed)):
#    print(n+1,".",nimed[n],sep=" ")

#print("Vimasena oli lisatud: ",nimi)

#opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']

#nimed = []
#for nimi in opilased:
#    if nimi not in nimed:
#        nimed.append(nimi)

#print(nimed)
#vanused=[]
#for i in range(5):
#    vanus=int(input("Sisesta vanus: "))
#    vanused.append(vanus)
#maksimum=max(vanused)
#minimum=min(vanused)
#summa=sum(vanused)
#keskmine=summa/len(vanused)

#print(maksimum, "," , minimum, "," , summa, "," , keskmine)
## kuva ekraanile nimi koos vnusega 

#for i in range(5):
#    print(nimed[i], "on", vanused[i], "aastad vana")

##3
#from random import * 
#arvud=[]
#N=int(input("Mitu rida joonistame?"))
#S=input("Sisestage sümbol mida tahate kasutada: ")
#for p in range(N):
#    arvud.append(randint(1, 100))
##4
#for p in range(N):
#    print(arvud[p]*S)

##5
#indeks=["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", 
#        "Ida-Virumaa, Lääne-Virumaa, Jõgevama", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
#        , "Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa",
#       "Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    try:
#        indeks=int(input("Sisesta oma indeks: "))
#        indeks_elemendide_arv=len(str(indeks))
#        if indeks_elemendide_arv==5:
#            print("5numbriline indeks")
#        else:
#            print("On vaj 5numbriline anv(Indeks)")

#    except:
#        print("Vale andmetüüp! ")

