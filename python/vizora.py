print(" viz számla számítás")
asd = int(input("Előző havi víz óra álás (M^3) > "))
sad = int(input("Jelenlegi havi víz óra álás (M^3) > "))
dsa = ( asd - sad )

if dsa <= 10:
    print("Alacsony fogyasztás")
else:
    print("Magas fogyasztás")

print("\n Fizetendő: " + str(dsa* 360))

