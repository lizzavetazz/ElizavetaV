#2 
def kustutamine(i,p): #удаляем человека из списка
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

#7 
def otsing_nimi_jargi(inimesed:list,palgad:list):
    """Tagastame järjed või tekst
    :rtype var:tulemus
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
                t.append(nimi+str(palk))
            return
        else:
            t="Ei ole nimekirjas"
            print(t)

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]