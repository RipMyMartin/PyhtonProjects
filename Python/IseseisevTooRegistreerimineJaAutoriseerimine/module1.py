import random
import string

def salasona(pikkus: int):
    """Funktsioon genereerib juhusliku parooli."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(pikkus))

def registreeri_kasutaja(kasutajanimi, parool, kasutajad, paroolid):
    """Funktsioon registreerib uue kasutaja, kui kasutajanimi on vaba."""
    if kasutajanimi in kasutajad:
        print("Kasutajanimi on juba v�etud.")
    else:
        kasutajad.append(kasutajanimi)
        paroolid.append(parool)
        print("Kasutaja registreeritud edukalt.")
        print("Genereeritud parool:", parool)

def sisselogimine(kasutajanimi, parool, kasutajad, paroolid, auto_gen=False):
    """Funktsioon kontrollib sisselogimisel kasutajanime ja parooli."""
    if not kasutajanimi or not (parool or auto_gen):
        print("Palun sisestage nii kasutajanimi kui ka parool.")
        return

    if kasutajanimi in kasutajad:
        if parool == paroolid[kasutajad.index(kasutajanimi)] or auto_gen:
            print("Sisselogimine �nnestus.")
        else:
            print("Vale parool.")
    else:
        print("Kasutajanimi ei eksisteeri.")

def muuda_parool(kasutajanimi, vana_parool, uus_parool, kasutajad, paroolid):
    """Funktsioon v�imaldab kasutajal muuta oma parooli."""
    if kasutajanimi in kasutajad and vana_parool == paroolid[kasutajad.index(kasutajanimi)]:
        paroolid[kasutajad.index(kasutajanimi)] = uus_parool
        print("Parool muudetud edukalt.")
    else:
        print("Vale kasutajanimi v�i vana parool.")

def unustatud_parool(kasutajanimi, uus_parool, kasutajad, paroolid):
    """Funktsioon v�imaldab kasutajal taastada unustatud parooli."""
    if kasutajanimi in kasutajad:
        paroolid[kasutajad.index(kasutajanimi)] = uus_parool
        print("Parool taastatud edukalt.")
    else:
        print("Kasutajanimega seotud kasutajat ei leitud.")



from MyModul2 import *

kasutajad = []
paroolid = []

while True:
    print("\n0 - Registreerimine\n1 - Autoriseerimine\n2 - Nime v�i parooli muutmine\n3 - Unustatud parooli taastamine\n4 - L�petamine")
    valik = input("Sisestage number: ")
    
    if valik == "4":
        break

    kasutajanimi = input("Sisestage kasutajanimi: ")

    if valik == "0":
        valik_parool = input("Kas soovite sisestada oma parooli (s) v�i lasta s�steemil genereerida parool (g)? ")
        if valik_parool.lower() == "s":
            parool = input("Sisestage parool: ")
        elif valik_parool.lower() == "g":
            parool = salasona(12)
        registreeri_kasutaja(kasutajanimi, parool, kasutajad, paroolid)

    elif valik == "1":
        valik_parool = input("Kas soovite sisestada oma parooli (s) v�i lasta s�steemil genereerida parool (g)? ")
        if valik_parool.lower() == "s":
            parool = input("Sisestage parool: ")
        elif valik_parool.lower() == "g":
            sisselogimine(kasutajanimi, None, kasutajad, paroolid)

    elif valik == "2":
        vana_parool = input("Sisestage vana parool: ")
        uus_parool = input("Sisestage uus parool: ")
        muuda_parool(kasutajanimi, vana_parool, uus_parool, kasutajad, paroolid)

    elif valik == "3":
        uus_parool = input("Sisestage uus parool: ")
        unustatud_parool(kasutajanimi, uus_parool, kasutajad, paroolid)
        #martinsild.mr@gmail.com vray cpyb uxhk gyja 

