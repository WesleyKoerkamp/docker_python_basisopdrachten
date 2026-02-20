# Opdracht 1 functies
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

# importeer de module csv...

from my_modules import csv

def main():
    bestandsnaam = "gegevens.csv"
    
    data = csv.lees_bestand(bestandsnaam)
    
    if data:
        print("Inhoud van het CSV-bestand:")
        csv.toon_gegevens(data)
    else:
        print("Geen gegevens om te tonen.")

if __name__ == "__main__":
    main()
