from MyModul2 import *

kasutajad = []
paroolid = []

while True:
    print("\n0 - Registreerimine\n1 - Autoriseerimine\n2 - Nime või parooli muutmine\n3 - Unustatud parooli taastamine\n4 - Lõpetamine")
    valik = input("Sisestage number: ")
    
    if valik == "4":
        break

    kasutajanimi = input("Sisestage kasutajanimi: ")

    if valik == "0":
        valik_parool = input("Kas soovite sisestada oma parooli (s) või lasta süsteemil genereerida parool (g)? ")
        if valik_parool.lower() == "s":
            parool = input("Sisestage parool: ")
        elif valik_parool.lower() == "g":
            parool = salasona(12)
        registreeri_kasutaja(kasutajanimi, parool, kasutajad, paroolid)

    elif valik == "1":
        valik_parool = input("Kas soovite sisestada oma parooli (s) või lasta süsteemil genereerida parool (g)? ")
        if valik_parool.lower() == "s":
            parool = input("Sisestage parool: ")
        elif valik_parool.lower() == "g":
            sisselogimine(kasutajanimi, None, kasutajad, paroolid)

    elif valik == "2":
        vana_parool = input("Sisestage vana parool: ")
        uus_parool = input("Sisestage uus parool: ")
        muuda_parool(kasutajanimi, vana_parool, uus_parool, kasutajad, paroolid)

    elif valik == "3":
        unustatud_parool(kasutajanimi, None, kasutajad, paroolid)









import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Funktsioon juhusliku parooli genereerimiseks
def loo_juhuslik_parool(pikkus=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(pikkus))

# Funktsioon e-kirja saatmiseks
def saada_e_kiri(saaja_email, teema, sisu):
    smtp_server = "smtp.gmail.com"
    port = 587
    saatja_email = "martinsild.mr@gmail.com"
    parool = input("Sisestage oma e-posti parool: ")

    sõnum = MIMEMultipart()
    sõnum['From'] = saatja_email
    sõnum['To'] = saaja_email
    sõnum['Subject'] = teema

    sõnum.attach(MIMEText(sisu, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(saatja_email, parool)
        server.sendmail(saatja_email, saaja_email, sõnum.as_string())
        print("E-kiri saadetud edukalt")
    except Exception as e:
        print("Viga e-kirja saatmisel:", str(e))
    finally:
        server.quit()

# Funktsioon parooli lähtestamiseks
def lähtesta_parool(kasutajanimi, email, kasutajad, paroolid):
    if kasutajanimi in kasutajad:
        uus_parool = loo_juhuslik_parool()
        vana_parool = paroolid[kasutajad.index(kasutajanimi)]
        paroolid[kasutajad.index(kasutajanimi)] = uus_parool
        saada_e_kiri(email, "Parooli lähtestamine", f"Teie uus parool: {uus_parool}\nVana parool: {vana_parool}")
        print("Parool lähtestatud edukalt. Kontrollige oma e-posti uue parooli jaoks.")
    else:
        print("Kasutajanimi ei leitud.")

# Funktsioon unustatud parooli taastamiseks
def unustatud_parool(kasutajanimi, email, kasutajad, paroolid):
    if kasutajanimi in kasutajad:
        uus_parool = loo_juhuslik_parool()
        paroolid[kasutajad.index(kasutajanimi)] = uus_parool
        saada_e_kiri(email, "Parooli lähtestamine", f"Teie uus parool: {uus_parool}")
        print("Parool taastatud edukalt. Kontrollige oma e-posti uue parooli jaoks.")
    else:
        print("Kasutajanimi ei leitud.")

# Näide kasutamisest
kasutajad = ["kasutaja1", "kasutaja2"]
paroolid = ["parool1", "parool2"]

kasutajanimi = input("Sisestage oma kasutajanimi: ")
email = input("Sisestage oma e-posti aadress: ")

lähtesta_parool(kasutajanimi, email, kasutajad, paroolid)

