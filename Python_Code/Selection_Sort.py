liste = [1, 5, 6, 8, 3]

n = len(liste)

for i in range(0, n):
    kleinste = i

    for j in range(i+1, n):
        if liste[j] < liste[kleinste]:
            kleinste = j
    liste[i], liste[kleinste] = liste[kleinste], liste[i]

    print(liste)
