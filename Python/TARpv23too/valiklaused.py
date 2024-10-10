﻿from datetime import *




korrutis = 1
for i in range(8):
    arv = float(input(f"Sisestage {i + 1}. arv: "))
    if arv > 0:
        korrutis *= arv
print(f"Positiivsete arvude korrutis: {korrutis}")


korrutis = 1
arvud = [float(input(f"Sisestage {i + 1}. arv: ")) for i in range(8)]

# Korrutame ainult positiivsed arvud
for arv in arvud:
    if arv > 0:
        korrutis *= arv
print(f"Positiivsete arvude korrutis: {korrutis}")




#1
#for


for i in range(15):
    arv=float(input("Sisesta {0} .arv".format(i+1)))
    if arv==int(arv):
        r+=1
print("Täisarvde arv on "+str(r))
#while True
r=0
i=0
while i<15:
    i+=1
    arv=float(input("Sisesta {0} .arv".format(i)))
    if arv==int(arv):
        r+=1
    if i==15: break
print("Täisarvude arv on "+str(r))





































#14
maht=int(input("Bussi maht:  "))
i=int(input("Inimeste arv:  "))
ba=round(i/maht)
if i%maht!=0:
    ba+=1
vb=i%maht
print("kokku on vaja {0} Bussis ja viimasel sõidavad {1} inimest".format(ba,vb))







#11 
ta=date.today().year()
sp=date(int(input("Sünniaasta:  ")),int(input("Sünnikuu:  ")),int(input("Sünnipäev:  "))).year
if(ta-sp)%5==0:
    print("Juubel")
else:
    print("Tavaline sünnipäev")
















