import json
import os


CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "liste.json")

MENU = """Choisissez parmi les options suivantes : 
    1 : Ajoutez un element a la liste
    2 : Retirer un element de la liste
    3 : Afficher la liste
    4 : Vider la liste
    5 : Quitter
    ? Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f:
        LISTE = json.load(f)

else:
    LISTE = []

while True:

    i = input(MENU)
    
    if i not in MENU_CHOICES:
        print("Veuillez choisir une option valide... ")
        continue

    if i == "1":
        item = input("Entrez le nom de l'element a ajouter a la liste : ")
        LISTE.append(item)
        print(f"L'element {item} a bien ete ajouter a la liste. ")

    elif i == "2":
        item = input("Entrez le nom de l'element a retirer de la liste : ")

        if LISTE:
            if item in LISTE:
                LISTE.remove(item)
                print(f"L'element {item} a bien ete retirer a la liste. ")

            else:
                print("Veuillez entrez un element valide. ")
        else:
            print("Votre liste ne contient aucun element. ")        

    elif i == "3":

        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        
            else:
                print("Votre liste ne contient aucun élément. ")

    elif i == "4":
        LISTE.clear()
        print("Votre liste a ete videe. ")

    elif i == "5":
        with open(LISTE_PATH, "w") as f:
            json.dump(LISTE, f, indent=4)
        break

print("A bientot ! ")