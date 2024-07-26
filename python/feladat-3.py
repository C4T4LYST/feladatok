#feladat 4

#további adat típusok és műveletek velük

# lista: több elemet tartalmazó adat
lista = [1, 2, 3]

#új elem hozzáadása a listához
lista.append(4)
#elem törlése a listából
lista.remove(2)
#elem indexének lekérdezése
print(lista.index(3))

#---------------------------------------------

# könyvtár: kulcs-érték párokat tartalmazó adat
dictionary = { "kulcs": "érték" } 

dictionary["kulcs"] = "új érték"
#kulcs-érték pár törlése
del dictionary["kulcs"]

#---------------------------------------------

# tuple: nem módosítható lista
tuple = (1, 2, 3)

# ezt nem lehet megváltoztatni