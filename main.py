import random

class Monde:

    def __init__(self, dimension, duree_repousse, carte):
        self.dimension = dimension
        self.duree_repousse = 30
        self.carte = [[random.randint(0,50) for i in range(dimension)] for j in range(dimension)]

    def herbePousse(self):
        for i,j in range(len(self.carte)):
            self.carte[i][j] += 1
    
    def herbeMangee(self, i, j):
        for i,j in range(len(self.carte)):
            if self.carte[i][j] >= 30:
                self.carte[i][j] = 0 
    
    def nbHerbe(self):
        nbHerbe = 0
        for i,j in range(len(self.carte)):
            if self.carte[i][j] >= 30:
                nbHerbe += 1

    def getCoefCarte(self, i, j):
        return self.carte[i][j]

class Mouton:
    def __init__(self, gain_nourriture, position, energie, taux_reproduction, monde):
        self.gain_nourriture = 4
        self.position = (i,j)
        self.energie = random.randint(1, 2*self.gain_nourriture)
        self.taux_reproduction = 4
        self.monde = monde

    def variationEnergie(self):
        if self.monde.carte[self.position[0]][self.position[1]] >= self.monde.duree_repousse:
            self.energie += self.gain_nourriture
            self.monde.herbeMangee(self.position[0], self.position[1])
        else:
            self.energie = self.energie - 1

    def deplacement(self):
        position = list(self.position)
        position[0] = position[0] + random.randint(-1, 1)
        if position[0] < 0:
            position[0] = 50
        elif position[0] > dimension:
            position[0] = 0

        position[1] = position[1] + random.randint(-1, 1)
        if position[1] < 0:
            position[1] = 50
        elif position[1] > dimension:
            position[1] = 0

        self.position = tuple(position)
        return self.position

    def bebe(self, pere):
        x = random.randint(0,100)
        if x <= taux_reproduction:
            bebe = Mouton(4,pere.position, random.randint(1, 2*self.gain_nourriture), 4, pere.monde)

class Simulation:
    def __init__(self, nombre_moutons, horloge, fin_du_monde, moutons, monde):
        self.nombre_moutons = nombre_moutons
        self.horloge = 0
        self.fin_du_monde = 5000
        self.moutons = moutons
        self.monde = monde

    def resultats_herbe(self):
        return self.monde.nbHerbe()

    def resultats_moutons(self):


    def simMouton(self):
        
