from random import *
nimed=["Mati","Meelis","Kati","Mati"]
while True:
    print("--------------------")
    v=input("N-näita andmet\nL - lisa andmeid\nK-andmete kustutamine\nH-andmete haldus\nI-positsiooni otsing\n")
    if v=="N":
        v=input("Kas juhusik(j) nimi või terve loetelu(t)")
        if v=="t":
            print(nimed)
        elif v=="j":
            print(choice(nimed))
    elif v=="L":
        v=input("Kas nimekirja lõppu(l) või positsioonile(p)")
        if v=="l":
            nimi=input("Sisesta nimi:" )
            nimed.append(nimi)
        elif v=="p":
            nimi=input("Sisesta nimi:" )
            ind=int(input("Mis kohale:" ))
            nimed.insert(ind-1,nimi)
    elif v=="K":
        v=input("Kas nimi järgi(n), indeksi järgi(i) või kõik nimed(k)")
        if v=="i":
            ind=int(input("Sisesta indeks:"))
            nimed.pop(ind-1)
        elif v=="k":
            nimi.clear()
        elif v=="n":
            nimi=input("Sisesta nimi:  ")
            mitu=nimed.count(nimi)
            if mitu>0:
                for i in range(mitu):
                    nimed.remove(nimi)
            elif v==nimi:
                print(f"{nimi} ei ole loetelus")
    elif v=="H":
        v=input("Sorteerimine(s),kopeerimine(k) või ümber pööramine(p)")
        if v=="s":
            v=int(input("A-z(1) või Z-a?(2)"  ))
            if v==1:
                nimed.sort(reverse=False)
            else v==2:
                nimed.sort(reverse=True)
        elif v=="k":
            nimed.copy()
        elif v=="p":
            nimed.reverse()
    elif v=="I":
        nimi=input("Sisesta nimi: ")
        mitu=nimed.count(nimi)
        if mitu>0:
            print(f"Seal on {mitu} {nimi}")
            for i in range(mitu):
                print(f"{nimi} on {i+1} positsioonil")
        else:
            print(f"{nimi} ei ole loetelus.")


