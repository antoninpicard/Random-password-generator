import random
import string
import os.path
import tkinter as tk
import pyperclip
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

def GeneratePasswordLDP(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password


def GeneratePasswordLD(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password


def save_password(website, password):
    if not os.path.exists("passwords.txt"):
        open("passwords.txt", "w").close()

    with open("passwords.txt", "a") as f:
        f.write(f"{website} : {password}\n")


class PasswordGeneratorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Générateur de mot de passe")
        self.window.geometry("400x350")

        self.length_label = tk.Label(self.window, text="Longueur du mot de passe :")
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self.window)
        self.length_entry.pack()

        self.symbols_var = tk.BooleanVar(value=True)
        self.symbols_checkbox = tk.Checkbutton(self.window, text="Inclure des symboles", variable=self.symbols_var)
        self.symbols_checkbox.pack(pady=10)

        self.generate_button = tk.Button(self.window, text="Générer un mot de passe", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self.window, text="")
        self.password_label.pack(pady=10)

        self.copy_button = tk.Button(self.window, text="Copier", command=self.copy_password)
        self.copy_button.pack(pady=10)

        self.website_label = tk.Label(self.window, text="Site web :")
        self.website_entry = tk.Entry(self.window)

        self.save_button = tk.Button(self.window, text="Enregistrer le mot de passe", command=self.save_password)

        self.window.mainloop()

    def generate_password(self):
        length = int(self.length_entry.get())
        use_symbols = self.symbols_var.get()

        if use_symbols:
            password = GeneratePasswordLDP(length)
        else:
            password = GeneratePasswordLD(length)

        self.password_label.config(text=f"Mot de passe généré : {password}")
        self.copy_button.pack(pady=10)

        self.website_label.pack(pady=10)
        self.website_entry.pack()

        self.save_button.pack(pady=10)

    def copy_password(self):
        password = self.password_label.cget("text").split(": ")[1]
        pyperclip.copy(password)

    def save_password(self):
        website = self.website_entry.get()
        password = self.password_label.cget("text").split(": ")[1]
        save_password(website, password)
        self.website_entry.delete(0, tk.END)
        self.password_label.config(text="")
        self.copy_button.pack_forget()
        self.website_label.pack_forget()
        self.website_entry.pack_forget()
        self.save_button.pack_forget()


if __name__ == "__main__":
    app = PasswordGeneratorApp()

