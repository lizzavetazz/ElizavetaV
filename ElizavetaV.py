from keyboard import*
print("Kivi, Paber, Käärid")
while True:
    try:
        if read_key()=="k":
            print("Oli valitud kivi")
    except:
        ValueError
v1=["Kivi,"Paber",Käärid"]
v2=["Kivi,"Paber",Käärid"]
m=3
while m not in [1,2,3]:
    try:
        m=int(input("Kellega mängime?\n1 - inimestega\n2-robotiga\n3-robot-robotiga"))
    except:
        ValueError

if m==1:
    print("Mängime inimestega")
    while True:
        print("Mängime")
        if read_key()=="n": break
        p1=choice(v1)
        p2=choice(v2)
        if p1==p2: print("Viik")
        if p1==v: print ("2")
        if p1="1": print("1")
        
elif m==2:
    print("Mängime robotiga")
    while True:
        print("Mängime")
        if read_key()=="n": break
        p1=choice(v1)
        p2=choice(v2)
        if p1==p2: print("Viik")
        if p1==v: print ("2")
        #if p1=="3": print ("3")
       
elif m==3:
    print("Mängib robot-robotiga")
    while True:
        if read_key()=="n": break
        p1=choice(v1)
        p2=choice(v2)
        if p1==p2: print("Viik")
        if p1==v1[0] and p2==v2[1] or p1==v1[3] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
            print("Võitis 1")
        else:
            print("Võitis 2")
else:
    print("On vaja valida õige ")


while (arv == 0):
        player = int(input("1 -> kivi, 2 -> paber, 3 -> käärid. "))
        if (player == 1 or player == 2 or player == 3):
            arv = 1  
if player == 1:
    print("Te valisite kivi")
if player == 2:
    print("Te valisite paber")
if player == 3:
    print("Te valisite käärid")
#bot valib
comp = random.randint(1, 3)
if comp == 1:
    print("Comp valis kivi")
elif comp == 2:
    print("Comp valis paber")
elif comp == 3:
    print("Comp valis käärid")
elif player == 1 and comp == 2:
        win = 1
elif win == 0:
        print("Viik!")
elif win == 1:
        print("Võitja on player!")
else win == 2:
        print("Võitja on comp!")
