# létrehozza a 'sor' változót 1-es értékkel
sor = 1
#addig fut amiíg a 'sor' kissebb vagyegyenlő mint a 3
while sor <= 3:
    # létrehozza a 'oszlop' változót 1-es értékkel
    oszlop = 1
    #addig fut amiíg a 'oszlop' kissebb vagyegyenlő mint a 5
    while oszlop <= 5:
        #ki irja azt hogy 'O ' és a sort '' - ral zájra sortörés helyett
        print('O ', end='')
        # oszlopot megnöveli 1-gyel
        oszlop = oszlop + 1
    #sort tör
    print('')
    #sort megnöveli 1gyel
    sor = sor + 1       
    