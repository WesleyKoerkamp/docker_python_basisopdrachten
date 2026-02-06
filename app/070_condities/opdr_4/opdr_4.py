# Opdracht 4 condities
# Naam student: Wesley Koerkamp
# Groep: 4ITX1



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...

gevonden = False
for topping in toppings:
    if keuze == topping[0]:
        print(f"U heeft {keuze} besteld. Dat kost {topping[1]}")
        gevonden = True
        break

    if not gevonden:
        print("De keuze die u maakt zit niet in ons assortiment. Kies een topping uit de lijst.")
        print(f"Onze toppings zijn: {beschikbare_toppings}")
        break