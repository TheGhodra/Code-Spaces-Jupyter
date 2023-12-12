def berechnung_stueckkosten(p_variable_kosten, p_stückzahl, p_fix):
    stueckkosten_ges = round((p_variable_kosten * p_stückzahl + p_fix) / p_stückzahl, 2)
    return stueckkosten_ges

print("Berechnung des Stückgewinns:")

variable_kosten = float(input("Bitte gib die Variablen Stückkosten ein: "))
fix = float(input("Bitte gib die fixen Kosten ein: "))
stückzahl = float(input("Bitte gib die Stückzahl ein: "))

stueckkosten_ges = berechnung_stueckkosten(variable_kosten, fix, stückzahl)

print("Die Stückkosten betragen ", stueckkosten_ges, " Euro.")