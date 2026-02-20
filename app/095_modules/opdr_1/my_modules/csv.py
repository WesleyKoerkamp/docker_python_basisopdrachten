def lees_bestand(bestandsnaam):
    """Leest een CSV-bestand en geeft de inhoud terug als lijst."""
    gegevens = []
    
    try:
        with open(bestandsnaam, "r") as bestand:
            for regel in bestand:
                regel = regel.strip()
                gegevens.append(regel.split(","))
        return gegevens
    
    except FileNotFoundError:
        print("Bestand niet gevonden.")
        return []


def toon_gegevens(gegevens):
    """Toont de gegevens netjes op het scherm."""
    for rij in gegevens:
        print(" | ".join(rij))