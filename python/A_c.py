
import os 
os.system('cls')
print("Listaelemek beolvasása:") 
fajl = open('haziallat.txt', 'r', encoding='utf-8')

allatok=[ ]
for sor in fajl: 
    nev, magas = sor.strip().split(";")
    allatok.append((nev, int(magas)))

fajl.close()

for adat in allatok:
    print(adat[0], adat[1])

print("Ennyi ember található a listában:", len(allatok))

db=0 
for adat in allatok:
    if adat[1]>3:
        db += 1

print('Ennyi embernek van 3-nál több háziállata: ', db)

kiiras = open('kiiratas.txt', 'w')
print('Ennyi ember található a listában:', len(allatok), file=kiiras)
print(db, 'Főnek 3-nál több háziállata van.', file=kiiras)
kiiras.close()

input()