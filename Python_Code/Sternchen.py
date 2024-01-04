num_rows = int(input("Gib die Anzahl der Reihen ein: "))
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
      print("* ", end="")
    k = k + 1
    print()