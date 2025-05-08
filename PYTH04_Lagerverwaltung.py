"""************************************************
Einsendeaufgabe 4
************************************************"""


#Erstellt und gibt ein leeres Lager-Dictionary zurück
def erstelle_lager():
    return {}


#Eingabe einer neuen Kiste
def eingabe_kiste(lager):
    nummer = int(input("Kistennummer eingeben: "))
    if nummer in lager:
        print("Diese Kistennummer existiert bereits.")
        return
    breite = float(input("Breite eingeben: "))
    laenge = float(input("Länge eingeben: "))
    hoehe = float(input("Höhe eingeben: "))
    lager[nummer] = [breite, laenge, hoehe]
    print(f"Kiste {nummer} erfolgreich hinzugefügt.")


#Löschen einer vorhandenen Kiste
def loesche_kiste(lager):
    nummer = int(input("Kistennummer zum Löschen eingeben: "))
    if nummer in lager:
        del lager[nummer]
        print(f"Kiste {nummer} erfolgreich gelöscht.")
    else:
        print("Diese Kistennummer existiert nicht.")


#Ändern einer vorhandenen Kiste
def aendere_kiste(lager):
    nummer = int(input("Kistennummer zum Ändern eingeben: "))
    if nummer in lager:
        breite = float(input("Neue Breite eingeben: "))
        laenge = float(input("Neue Länge eingeben: "))
        hoehe = float(input("Neue Höhe eingeben: "))
        lager[nummer] = [breite, laenge, hoehe]
        print(f"Kiste {nummer} erfolgreich geändert.")
    else:
        print("Diese Kistennummer existiert nicht.")


#Anzeigen einer vorhandenen Kiste
def zeige_kiste(lager):
    nummer = int(input("Kistennummer zum Anzeigen eingeben: "))
    if nummer in lager:
        print(f"Kiste {nummer}: Breite={lager[nummer][0]}, Länge={lager[nummer][1]}, Höhe={lager[nummer][2]}")
    else:
        print("Diese Kistennummer existiert nicht.")


#Anzeigen aller vorhandenen Kisten
def liste_lager(lager):
    if not lager:
        print("Das Lager ist leer.")
    else:
        print("Lagerübersicht:")
        for nummer, daten in lager.items():
            print(f"Kiste {nummer}: Breite={daten[0]}, Länge={daten[1]}, Höhe={daten[2]}")


#Menü der Lagerverwaltung
def menue():
    lager = erstelle_lager()
    while True:
        print("\nLagerverwaltung")
        print("1. Kiste hinzufügen")
        print("2. Kiste löschen")
        print("3. Kiste ändern")
        print("4. Kiste anzeigen")
        print("5. Lager anzeigen")
        print("6. Beenden")
        wahl = input("Wählen Sie eine Option: ")
        if wahl == "1":
            eingabe_kiste(lager)
        elif wahl == "2":
            loesche_kiste(lager)
        elif wahl == "3":
            aendere_kiste(lager)
        elif wahl == "4":
            zeige_kiste(lager)
        elif wahl == "5":
            liste_lager(lager)
        elif wahl == "6":
            break
        else:
            print("Ungültige Eingabe.")

# Hauptprogramm
menue()
print("Programm beendet.")

