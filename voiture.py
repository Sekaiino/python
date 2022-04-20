class Voiture:

    def __init__(self):
        essence = 100

    def afficher_reservoir(self):
        print(f"Il vous reste {self.essence}L d'essence.")

    def roule(self, km):
        self.essence -= (km * 5) / 100

        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faite le plein !")
        
        elif self.essence <= 10 and self.essence > 0:
            print("Vous n'avez bientôt plus d'essence !")
        
        self.afficher_reservoir()

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")
