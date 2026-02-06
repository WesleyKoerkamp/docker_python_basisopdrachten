# Opdracht 1 functies
# Naam student: Wesley Koerkamp
# Groep: 4ITX1


def write_to_file(afile, atext):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    with open(afile, "a") as file:
        file.write(atext + "\n")

my_tekst = "Test tekst"
my_file = "test.txt"
write_to_file(my_file, my_tekst)

