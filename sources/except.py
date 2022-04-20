chemin = input("Entrez le fichier à ouvrir : ")

try:
    with open(chemin,"r") as f:
        contenu = f.read()
        print(contenu)
except UnicodeDecodeError as i:
    print("Error = ", i)
except FileNotFoundError as i:
    print("Error = ", i)