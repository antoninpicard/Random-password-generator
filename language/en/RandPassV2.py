import random
import string
import os.path

from pystyle import Colors, Colorate
print(Colorate.Horizontal(Colors.yellow_to_red,"""
 ____________________________________________________________________________________________________________________
|                                                                                                                    |
|           ▄████████    ▄████████ ███▄▄▄▄   ████████▄     ▄███████▄    ▄████████    ▄████████    ▄████████          |
|          ███    ███   ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███   ███    ███   ███    ███          |
|          ███    ███   ███    ███ ███   ███ ███    ███   ███    ███   ███    ███   ███    █▀    ███    █▀           |
|         ▄███▄▄▄▄██▀   ███    ███ ███   ███ ███    ███   ███    ███   ███    ███   ███          ███                 |
|        ▀▀███▀▀▀▀▀   ▀███████████ ███   ███ ███    ███ ▀█████████▀  ▀███████████ ▀███████████ ▀███████████          |
|        ▀███████████   ███    ███ ███   ███ ███    ███   ███          ███    ███          ███          ███          |
|          ███    ███   ███    ███ ███   ███ ███   ▄███   ███          ███    ███    ▄█    ███    ▄█    ███          |
|          ███    ███   ███    █▀   ▀█   █▀  ████████▀   ▄████▀        ███    █▀   ▄████████▀   ▄████████▀           |
|          ███    ███                                                                                                |
|____________________________________________________________________________________________________________________|
 
""",1))


def generate_password_with_symbols(length):
    # Concatenate strings containing the desired characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use the random.choices function to select a random character from the "characters" string
    # Repeat this operation "length" times to obtain a password of length "length"
    password = ''.join(random.choices(characters, k=length))

    return password

def generate_password_without_symbols(length):
    # Concatenate strings containing the desired characters for the password
    characters = string.ascii_letters + string.digits

    # Use the random.choices function to select a random character from the "characters" string
    # Repeat this operation "length" times to obtain a password of length "length"
    password = ''.join(random.choices(characters, k=length))

    return password

# Ask the user for the desired length of the password
length = int(input("Enter the desired length for your password: "))
response = input("Do you want symbols in your password? (Y for Yes, N for No): ")
if response.lower() == "y":
    # Generate a random password using the generate_password_with_symbols function
    password = generate_password_with_symbols(length)
elif response.lower() == "n":
    # Generate a random password using the generate_password_without_symbols function
    password = generate_password_without_symbols(length)
else:
    print(" ")
    print("ERROR: Enter only Y or N.")
    response = input("Do you want symbols in your password? (Y for Yes, N for No): ")

# Display the generated password to the user
print("Your random password is:", password)
print(" ")
response = input("Do you want to save it? (Y for Yes, N for No): ")

def save_password():
    # Ask the user for which website the password is intended
    website = input("For which website do you want to generate this password? ")
    # Create a text file to store passwords if the file does not already exist
    if not os.path.exists("passwords.txt"):
        open("passwords.txt", "w").close()

    # Add a line in the text file containing the website and the password
    with open("passwords.txt", "a") as f:
        f.write(f"{website} : {password}\n")

if response.lower() == "y":
    save_password()
else:
    response = input("Are you sure you don't want to save it? (Y for Yes, N for No): ")
    if response.lower() == "y":
        exit
    else:
        save_password()
