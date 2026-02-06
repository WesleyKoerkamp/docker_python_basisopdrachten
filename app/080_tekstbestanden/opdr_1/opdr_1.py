# Opdracht 1 while-loops
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

# Jouw code komt hier

vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

antwoorden = []

for vraag in vragen:
    antwoord = input(vraag + " \n")
    antwoorden.append(antwoord)

with open("antwoorden.txt", "w") as bestand:
    for vraag, antwoord in zip(vragen, antwoorden):
        bestand.write(f"{vraag}\n{antwoord}\n\n")

print("Bedankt voor het invullen van de vragenlijst! Je antwoorden zijn opgeslagen in 'antwoorden.txt'.")