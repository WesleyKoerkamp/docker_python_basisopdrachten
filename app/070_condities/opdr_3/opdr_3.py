# Opdracht 3 condities
# Naam student: Wesley Koerkamp
# Groep: 4ITX1




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

leeftijd_bezoeker = int(input("Geef uw leeftijd in aantal jaar \n"))

for groep, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_bezoeker <= max_leeftijd:
        print(f"U valt in de leeftijdscategorie: {groep}")
        korting = kortings_percentages[groep]
        print(f"U krijgt een korting van: {korting}%")
        prijs = normale_toegangsprijs * (1 - korting / 100)
        print(f"Uw toegangsprijs is daarom {prijs}")
        break