from module1 import*
from keyboard import*
palgad=loe_failist_listisse("palgad.txt")
inimesed=loe_failist_listisse("inimesed.txt")

while 1:
    print("*"*100, "\nKeskmine - A\nMinimum - B\Maksimum - C\nOtsing - G\nLisa - V")
    print("Vajuta nuppu==>")

    if read_key()=="A":
        kesk_palk=round(keskmine(palk),2)
        print("Keskmine palk on ", kesk_palk)
    elif read_key()=="B":
        min_palk, kellel=minimum(palk,inimesed)
        print("Minimaalne palk=> ", min_palk, "Kellel=> ",  kellel)
    elif read_key()=="C":
        max_palk, kellel=maksimum(palk, inimesed)
        print("Maksimaalne palk=> ", max_palk, "Kellel=> ",  kellel)



















palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
otsing_nimi_jargi(inimesed,palgad)