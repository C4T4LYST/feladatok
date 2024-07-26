print("Kérlek adj meg egy számot!")
num = int(input(" > "))

maradek = num % 2

if maradek == 0:
    print("PÁROS!")
else:
    print("PÁRATLAN!")