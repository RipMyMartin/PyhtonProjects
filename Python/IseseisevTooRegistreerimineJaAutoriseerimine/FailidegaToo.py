from os import system
from gtts import *

def loeFailist(fail:str)->list:
    """Loeme failist read ja salvestame järendisse. Funktsioon
    tagastab järjend
    :param str fail:
    :rtype: list
    """

    f=open(fail,"r",encoding="utf-8") #зделать конструктсую try
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def kirjutaFailisse(fail:str, jarjend=[]):
    """ümberkirjutab failid sisse

    """
    n=int(input("Sisestage mitu elemendi: "))
    for i in range(n):
        jarjend.append(input(f"{i+1}. element:  "))
    f=open(fail,"w",encoding="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()

def LoePasJaLog(fail:list)->any:
    """Loeb failist andmed, mis oli sisestatud farmaadis "login:password" igas reas eraldi


    """
    fail=open(fail,"r",encoding="utf-8")
    log=[]
    pas=[]
    logPas=[]
    for line in fail:
        n=line.find(":")
        log.append(line[0:n].strip())
        pas.append(line[n+1:len(line)].strip())
        l,p=line.strip().split(":")
        logPas[l]=p
    fail.close()
    return log,pas,logPas


def heli(tekst:str,keel:str):
    obJ=gTTS(text=tekst,lang=keel,show=False).save("heli.mp3")
    system("heli.mp3")

tekst=input("Sisestage tekst: ")
heli(tekst,"ru")


kirjutaFailisse("Text.txt")

paevad = loeFailist("paevad.txt")
print(paevad)


