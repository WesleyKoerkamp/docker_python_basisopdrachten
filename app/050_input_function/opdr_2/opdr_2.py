# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Paul", "Kees", "Marie", "Hilda"]

gasten.insert(0, "Wesley")
print(gasten)

gasten.remove("Marie")
print(gasten)

index_kees = gasten.index("Kees")
gasten.insert(index_kees + 1, "George")
print(gasten)