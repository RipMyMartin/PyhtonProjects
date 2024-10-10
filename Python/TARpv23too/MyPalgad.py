def Palgad_Inimesed(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus inmesi ja plaka
    :param list i: Inimeste järjend
    :param list p: Palgate järjend
    :param list n: Inimeste arv
    :rtype list, list

    """
    if n>0:
        for j in range(n):
            nimi=input("Sisestage nimi: ").capitalize()
            palk=int(input("Sisestage palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p  
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    for j in range(len(i)):
        print(i[j],"-",p[j])

def andmete_emaaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andid ja tagastab listitud järjendid
    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    nimi=input("Keda kustutada ära(nimi): ")

    for j in range(0,len(i)):
        if nimi in i:
            i.remove(nimi)
            p.pop(j)
    return i,p

def kellel_on_suurim_palk(i:list,p:list)->list:
    """Funktsioon näitab kellel on suurim palk
    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    nimed=[]
    max_palk=max(p)
    ind=-1
    for palk in p:
        if palk==max_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

def kellel_on_vahem_palk(i:list,p:list)->list:
    """Funktsioon näitab kellel on väiksem palk
    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    nimed=[]
    min_palk=min(p)
    ind=-1
    for palk in p:
        if palk==min_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed


def sorteerimine(i:list,p:list):
    """Funktsiooni teeb palgade sorteerimist 

    :param list i:Inimeste järjend
    :param list p:Inimeste järjend

    """
    for n in range(0, len(i)):
        for n in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]

    return i,p