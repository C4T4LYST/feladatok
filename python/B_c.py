import os 
os.system('cls')

print("lista elemek beolvasása: ")
nevek = []
with open("nevek.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        nev = sor.strip()
        nevek.append(nev)
        print(nev, ';', end="")

print("")

print("Ennyi ember van a listában:" , len(nevek))

print("12 karaktert meghaladó nevek:")
for adat in nevek:
    if len(adat) > 12:
        print(adat)

kiiras = open("nevsorba.txt", "w")
print(nevek.sort())

for adat in nevek:
    print(adat, file=kiiras)

kiiras.close()
input()