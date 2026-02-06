# Opdracht 1 functies
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

MI = 1.609344

def kilometers_naar_miles(km):
    return km / MI
    # je code komt hier
    # het woordje pass hieronder kun je weghalen


def miles_naar_kilometers(miles):
    return miles * MI
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    

kilometers = 1223
miles = 867

print(f"{kilometers} kilometers is {kilometers_naar_miles(kilometers):.2f} miles")
print(f"{miles} miles is {miles_naar_kilometers(miles):.2f} kilometers")