from random import randint

n = randint(1, 100)
essais = 5
print("*** Le jeu du nombre mystère ***")
while essais > 0:
    print(f"Il te reste {essais} essai{'s' if essais > 1 else ''}")
    nbr = input("Devine le nombre : ")

    if not nbr.isdigit():
        print("Veuillez entrez un nombre valide.")
        continue

    nbr = int(nbr)
    
    if nbr > 100 or nbr < 1:
        print("Veuillez entrez un nombre valide.")
        continue

    elif nbr > n:
        print(f"Le nombre mystère est plus petit que {nbr}")

    elif nbr < n:
        print(f"Le nombre mystère est plus grand que {nbr}")

    else:
        break

    essais -= 1

if nbr == n:
    print(f"""Bravo ! Vous avez trouvé le nombre mystère,
c'était bien {n}. Tu as trouvé le nombre en { 6 - essais } essais.""")

elif essais == 0:
    print(f"""Dommage ! Vous n'avez pas trouvé le nombre mystère,
c'était {n}""")

print("Fin du jeu.")