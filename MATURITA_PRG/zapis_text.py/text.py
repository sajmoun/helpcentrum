# Otevření souboru pro zápis (vytvoří soubor, pokud neexistuje)
with open("text.txt", "w") as file:
    # Zápis několika řádků do souboru
    file.write("Ahoj, toto je první řádek.\n")
    file.write("Druhý řádek je tady.\n")
    file.write("Třetí řádek má něco o Pythonu.\n")

# Otevření souboru pro čtení
with open("text.txt", "r") as file:
    # Čtení všech řádků souboru
    content = file.read()
    print(content)

# Bonus: Hledání slova 'Python' ve souboru
if "Python" in content:
    print("Slovo Python bylo nalezeno.")
else:
    print("Slovo Python nebylo nalezeno.")




### NEBO ###
# # Otevření souboru pro zápis a čtení současně
# with open("text.txt", "w+") as file:
#     file.write("Ahoj, toto je první řádek.\n")
#     file.write("Druhý řádek je tady.\n")
#     file.write("Třetí řádek má něco o Pythonu.\n")

#     # Přejděte zpět na začátek souboru pro čtení
#     file.seek(0)  # Nastaví kurzor na začátek souboru

#     # Přečteme obsah souboru
#     content = file.read()
#     print(content)

#     # Hledáme slovo 'Python'
#     print("Slovo Python bylo nalezeno." if "Python" in content else "Slovo Python nebylo nalezeno.")
