from MyPalgad import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]




while True:
    print("0-Näita anded veerudes\n1-andmete lisamine\n2-andmete_emaaldamine_nimi_jargi\n3-kellel_on_suurim_palk\n4-kellel_on_vahem_palk\n5-järjesta_palgad")
    valik=int(input())
    if valik==1:
        inimesed,palgad=Palgad_Inimesed(inimesed,palgad,int(input("Mitu inimest lisame?")))
    elif valik==0:
        andmed_veerudes(inimesed,palgad)

    elif valik==2:
        andmete_emaaldamine_nimi_jargi(inimesed,palgad)
    elif valik==3:
        kellel_on_suurim_palk(inimesed,palgad)
    elif valik==4:
        kellel_on_vahem_palk(inimesed,palgad)
    elif valik==5:
        sorteerimine(inimesed,palgad)