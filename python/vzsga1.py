print("Ez a program kiszámolja a téglatest területét, felületét")
print("Kérlek add meg ezeket az értékeket cm-ben")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

print("   _______________")
print("  /              /|")
print(" /              / |")
print("/______________/  |")
print("|              |  /")
print("|              | /")
print("|______________|/")


ter = a * b * c
fel = 2 * (a * b + b * c + a * c )

print("A= " + str(fel) + " cm2\nV= " + str(ter) + " cm3")