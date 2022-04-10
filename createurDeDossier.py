from pathlib import Path

chemin = "C:/Users/envu1/OneDrive/Documents/python"

d = {"Films" : ["Harry Potter",
                "Le Seigneur Des Anneaux",
                "Moon",
                "Forrest Gump"],
    "Employes" : ["Paul",
                    "Pierre",
                    "Marie"],
    "Exercices" : ["les_variables",
                    "les_fichiers",
                    "les_boucles"]}

for mainDir, dir in d.items():
    for f in dir:
        pathDir = Path(chemin) / mainDir / f
        pathDir.mkdir(exist_ok=True, parents=True)