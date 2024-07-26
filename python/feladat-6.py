#feladat 3
print("felszín és térfogat számítás")

# ASCII art-nak hívott művészet
print(" ._________B_______________,")
print(" |`                        :\\")
print(" | a                       : \\")
print(" |  `                      :  \\")
print(" c   +---------B---------------+")
print(" |   :                     :   :")
print(" |__ : ____B_______________:   :")
print(" `   c                      \  :")
print("  a  :                       \ :")
print("   ` :                        \:")
print("    `:________B________________>")
print()

#---------------------------

#Változók bekérése és át

a = int(input("'a' hossza > "))
b = int(input(" 'b' hossza >"))
c = int(input(" 'c' hossza >"))

felszin = 2 * (a *c + b*c + a*b)
ter = a * b * c

print("\n Térfogat: " + str(ter) + "\n Felszín: " + str(felszin))
