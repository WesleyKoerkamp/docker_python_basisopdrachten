# Opdracht 3 Tekst opslaan
# Naam student: Wesley Koerkamp
# Groep: 4ITX1

def encrypt(tekst):
    resultaat = ""
    
    for letter in tekst:
        if letter.isalpha():  # Controleer of het een letter is
            if letter.islower():
                nieuwe_letter = chr((ord(letter) - ord('a') + 5) % 26 + ord('a'))
            else:
                nieuwe_letter = chr((ord(letter) - ord('A') + 5) % 26 + ord('A'))
            resultaat += nieuwe_letter
        else:
            resultaat += letter  # Spaties en leestekens blijven gelijk
            
    return resultaat


def decrypt(tekst):
    resultaat = ""
    
    for letter in tekst:
        if letter.isalpha():
            if letter.islower():
                nieuwe_letter = chr((ord(letter) - ord('a') - 5) % 26 + ord('a'))
            else:
                nieuwe_letter = chr((ord(letter) - ord('A') - 5) % 26 + ord('A'))
            resultaat += nieuwe_letter
        else:
            resultaat += letter
            
    return resultaat


# Hoofdprogramma
invoer = input("Geef de tekst die je wilt encrypten: ")

versleuteld = encrypt(invoer)
print("Versleuteld:", versleuteld)

ontsleuteld = decrypt(versleuteld)
print("Ontsleuteld:", ontsleuteld)