#1 Juku läheb kinno
nimi=input("Mis on sinu nimi?").capitalize()
print("Tere ",nimi) #Tere, Anna"
if nimi=="Juku":
    print("Lähme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:
        pilet="lastepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet) ##ilus ja õige vastus! "vale vastus" või "on vaja osta...."
else:
    print("Ma ootan Jukkut")
    
#2
nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")
print("Täna on",nimi1, "ja" ,nimi2, "pinginaabrid!")

#3
pikkus = float(input("Sisesta seina pikkus meetrites: "))
laius = float(input("Sisesta teise seina pikkus meetrites: "))
pindala = pikkus * laius
print("Põranda pindala on" ,pindala, "ruutmeetrit.")
soov = input("Kas soovid remonti teha? (jah/ei): ")
if soov.lower() == "jah":
    
    hind = float(input("Sisesta ruutmeetri hind: "))
    
    remondi_hind = pindala * hind
    print("Remondi hind on" ,remondi_hind, "eurot.")
    

#4
alghind = float(input("Sisesta alghind: "))
soodushind = alghind * 0.7 if alghind > 700 else alghind
print("30% soodustusega hind on" ,soodushind, "eurot.")

#5
temperatuur = float(input("Sisesta temperatuur: "))
if temperatuur > 18:
    print("Temperatuur on üle 18 kraadi, soovitav toasoojus talvel.")
else:
    print("Temperatuur on 18 kraadi või madalam.")
    
#6
# Küsi inimese pikkus
pikkus = float(input("Sisesta inimese pikkus meetrites: "))

# Teata, kas ta on lühike, keskmine või pikk
if pikkus < 1.6:
    print("Inimene on lühike.")
elif 1.6 <= pikkus < 1.8:
    print("Inimene on keskmise pikkusega.")
else:
    print("Inimene on pikk.")
    

#7
# Küsi inimese pikkus ja sugu
pikkus = float(input("Sisesta inimese pikkus meetrites: "))
sugu = input("Sisesta inimese sugu (m/n): ")

# Teata, kas ta on lühike, keskmine või pikk
if sugu.lower() == "m":
    if pikkus < 1.6:
        print("Inimene on lühike mees.")
    elif 1.6 <= pikkus < 1.8:
        print("Inimene on keskmise pikkusega mees.")
    else:
        print("Inimene on pikk mees.")
elif sugu.lower() == "n":
    if pikkus < 1.6:
        print("Inimene on lühike naine.")
    elif 1.6 <= pikkus < 1.8:
        print("Inimene on keskmise pikkusega naine.")
    else:
        print("Inimene on pikk naine.")
else:
    print("Vale sugu.")



#8 
from datetime import *
arve_nr= date.today()#datetime.now()
print(arve_nr)
tsekk="Arve:  "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

for toode in ["Piim", "Leib", "Komm"]:
    hind=randint(50,150)/100
    v=input("Toode:"+toode+"Hind"+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("mitu?"))
        tsekk+=toode+"  "+str(hind)+"   "+str(mitu)+"   "+str(mitu+hind)+"\n"
        summa+=mitu+hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
while True:
    raha=float(input("Maksa "+str(summa)+"\n"))
    if raha==summa:
        print("tänan ostu eest!")
        break 
    elif raha>summa:
        print("Tänan ostu eest! Tagasi "+str(raha-summa))
        break
    else:
        summa-=raha
        print("Maksa veel" +str(summa))



toode="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toode+"Hind"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("mitu?"))
    tsekk+=toode+"  "+str(hind)+"   "+str(mitu)+"   "+str(mitu+hind)+"\n"
    summa+=mitu+hind
toode="leib"
hind=randint(90,300)/100
v=input("Toode:"+toode+"Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("mitu?"))
    tsekk+=toode+"  "+str(hind)+"   "+str(mitu)+"   "+str(mitu+hind)+"\n"
    summa+=mitu+hind
toode="Kommid"
hind=randint(600,1500)/100
v=input("Toode:"+toode+"Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("mitu?"))
    tsekk+=toode+"  "+str(hind)+"   "+str(mitu)+"   "+str(mitu+hind)+"\n"
    summa+=mitu+hind
    toode="leib"
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
raha=float(input("Maksa "+str(summa)))
if raha==summa:
    print("tänan ostu eest!")
elif raha>summa:
    print("Tänan ostu eest! Tagasi "+str(raha-summa))
else:
    print("Maksa veel" +str(summa-raha))






#9
külg = float(input("Sisesta ruudu küljepikkus: "))
if külg > 0 and külg == külg:
    print("Tegemist on ruuduga.")
else:
    print("See ei ole ruut.")
    


#11

sünnipäev = int(input("Sisesta oma sünnipäev (aasta): "))

juubel = (2024 - sünnipäev) % 10 == 0
if juubel:
    print("Palju õnne, sul on juubeliaasta!")
else:
    print("Sul ei ole juubeliaastat.")
    
#12

hind = float(input("Sisesta toote hind eurodes: "))

if hind <= 10:
    allahindlus_protsent = 10
else:
    allahindlus_protsent = 20

soodustus = hind * (allahindlus_protsent / 100)
lõpplik_hind = hind - soodustus

print("Alghind:" ,hind, "eurot")
print("Allahindlus:" ,allahindlus_protsent,"%")
print("Lõplik hind:" ,lõpplik_hind, "eurot")

#13

sugu = input("Sisesta oma sugu (m/n): ")

if sugu.lower() == "m":
    vanus = int(input("Sisesta oma vanus: "))
    if 16 <= vanus <= 18:
        print("Oled sobiv kandideerima jalgpalli meeskonda!")
    else:
        print("Vabandame, sa ei sobi meeskonda vanuse tõttu.")
elif sugu.lower() == "n":
    print("Vabandame, meeskond on avatud ainult meestele.")
else:
    print("Vale sugu.")
    

#14

inimeste_arv = int(input("Sisesta inimeste arv: "))
bussi_kohtade_arv = int(input("Sisesta bussi kohtade arv: "))

busside_arv = inimeste_arv // bussi_kohtade_arv
viimase_bussi_inimesed = inimeste_arv % bussi_kohtade_arv

print("Vaja on" ,busside_arv, "bussi.")
print("Viimases bussis on" ,viimase_bussi_inimesed, "inimest.")








    














protsent=randint(0,100) #0-100 0-60-"2" , 61-75-"3",76-89-"4", 90-100"5"
print(protsent,"%", "on testi tulemus")
if protsent<0 or protsent>100:
    tulemus="valed andmed"
elif 0<protsent<60: #protsent>0 and protsent<60 ,0<protsent>60
    tulemus="hinne 2"
elif 60<=protsent<75:
    tulemus="hinne 3"
elif 75<=protsent<90:
    tulemus="hinne 4"
else:       #=elif 90<=protsent<=100:
    tulemus="hinne 5"
print(tulemus)
print()




arv=randint(0,100) #juhuslik täisarv vahemikust 0...100
print(arv)
if arv%2==0:
    print(arv, "on paaris arv")
else:
    print(arv, "on paaritu arv")
print()

print("tund on alanud")
hilinemine=input("kas õpilane on hilinenud?") 
# "JAH"- a.upper(), "jah"- a.lower() , Jah-a.capitalize() , jAH
if hilinemine.lower()=="jah":
    print("Õpilane ootab 30min ")
print("Õpilane astub klassi")
