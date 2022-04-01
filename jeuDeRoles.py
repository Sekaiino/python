from random import randint

choice = "Souhaitez-vous attaquer(1) ou utiliser une potion(2) ?   "
potion = 3
userLife = 50
ennemyLife = 50
passTour = False

while True:

    if passTour == False:
        userChoice = input(choice)

        if not userChoice.isdigit():
            print("Veuillez entrez un choix valide...")
            continue

        userChoice = int(userChoice)
        if userChoice > 2 or userChoice < 1:
            print("Veuillez entrez un choix valide...")
            continue

        elif userChoice == 1:
            userAttack = randint(5, 10)
            ennemyLife -= userAttack
            print(f"Vous infligez {userAttack} points de dégâts à l'ennemi ⚔️")
            
            if ennemyLife <= 0:
                print("Tu as gagné 💪")
                break

        elif userChoice == 2 and potion > 0:
            potion -= 1
            userPotion = randint(15, 50)
            userLife += userPotion
            passTour = 1
            print(f"Vous récupérez {userPotion} points de vie ❤️ ({potion} 🧪 restantes)")
        
        elif potion <= 0:
            print("Vous n'avez plus de potions...")
            continue

    elif passTour == True:
        print("Vous passez votre tour...")
        passTour = False
        pass

    ennemyAttack = randint(5, 15)
    userLife -= ennemyAttack
    print(f"L'ennemi vous a infligé {ennemyAttack} points de dégâts ⚔️")
    if userLife <= 0:
        print("Tu as perdu 😔")
        break

    print(f"Il vous reste {userLife} points de vie.")
    print(f"Il reste {ennemyLife} points de vie à l'ennemi.")
    print("""
--------------------------------------------------------------------------------------------------
    """)

print("Fin du jeu.")