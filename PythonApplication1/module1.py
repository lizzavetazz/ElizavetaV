#1
def otsing_nimi_jargi(inimesed, palgad):
    """Tagastame järjed või tekst
    :param list inimesed: Inimeste nimekiri
    :param list palgad: Palgade kogum
    :rtype: list, list 
    """
    nimi=input("Keda otsime?")
    for inimene in inimesed:
        if inimene==nimi:
            n=inimesed.count(nimi)
            print("Inimene on olemas, selline nimi kohtume ",n,"korda")
            b=0
            for i in range(n):
                k=inimesed.index(nimi,b)
                b+=k+1
                t.append(nimi+str(palgad))
                return palgad,inimesed
        else:
            t="Ei ole nimekirjas"
     



#2 
def min_palk():
    """Programm kontrollib ja nätab välja ekraanile inimesi, kelell on kõige väiksem palk
    :rtype str nimi: inimese nimi, kellel on kõige väiksem palk
    """
    palgad=[]
    with open("palgad.txt", "r") as f1:
        for strok in f1:
            palgad.append(strok.strip())
            inimesed=[]
            f=open("login.txt", "r")
            inimesed=[]
        for stroka in f:inimesed.append(stroka.strip())
        zp=palgad.copy()
        zp.sort()
        zp.reverse()
        a=zp[0]
        b=palgad.index(a)
        nimi=inimesed[b]
    return nimi

#3
def suurim_palk():
    """Programm kontrollib ja nätab välja ekraanile inimesi, kelell on kõige suurem palk
    :rtype str nimi: inimese nimi, kellel on kõige suurem palk
    """
    palgad=[]
    with open ("palgad.txt", "r") as f1:
        for stroka in f1:
            palgad.append(stroka.strip())
            f=open("inimesed.txt", "r")
            inimesed=[] 
        for stroka in f:
            inimesed.append(stroka.strip())
            f.close
            palgadS=palgad.copy()
            palgadS.sort()
            a=palgadS[0]
            b=palgad.index(a)
            inimesed[b]
        return nimi
#4
def kustutamine(inimesed,palgad): #удаляем человека из списка
    """Kustutame inimesi ja palga palgast
    :param list inimesed: Inimeste nimekiri
    :param list palgad: Palgade kogum
    :rtype: list, list 
    """
    nimi=input("Sisestage nime, keda kustutame: ")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #список индексов
                print(t,". ",i[e],"-", p[e])
                jaar=int(input("Järjenumber: "))
                i.pop(abi_list[jaar-1])
                p.pop(abi_list[jaar-1])
                andmed_ekranile(i,p)
            return inimesed, palgad

#5
def lisa(inimesed, palgad):
    """Lisame veel inimesi ja nende palgad listisse
    :param list inimesed: Inimeste nimekiri
    :param list palgad: Palgade kogum
    :rtype: list, list 
    """
    a=input("Sisesta nimi=>")
    inimesed.append(a)
    b=int(input("Sisesta palk=>"))
    palgad.append(b)
    return palgad,inimesed