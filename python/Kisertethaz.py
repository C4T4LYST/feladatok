#Kísértett há
from random import randint
print("Kísértettház")

bator_vagyok = True
pontszam = 0

def getIt(number):
    asd = "( "
    for kl in range(1,number + 1):
        asd += " "+ str(kl) + " ,"
    asd = asd[:-1]
    asd += ")"
    return asd

while bator_vagyok:
    ajtok = randint(3,6)
    if(pontszam == 0):
       ajtok = 3
    szellem_ajto = randint(1,ajtok)
    print("\n " + str(ajtok) +" ajtó van elötted...")
    print("Az egyik mögött egy szellem van")
    print("Melyiket nyitod ki? " + getIt(ajtok))
    ajto_szam = int(input(" > "))

    if ajto_szam == szellem_ajto:
        print("Talákoztál a szellemmel!")
        bator_vagyok = False
    else:
        print("\n Nincs szellem")
        print("Lépje be a következő szobába")
        pontszam += 1

print("Véget ért a játék")
if pontszam > 0:
    print("Gratulálok a " + str(pontszam) + " pontoshoz!" )
else:
    print("bena")