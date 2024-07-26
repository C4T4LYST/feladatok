import os 
os.system("cls")
print("=========================")
print("Kocka felszíne, térfogata") 
print("=========================") 
print("Add meg a kocka oldalának hosszát cm-ben!")


a = int(input("a="))

print("   ________")
print("  /       /|")
print(" /       / |")
print("/_______/  |")
print("|       |  |")
print("|       |  /")
print("|       | / ")
print("|_______|/  ")

A = 6*(a**2)
V = a**3

print("A= ",  A, "cm2")

print("V= ", V, "cm3")

input()