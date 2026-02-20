# Opdracht 1 modules
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

from my_modules import csv


def toon_resultaten(resultaten):
    for persoon in resultaten:
        print(
            persoon["voornaam"],
            persoon["achternaam"]
        )


def main():
    personen = csv.lees_bestand("personen.csv")
    
    # Voorbeeld 1
    print("Filter op voornaam 'ja':")
    resultaten = csv.filter(personen, "voornaam", "ja")
    toon_resultaten(resultaten)
    
    print("\nFilter op voornaam 'Pie':")
    resultaten = csv.filter(personen, "voornaam", "Pie")
    toon_resultaten(resultaten)
    
    print("\nFilter op plaats 'd':")
    resultaten = csv.filter(personen, "plaats", "d")
    toon_resultaten(resultaten)


if __name__ == "__main__":
    main()