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
            self.carte[i][j] = 0 if self.carte[i][j] >= 30
    
    def nbHerbe(self, nbHerbe):
        nbHerbe = 0
        for i,j in range(len(self.carte)):
            if self.carte[i][j] >= 30:
                nbHerbe += 1

    def getCoefCarte(self, i, j):
        return self.carte[i][j]

class Mouton:
    def __init__(self, gain_nourriture, position, energie, taux_reproduction, monde)
    self.gain_nourriture = 4
    self.position = (i,j)
    self.energie = random.randint(1, 2*self.gain_nourriture)
    self.taux_reproduction = 4
    self.monde = monde

    def variationEnergie(self):
        if self.monde.carte[self.position[0]][self.position[1]] >= self.monde.duree_repousse:
            self.energie += self.gain_nourriture
            self.monde.carte[self.position[0]][self.position[1]] = 0
        else:
            self.energie = self.energie - 1

    def deplacement(self):
        self.position[0] = self.position[0] + random.randint(-8, 8)
        if self.position[0] <0:
            self.position[0] = self.position - 
