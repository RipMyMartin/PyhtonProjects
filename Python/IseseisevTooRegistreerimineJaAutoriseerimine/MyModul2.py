import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

def sisselogimine(kasutajanimi, parool, kasutajad, paroolid):
    """Funktsioon kontrollib sisselogimisel kasutajanime ja parooli."""
    if not kasutajanimi or not parool:
        print("Palun sisestage nii kasutajanimi kui ka parool.")
        return

    if kasutajanimi in kasutajad:
        if parool == paroolid[kasutajad.index(kasutajanimi)]:
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

def unustatud_parool(kasutajanimi, uus_parool, kasutajad, paroolid, saatja_email, saatja_parool):
    """Funktsioon saadab kasutajale e-kirja uue parooliga."""
    if kasutajanimi in kasutajad:
        paroolid[kasutajad.index(kasutajanimi)] = uus_parool

        # E-kirja loomine
        msg = MIMEMultipart()
        msg['From'] = saatja_email
        msg['To'] = kasutajanimi  # Võiks olla kasutaja e-posti aadress
        msg['Subject'] = "Uus parool"

        # Sõnumi sisu
        message = f"Teie uus parool on: {uus_parool}"
        msg.attach(MIMEText(message, 'plain'))

        # E-kirja saatmine
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(saatja_email, saatja_parool)
            server.sendmail(saatja_email, kasutajanimi, msg.as_string())
            print("E-kiri saadetud edukalt")
        except Exception as e:
            print("Viga e-kirja saatmisel:", str(e))
        finally:
            server.quit()

        print("Parool taastatud edukalt. Uus parool saadetakse e-posti teel.")
    else:
        print("Kasutajanimega seotud kasutajat ei leitud.")

