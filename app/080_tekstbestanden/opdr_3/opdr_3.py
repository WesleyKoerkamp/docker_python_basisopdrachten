# Opdracht 3 Tekst opslaan
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

tekst = input("Voer een tekst in die je wilt encrypten: \n")

versleuteld = ""

for letter in tekst:
    if letter.isalpha():

        if letter.isupper():
            base = ord('A')
        else:
            base = ord('a')

    nieuwe_code = (ord(letter) - base + 1) % 26 + base
    versleuteld += chr(nieuwe_code)
else: 
    versleuteld += letter

print(versleuteld)