#képernyőtörlés 
import os 
os.system("cls")
print('====================')
print('100-hoz viszonyítás')
print('====================')
print('Adj meg egy számot és kiírom, 100-nál kisebb, nagyobb, vagy egyenlő-e vele!')
szam=int(input('Kérek egy számot: '))
if szam == 100:
    print("A szám egyenlő 100-zal.")
elif szam < 100:
    print("A szám kisebb 100-nál.")
else:
    print("A szám nagyobb 100-nál. ")