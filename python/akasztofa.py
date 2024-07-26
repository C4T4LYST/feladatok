from random import *
import os
fl = open("texts.txt", encoding="utf8")

szavak = []
line = fl.readline()
while line:
    szavak.append(str(line))
    line = fl.readline()

ind = szavak[randint(0, len(szavak))].lower()
betuk = []

tippek = 10

def keres(array, szo):
    for alma in array:
        if alma == szo:
            return True
    
    return False

while True:
    os.system('cls')
    print("\n ", end="")
    for jk in ind:
        if keres(betuk, jk):
            print(jk, end=" ")
        else:
            print("_", end=" ")

    print("\n\n Még Ennyit tipelhetsz: ", end="")
    uzh = 0
    for uh in betuk:
        if not keres(ind, uh):
            uzh += 1

    print(tippek - uzh, end="\n")
    
    print("\n Eddig Teiipelt betűk: ", end="")
    for ol in betuk:
        print(ol, end=", ")

    hk = ""
    while True:
        hk = input("\n\n\n Kérlek Adj Meg egy betűt > ")
        if len(hk) == 1 and not keres(betuk, hk):
            break
        else:
            print("\n Ez a beű már volt vagy nem betűt irtál be!", end="")
    
    betuk.append(hk)
    

