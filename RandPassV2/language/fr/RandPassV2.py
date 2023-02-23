import random
import string
import os.path

def GeneratePasswordLDP(length):
    # Concaténer les chaînes de caractères contenant les caractères souhaités pour le mot de passe
    characters = string.ascii_letters + string.digits + string.punctuation

    # Utiliser la fonction random.choices pour sélectionner un caractère aléatoire dans la chaîne de caractères "characters"
    # Répéter cette opération "length" fois pour obtenir un mot de passe de longueur "length"
    password = ''.join(random.choices(characters, k=length))

    return password

def GeneratePasswordLD(length):
    # Concaténer les chaînes de caractères contenant les caractères souhaités pour le mot de passe
    characters = string.ascii_letters + string.digits

    # Utiliser la fonction random.choices pour sélectionner un caractère aléatoire dans la chaîne de caractères "characters"
    # Répéter cette opération "length" fois pour obtenir un mot de passe de longueur "length"
    password = ''.join(random.choices(characters, k=length))

    return password

# Demander à l'utilisateur la longueur souhaitée pour le mot de passe
length = int(input("Entrez la longueur souhaitée pour votre mot de passe : "))
rep = input("Souhaitez vous des symboles dans votre mot de passe ? (O pour Oui, N pour NoN) : ")
if rep == "O" or rep == "o":
    # Générer un mot de passe aléatoire en utilisant la fonction GeneratePasswordLDP
    password = GeneratePasswordLDP(length)
elif rep == "N" or rep == "n":
    # Générer un mot de passe aléatoire en utilisant la fonction GeneratePasswordLD
    password = GeneratePasswordLD(length)
else:
    print(" ")
    print("ERREUR : Entrez seulement O ou N.")
    rep = input("Souhaitez vous des symboles dans votre mot de passe ? (O pour Oui, N pour NoN) : ")

# Afficher le mot de passe généré à l'utilisateur
print("Votre mot de passe aléatoire est :", password)
print(" ")
rep = input("Souhaitez vous l'enregistrez ? (O pour Oui, N pour NoN) : ")

def Save():
    # Demander à l'utilisateur pour quel site le mot de passe est destiné
    website = input("Pour quel site souhaitez-vous générer ce mot de passe ? ")
    # Créer un fichier texte pour stocker les mots de passe si le fichier n'existe pas déjà
    if not os.path.exists("passwords.txt"):
        open("passwords.txt", "w").close()

    # Ajouter une ligne dans le fichier texte contenant le site et le mot de passe
    with open("passwords.txt", "a") as f:
        f.write(f"{website} : {password}\n")

if rep =="O" or rep=="o":
    Save()
else:
    rep = input("Êtes vous sûr de ne pas vouloir enregistrez ? (O pour Oui, N pour NoN) : ")
    if rep =="O" or rep=="o":
        exit
    else:
        Save()
