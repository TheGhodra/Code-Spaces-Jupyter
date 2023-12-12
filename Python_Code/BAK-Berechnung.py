print("BAK-Berechnung nach Widmark")

name = input("Bitte gib deinen Namen ein: ")
gewicht = int(input("Gib bitte dein Gewicht in kg ein: "))
alkohol = int(input("Aufgenommene Menge Alkohol in g: "))
vfaktor = 0.7
bak = round(alkohol / (gewicht * vfaktor), 2)
print("Hallo ", name, ", dein BAK beträgt ", bak, " Promille")