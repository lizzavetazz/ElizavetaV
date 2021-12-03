from module1 import*
from keyboard import*
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("*"*100, "\nOtsing - 1\nMinimum - 2\Suurim - 3\nOtsing - 4\nLisa - 5")
    print("Vajuta nuppu==>")
    if read_key()=="1":
        otsing_nimi_jargi=(inimesed)
        print("Otsime=> ", otsing_nimi_jargi)
    elif read_key()=="2":
        min_palk, kellel=minimum(palk,inimesed)
        print("Minimaalne palk=> ", min_palk, "Kellel=> ",  kellel)
    elif read_key()=="3":
        suurim_palk, kellel=maksimum(palk, inimesed)
        print("Suurim palk=> ", suurim_palk, "Kellel=> ",  kellel)
    elif read_key()=="4":
        kustutamine(palk, inimesed)
        print("Kustutamine=> ", kustutamine, "Kellel=> ",  kellel)
    elif read_key()=="5":
        lisa(palk,inimesed)
        print("Lisame=> ", lisa, "Kellel=> ",  kellel)


