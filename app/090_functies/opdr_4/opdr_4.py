# Opdracht 1 functies
# Naam student: Wesley Koerkamp
# Groep: 4ITX1


def volledige_naam(lijst_met_namen):
    # hier komt jouw code
    # Het woordje pass mag je weghalen
    for persoon in lijst_met_namen:
        voornaam = persoon["voornaam"]
        tussenvoegsel = persoon["tussenvoegsel"]
        achternaam = persoon["achternaam"]
        
        if tussenvoegsel:
            volledige_naam = f"{voornaam} {tussenvoegsel} {achternaam}"
        else:
            volledige_naam = f"{voornaam} {achternaam}"
        
        print(volledige_naam)


namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)