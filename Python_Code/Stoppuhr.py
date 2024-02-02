import time

input("Drücke Enter, um die Stoppuhr zu starten...")
startzeit = time.time()

input("Drücke Enter, um die Stoppuhr zu stoppen...")
endzeit = time.time()

gemessene_zeit = endzeit - startzeit
print("Gemessene Zeit: {:.2f} Sekunden".format(gemessene_zeit))
