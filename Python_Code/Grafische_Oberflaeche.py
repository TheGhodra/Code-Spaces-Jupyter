from tkinter import *

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer auf den Button klickt
def button_action():
    anweisungs_label.config(text = "Ich wurde geändert!")

# Ein Fenster erstellen
fenster = Tk()

# Den Fenstertitle erstellen
fenster.title("Grafische Oberfläche")

#Label und Buttons ertsellen
change_button = Button(fenster, text = "Ändern", command = button_action)
exit_button = Button(fenster, text = "Beenden", command = fenster.quit)

anweisungs_label = Label(fenster, text = "Ich bin eine Anweisung: \n Klicke auf 'Ändern'")


info_label = Label(fenster, text = "Ich bin eine Info: \n Der Beenden Button schließt das Programm")

# Nun fügen wir die Komponenten unserem Fenster
# in der gewünschten Reihenfolge zu
anweisungs_label.pack()
change_button.pack()
info_label.pack()
exit_button.pack()


# In der Ereignisschleife auf Eingabe des Benutzers warten
fenster.mainloop()



