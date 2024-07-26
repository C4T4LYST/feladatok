# be kér egyértéket 5 és 10 között majd, 
# miután stringként érkezik meg az input functiontől,
# ezért int-é konvertáljuk az 'int()' functionnel
# és azt eltárolja a 'szam' valtozóban
szam = int(input('Adj meg egy számot 5 és 10 között! '))

# ha a szám kissebb mint öt VAGY nagyobb mint 10 addig fut a ciklus 
# while szam < 5 or 10 < szam:

# a 'not' szó megfordíja a kitételt szóval nem addig fut 
# amíg a szám öt és 10 közéesik hanem ha nem e két szám között helyeszkedik el
while not 5 <= szam <= 10:
    # be kér egyértéket 5 és 10 között majd, 
    # miután stringként érkezik meg az input functiontől,
    # ezért int-é konvertáljuk az 'int()' functionnel
# és azt eltárolja a 'szam' valtozóban
    szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között! '))
    #elejére ugrika ciklus

# a program vége, ki írja hogy rendben
print('Rendben!')     
    
