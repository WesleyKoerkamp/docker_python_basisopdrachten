# Opdracht 2 tekstbestanden
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
pogingen = 0

while True:
    gok = int(input("Raad mijn geheime getal \n"))
    pogingen += 1

    if gok < geheim_getal:
        print("Hoger")
    elif gok > geheim_getal:
        print("Lager")
    else:
        print(f"Gefeliciteerd! Je hebt het geheime getal geraden in {pogingen} pogingen.")
        break

# De rest moet jij doen.....

