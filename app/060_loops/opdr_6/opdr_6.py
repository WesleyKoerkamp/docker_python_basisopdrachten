# Opdracht 3 input functie
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

# Hier komt je code...

# Hier start de for-loop

pizza = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

pizza.sort()
print(pizza)

pizza.append('yo-favorito')
print(pizza)

pizza.remove('olivio')
print(pizza)

print(pizza[:3])

midden_index = len(pizza) // 2
print([pizza[midden_index]])

print(pizza[-3:])