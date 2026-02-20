#!/usr/bin/env python3
# Dit is de module
# In dit bestand komen alle functies.
# Je kunt de functies in een ander .py bestand gebruiken door te starten  met:
# from my_modules import csv

def lees_bestand(bestandsnaam):
    personen = []
    
    try:
        with open(bestandsnaam, "r") as bestand:
            for regel in bestand:
                regel = regel.strip()
                voornaam, achternaam, plaats = regel.split(",")
                
                persoon = {
                    "voornaam": voornaam,
                    "achternaam": achternaam,
                    "plaats": plaats
                }
                
                personen.append(persoon)
                
        return personen
    
    except FileNotFoundError:
        print("Bestand niet gevonden.")
        return []


def filter(personen, filterveld, filterwaarde):
    """
    Filtert personen op basis van beginletters.
    Bijvoorbeeld:
    filter(personen, "voornaam", "ja")
    """
    
    resultaten = []
    
    for persoon in personen:
        waarde = persoon[filterveld]
        
        # case-insensitive vergelijken
        if waarde.lower().startswith(filterwaarde.lower()):
            resultaten.append(persoon)
    
    return resultaten