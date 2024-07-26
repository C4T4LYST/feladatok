#képernyő törlés
from encodings import utf_8
import os
os.system("cls")

print("lista elemek be olvasása")
forras = open('zene.txt', encoding="UTF-8")
zene = []
for sor in forras:
    nev, album = sor.strip().split(";")
    zene.append(nev, int(album))

forras.close()
print("Ennyi előadó van a listában", len(zene))


