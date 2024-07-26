import os 
os.system('cls')

print("======================")
print(" Páros vagy Páratlan?")
print("======================")

szam = int(input("Adj meg egy számot: "))

if szam % 2 == 0:
    print("Páros")
else:
    print("Páratlan")