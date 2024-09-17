from random import *

class Monde:
    def __init__(self, dimension, duree_repousse):
        '''intialise la carte du monde en fonction de la dimension et de la duree de repousse données par les utilisateurs'''
        assert dimension >= 10, "la dimension de la carte doit être supérieur ou égal à 50"
        assert duree_repousse > 0 and duree_repousse <= 100, "la duree de repousse de l'herbe doit être comprise entre 1 et 100"
        self.dimension = dimension
        self.duree_repousse = duree_repousse
        self.carte = [[0 for j in range(dimension)] for i in range(dimension)]
        nombreCarresHerbus = (dimension * dimension) // 2
        while nombreCarresHerbus > 0 :
            i = randrange(dimension)
            j = randrange(dimension)
            if self.carte[i][j] == 0 :
                self.carte[i][j] = self.duree_repousse
                nombreCarresHerbus -= 1
        for i in range (dimension):
            for j in range(dimension):
                if self.carte[i][j] == 0 :
                    self.carte[i][j] = randrange(duree_repousse - 1)

    def herbePousse(self) :
        '''fait repousser l'herbe d'une unité'''
        for i in range (self.dimension):
            for j in range(self.dimension):
                self.carte[i][j] += 1

    def herbeMangee(self, i,j):
        '''reinitialise le coefficient de la matrice à 0 lorsqu'un mouton occupe la case'''
        self.carte[i][j] = 0

    def nbHerbe(self):
        '''compte le nombre de cases contenant de l'herbe'''
        nb = 0
        for i in range (self.dimension):
            for j in range(self.dimension):
                if self.carte[i][j] >=  self.duree_repousse :
                    nb += 1
        return nb

    def getCoefCarte(self, i,j):
        return self.carte[i][j]

    def getDimension(self):
        return self.dimension

    def getCarte(self):
        return self.carte

    def getDuree_repousse(self):
        return self.duree_repousse


'''monde1 = Monde(10,30)
print(monde1.getCarte())
Monde1.herbePousse()
print(monde1.getCarte())
print(monde1.nbHerbe())
Monde1.herbeMangee(0,0)
print(monde1.getCarte())
print(monde1.nbHerbe())'''

class Mouton :
    def __init__(self, gain_nourriture, taux_reproduction, monde):
        ''' initialisation de l'objet Mouton'''
        assert gain_nourriture > 0, "le mouton doit pouvoir reprendre des forces"
        assert taux_reproduction > 1 and taux_reproduction < 100, "le taux de reproduction est compris entre 1 et 100"
        self.gain_nourriture = gain_nourriture
        self.position = [randrange(0, monde.getDimension()), randrange(0, monde.getDimension())]
        self.energie = randrange(1,2) * gain_nourriture
        self.taux_reproduction = taux_reproduction
        self.monde = monde

    def variationEnergie(self):
        ''' diminue l'energie du mouton si il ne se trouve pas sur une case herbeuse, l'augmente sinon'''
        if self.monde.carte[self.position[0]][self.position[1]] >= self.monde.duree_repousse :
            self.energie += self.gain_nourriture
            self.monde.herbeMangee(self.position[0], self.position[1])
        else :
            self.energie -= 1


    def deplacement(self):
        '''déplace le mouton'''
        deplacement = randrange(1,9)
        i = self.position[0]
        j = self.position[1]
        print(deplacement)
        if deplacement == 1 :
            i = self.position[0] - 1
            j = self.position[1] - 1
        elif deplacement == 2 :
            i = self.position[0] - 1
        elif deplacement == 3 :
            i = self.position[0] + 1
            j = self.position[1] + 1
        elif deplacement == 4 :
            j = self.position[1] - 1
        elif deplacement == 5 :
            j = self.position[1] + 1
        elif deplacement == 6 :
            i = self.position[0] - 1
            j = self.position[1] + 1
        elif deplacement == 7 :
            j = self.position[1] + 1
        elif deplacement == 8 :
            i = self.position[0] + 1
            j = self.position[1] + 1

        if i < 0 :
            i = self.monde.dimension - 1
        if j < 0 :
            j = self.monde.dimension - 1
        if i == self.monde.dimension :
            i = 0
        if j == self.monde.dimension :
            j = 0
        self.position[0] = i
        self.position[1] = j

    def getStats(self):
        return [self.energie, self.taux_reproduction, self.position]

    def setPosition(self, i, j):
                self.position =  [i,j]

'''monde1 = Monde(10,30)
mouton1 = Mouton(4, 4, monde1)
print(mouton1.getStats())
print(monde1.getCoefCarte(mouton1.position[0],mouton1.position[1] ))
mouton1.variationEnergie()
print(mouton1.getStats())
mouton1.deplacement()
print(mouton1.getStats())
mouton1.deplacement()
print(mouton1.getStats())
mouton1.deplacement()
print(mouton1.getStats())'''

class Simulation:
    '''gère la simulation'''
    def __init__(self, nombre_moutons, fin_du_monde, monde, max_moutons):
        assert nombre_moutons >= 0 and isinstance(nombre_moutons, int), "le nombre de moutons doit être un entier positif ou nul"
        self.nombre_moutons = nombre_moutons
        self.horloge = 0
        self.fin_du_monde = fin_du_monde
        self.moutons = [Mouton(4,50, monde) for x in range(nombre_moutons)]
        self.monde = monde
        self.resultats_herbe = []
        self.resultats_herbe.append(monde.nbHerbe())
        self.resultats_moutons = []
        self.resultats_moutons.append(nombre_moutons)
        self.max_moutons = max_moutons

    def simMouton(self):
        ''' création de la boucle qui fait fonctionner notre écosystème'''
        while self.horloge <= self.fin_du_monde :
            self.horloge += 1
            self.monde.herbePousse()
            for mouton in self.moutons :
                mouton.variationEnergie()
                if mouton.energie <= 0 :
                    self.moutons.remove(mouton)
                elif random()*100 <= mouton.taux_reproduction :
                    bebe_mouton = Mouton(4,50, self.monde)
                    bebe_mouton.setPosition(mouton.position[0], mouton.position[1])
                    self.moutons.append(bebe_mouton)
                    mouton.deplacement()
            self.resultats_herbe.append(self.monde.nbHerbe())
            self.resultats_moutons.append(len(self.moutons))
            if len(self.moutons) <= 0 or len(self.moutons) >= self.max_moutons :
                return self.resultats_herbe, self.resultats_moutons
            print(self.monde.getCarte())
            print(self.resultats_herbe)
            print(self.resultats_moutons)
            print(self.horloge)
        return self.resultats_herbe, self.resultats_moutons


'''sim = Simulation(3,10,Monde(10,30), 10)
print(sim.nombre_moutons)
print(sim.horloge)
print(sim.fin_du_monde)
for mouton in sim.moutons :
    print(mouton.getStats())
print(sim.resultats_herbe)
print(sim.resultats_moutons)
print(sim.monde.getCarte())
print(sim.simMouton())'''
