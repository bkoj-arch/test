class Humain():
    sexe=["H","F"]
    nom=["Estinien","Alisae","Alphinaud","Urianger","Minfillia", "Thancred", "Lyse"]
    def __init__(self,nom):   #Constructeur par defaut -> sois-même
        self.age=0
        self.nom=random.choice(Humain.nom)
        self.sexe=random.choice(Humain.sexe)
        self.before.birth=0
    def vieillir(self):
        self.age+=1
    def mourir(self):
        nb=random.randint(0,200)
        if nb<self.age:
            return True
        return False
    def reproduire(self,h2):
        if self.sexe != h2.sexe:
            if self.age 16 and h2.age > 16:
                self.before_birth == 0 and h2.before_birth == 0:
                
                    return Humain()
#créer des instances (objets)
