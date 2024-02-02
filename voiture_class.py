class Voiture:
    
    fonction = "Ce sont des engins de deplacement"
    
    def __init__(self,marque, modele, prix, vitesse):
        
        self.marque = marque
        self.modele = modele
        self.prix = prix
        self.vitesse = vitesse 
        
    def __repr__(self):
        return f"{__class__.__name__} {self.marque} {self.modele} {self.prix} {self.vitesse}"
       
    @classmethod  
    def fonc(cls):
         return cls.fonction
     
    #pdb.set_trace()
     
    def __getattr__(self, nom):
        return f"La marque du véhicule est {nom}"
        
    def getPrice(self, min, max):
        
        if self.prix < min:
            print("la voiture est moins chère")
        elif self.prix >  max:
            print("la voiture est couteuse")
        else:
            print("le prix me va ")
           
class Moto(Voiture): 
    
    def __init__(self,marque, modele, prix, vitesse, moteur):
        super().__init__(marque,modele,prix,vitesse)
        # attributs de Moto
        self.moteur = moteur
    
    def __str__(self):
        return f"vous avez un moteur robuste {self.moteur}"

class Moto4Roues(Moto):  # comme Moto hérite de Voiture,pas besoin d'hériter de Voiture
    
    def __init__(self, marque, modele, prix, vitesse, couleur, date, moteur):
        # super va redistribuer les paramètres vers les classes Moto et Voiture
        super().__init__(marque, modele, prix, vitesse, moteur)
        #Moto.__init__(moteur)
        
        # attributs de Moto4Roues
        self.couleur = couleur.lower()  # pour comparer mettre en minuscule
        self.date = date
        
    def getCouleur(self):
        # ce test doit être mis avant le test du différent de 'blanc' qui contient un return
        if self.couleur == 'bleu':
            print("j'aime cette couleur")
            
        if self.couleur != 'blanc':
            # instruction return doit être mise en fin de méthode
            # il faut un print pour afficher la valeur de retour
            return f"la couleur {self.couleur} ne tiendra pas"
        

# moto4roues = Moto4Roues("Ferrai","Citron", 24909, 56900,  "Bleu", 2005, "pluton")

class Velo(Moto4Roues,Moto):
    
    def __init__(self,marque, modele,prix,vitesse,moteur,couleur,date_creation,rayon,alarme):
        
        Voiture.__init__(self,marque,modele,prix,vitesse)
        #Moto.__init__(self,moteur)
        #Moto4Roues.__init__(self,couleur, date_creaction)
        
        # attributs de Velo
        self.rayon = rayon
        self.alarme = alarme
    	
    def get_alarme(self):
        if self.alarme=='oui':
            return "pipipi"
        # si alarme='non'
        return 'no alarm'

         
voiture1 = Voiture("Ferrai","Citron", 2400098,350)
print(voiture1)
print(voiture1.marque)
voiture2 = Voiture.fonc()

print(voiture2)
voiture1.getPrice(2008,30048)

moto1 = Moto("Ferrari", "Citron", 24909, 56900, "pluton")
print(moto1)

moto4roues = moto4roues = Moto4Roues("Ferrai","Citron", 24909, 56900,  "Bleu", 2005, "pluton")

print(moto4roues)
# print pour afficher la valeur de retour
print(moto4roues.getCouleur())

# paramètres Velo : marque, modele,prix,vitesse,moteur,couleur,date_creaction,rayon,alarme)
velo1 = Velo("Dupont", "Sport", 1200, 50,'moteur',"rouge",2024,50,'oui')
velo2 = Velo("Dupont", "Sport", 1200, 50,'moteur',"rouge",2024,50,'non')

print(f"velo1: {velo1.get_alarme()}")
print(f"velo2: {velo2.get_alarme()}")