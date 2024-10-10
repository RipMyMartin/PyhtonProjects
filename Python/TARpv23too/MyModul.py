import random
import string

def salasona(pikkus: int):
    """Funktsioon genereerib juhusliku parooli."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(pikkus))

def registreeri_kasutaja(kasutajanimi, parool, kasutajad, paroolid):
    """Funktsioon registreerib uue kasutaja, kui kasutajanimi on vaba."""
    if kasutajanimi in kasutajad:
        print("Kasutajanimi on juba võetud.")
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
            print("Sisselogimine õnnestus.")
        else:
            print("Vale parool.")
    else:
        print("Kasutajanimi ei eksisteeri.")

def muuda_parool(kasutajanimi, vana_parool, uus_parool, kasutajad, paroolid):
    """Funktsioon võimaldab kasutajal muuta oma parooli."""
    if kasutajanimi in kasutajad and vana_parool == paroolid[kasutajad.index(kasutajanimi)]:
        paroolid[kasutajad.index(kasutajanimi)] = uus_parool
        print("Parool muudetud edukalt.")
    else:
        print("Vale kasutajanimi või vana parool.")

def unustatud_parool(kasutajanimi, uus_parool, kasutajad, paroolid):
    """Funktsioon võimaldab kasutajal taastada unustatud parooli."""
    if kasutajanimi in kasutajad:
        paroolid[kasutajad.index(kasutajanimi)] = uus_parool
        print("Parool taastatud edukalt.")
    else:
        print("Kasutajanimega seotud kasutajat ei leitud.")