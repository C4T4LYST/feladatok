import math


print("Kör kerület, terület számítás")
r = int(input(" 'r' > "))
ker = round(2 * r* math.pi, 2)
ter = round(math.pi * (r**2), 2)
print("\n Kerület: " + str(ker) + "\n Terület: " + str(ter))