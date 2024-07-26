from dataclasses import dataclass
import os 
os.system('cls')

dk = 1
sor = 1

while sor <= 5:
    oszlop = 1
    while oszlop <= dk:
        print("* ", end="")
        oszlop += 1
    print("")
    dk += 1
    sor += 1