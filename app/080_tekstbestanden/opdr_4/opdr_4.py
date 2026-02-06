# Opdracht 4 Tekst opslaan
# Naam student: Wesley Koerkamp
# Groep: 4ITX1


# Party enquete

vragen = [
    ("Wat is je voornaam?", "voornaam"),
    ("Wat is je achternaam?", "achternaam"),
    ("Wat neem je mee aan drank?", "drank"),
    ("Wat neem je mee aan eten?", "eten")
]

feestgangers = []

while True:

    persoon = {}
    for i, (vraag, sleutel) in enumerate(vragen):
        antwoord = input(vraag + " ")
        persoon[sleutel] = antwoord
    feestgangers.append(persoon)

    print("Bedankt voor het invullen van de enquete!")
    nog_een = input("Wil je nog een persoon toevoegen? (ja/nee) ")
    if nog_een != "ja":
        print("Zie je op de party!")
        break

with open("feestgangers.txt", "w") as bestand:
    for persoon in feestgangers:
        bestand.write(f"Voornaam: {persoon['voornaam']}\n")
        bestand.write(f"Achternaam: {persoon['achternaam']}\n")
        bestand.write(f"Drank: {persoon['drank']}\n")
        bestand.write(f"Eten: {persoon['eten']}\n")
        bestand.write("\n")  # Lege regel tussen personen

# IK HEB DE FEESTGANGERS 3X LATEN AANMELDEN!