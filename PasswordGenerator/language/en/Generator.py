import random
import string


print(" ")
print(" ")
print(" ")
print("     88--Yb    db    88b 88 8888b.  88--Yb    db    .dP-Y8 .dP-Y8")
print("     88__dP   dPYb   88Yb88  8I  Yb 88__dP   dPYb   `Ybo.- `Ybo.- ")
print("     88-Yb   dP__Yb  88 Y88  8I  dY 88---   dP__Yb  o.`Y8b o.`Y8b ")
print("     88  Yb dP----Yb 88  Y8 8888Y-  88     dP----Yb 8bodP- 8bodP-")
print(" ")
print(" ")
print(" ")




def RandomPS():
    caracteres = string.ascii_letters + string.digits 
    password = ''.join(random.choices(caracteres, k=n)) 
    print("Your password is: ", password)

# Ask the user for the desired password length
n = int(input("Enter the number of characters you want in your password: "))
nb = n

# Ask the user for the desired password type
password_type = input("Enter the desired password type (L for letters, N for numbers, B for both): ")

# If the user chooses a password of letters
if password_type == "L":
    n_letters = n
    n_numbers = 0
    characters = string.ascii_letters

# If the user chooses a password of numbers
elif password_type == "N":
    n_numbers = n
    n_letters = 0
    characters = string.digits

# If the user chooses a password of letters and numbers
elif password_type == "B":
    randomRep = input("Do you want to generate a password with random letters and numbers ? (Y for Yes or N for No)")
    if randomRep == "O":
        RandomPS()
    # Ask the user for the desired number of letters
    n_letters = int(input("Enter the number of letters you want in your password: "))
    
    while n_letters > n or n_letters < 0:
        print("ERROR the number of letters cannot be greater than the chosen password length.")
        response = input("Do you want to change the number of characters in your password? (Y for Yes or N for No)")
        if response == "Y":
            n = int(input("Enter the number of characters you want in your password: "))
        else:
            n_letters = int(input("Enter the number of letters you want in your password: "))
            
    # Ask the user for the desired number of numbers
    nb = nb - n_letters
    n_numbers = int(input("Enter the number of numbers you want in your password: "))
    
    while n_numbers > n or n_numbers > nb or n_numbers < 0:
        print("ERROR the number of letters and numbers cannot be greater than the chosen password length.")
        response = input("Do you want to change the number of characters in your password? (Y for Yes or N for No)")
        if response == "Y":
            n = int(input("Enter the number of characters you want in your password: "))
        else:
            n_numbers = int(input("Enter the number of numbers you want in your password: "))
    
    characters = string.ascii_letters + string.digits

else:
    print("Invalid password type. Please enter L for letters, N for numbers, or B for both.")

# Generate the password
password = ''.join(random.choices(characters, k=n_letters + n_numbers))

# Insert the letters
random_letters = random.choices(string.ascii_letters, k=n_letters)
for i in range(n_letters):
    index = random.randint(0, n - 1)
    password = password[:index] + random_letters[i] + password[index+1:]

# Insert the numbers
random_numbers = random.choices(string.digits, k=n_numbers)
for i in range(n_numbers):
    index = random.randint(0, n - 1)
    password = password[:index] + random_numbers[i] + password[index+1:]

# Display the password
print("Your password is: ", password)

