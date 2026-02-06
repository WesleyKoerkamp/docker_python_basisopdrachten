# Opdracht 3 input functie
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

# Hier komt je code...

items = []

for i in range(5):
    item = input("Voer een item in: ")
    items.append(item)

items.sort(key=str.lower, reverse=True)

print(items)