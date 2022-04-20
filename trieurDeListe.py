from pathlib import Path

chemin = "C:/Users/envu1/OneDrive/Documents/python/prenoms.txt"

with open (chemin, "r") as f:
    contenu = f.read().splitlines()

prenoms = []
for f in contenu:
    prenoms.extend(f.split())

prenomsClean = [prenom.strip(" ,.") for prenom in prenoms]

with open(chemin, "w") as f:
    f.write("\n".join(sorted(prenomsClean)))