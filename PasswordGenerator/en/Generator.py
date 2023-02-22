import random
import string

def RandomPS():
    caracteres = string.ascii_letters + string.digits 
    password = ''.join(random.choices(caracteres, k=n)) 
    print("Votre mot de passe est : ", password)

# Demander à l'utilisateur la longueur souhaitée du mot de passe
n = int(input("Entrez le nombre de caractères que vous souhaitez dans votre mot de passe : "))
nb = n

# Demander à l'utilisateur le type de mot de passe souhaité
password_type = input("Entrez le type de mot de passe souhaité (L pour les lettres, N pour les chiffres, B pour les deux) : ")

# Si l'utilisateur choisit un mot de passe de lettres
if password_type == "L":
    n_letters = n
    n_numbers = 0
    characters = string.ascii_letters

# Si l'utilisateur choisit un mot de passe de chiffres
elif password_type == "N":
    n_numbers = n
    n_letters = 0
    characters = string.digits

# Si l'utilisateur choisit un mot de passe de lettres et de chiffres
elif password_type == "B":
    randomRep = input("Voulez-vous générer un mot de passe avec des lettres et des chiffres aléatoires ? (O pour Oui ou N pour Non)")
    if randomRep == "O":
        RandomPS()
    # Demander à l'utilisateur le nombre de lettres souhaité
    n_letters = int(input("Entrez le nombre de lettres que vous souhaitez dans votre mot de passe : "))
    
    while n_letters > n or n_letters < 0:
        print("ERREUR le nombre de lettres ne peut pas être supérieur à la longueur de mot de passe choisie.")
        response = input("Voulez-vous changer le nombre de caractères de votre mot de passe ? (O pour Oui ou N pour Non)")
        if response == "O":
            n = int(input("Entrez le nombre de caractères que vous souhaitez dans votre mot de passe : "))
        else:
            n_letters = int(input("Entrez le nombre de lettres que vous souhaitez dans votre mot de passe : "))
            
    # Demander à l'utilisateur le nombre de chiffres souhaité
    nb = nb - n_letters
    n_numbers = int(input("Entrez le nombre de chiffres que vous souhaitez dans votre mot de passe : "))
    
    while n_numbers > n or n_numbers > nb or n_numbers < 0:
        print("ERREUR le nombre de lettres et de chiffres ne peut pas être supérieur à la longueur de mot de passe choisie.")
        response = input("Voulez-vous changer le nombre de caractères de votre mot de passe ? (O pour Oui ou N pour Non)")
        if response == "O":
            n = int(input("Entrez le nombre de caractères que vous souhaitez dans votre mot de passe : "))
        else:
            n_numbers = int(input("Entrez le nombre de chiffres que vous souhaitez dans votre mot de passe : "))
    
    characters = string.ascii_letters + string.digits

else:
    print("Type de mot de passe invalide. Veuillez entrer L pour les lettres, N pour les chiffres ou B pour les deux.")

# Générer le mot de passe
password = ''.join(random.choices(characters, k=n_letters + n_numbers))
# Insérer les lettres
random_letters = random.choices(string.ascii_letters, k=n_letters)
for i in range(n_letters):
    index = random.randint(0, n - 1)
    password = password[:index] + random_letters[i] + password[index+1:]

# Insérer les nombres
random_numbers = random.choices(string.digits, k=n_numbers)
for i in range(n_numbers):
    index = random.randint(0, n - 1)
    password = password[:index] + random_numbers[i] + password[index+1:]

# Afficher le mot de passe
print("Votre mot de passe est : ", password)
