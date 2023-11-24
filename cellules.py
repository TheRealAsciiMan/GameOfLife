from random import *

class Grille:
    largeur = None
    hauteur = None
    matrix = [[]]
    def __init__(self, larg, haut):
        self.largeur = larg
        self.hauteur = haut

    def dans_grille(self, pixel):
        if self.matrix[pixel[0][pixel[1]]] in self.matrix:
            return True
        else:
            return False
    def setXY(self, boole, pixel):
        self.matrix[pixel[0][pixel[1]]] = boole
    def getXY(self, pixel):
        return self.matrix[pixel[0][pixel[1]]]

    def get_largeur(self):
        return self.largeur

    def get_hauteur(self):
        return self.hauteur

    def est_voisin(self, pixel1, pixel2):
        if abs(pixel1[0]-pixel2[0]) < 1 and abs(pixel1[1]-pixel2[1]):
            return True
        else:
            return False

    def get_voisins(self, pixel):
        return self.matrix[pixel[0][pixel[1]]].get_voisins

    def affecte_voisins(self):
        for i in self.matrix:
            for j in self.matrix:
                self.matrix[i[j]].set_voisins(self.get_voisins((i, j)))

    def __str__(self):
        ret = ""
        for i in self.matrix:
            ret += "\n"
            for j in self.matrix:
                ret += self.matrix[i[j]].__str__()
        return ret

    def remplir_alea(self, taux):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                if randint
                self.matrix[j[i]] ==  Cellule

                self.matrix[j[i]].naitre


        return True










class Cellule:
    actuel = False
    futur = False
    voisins = []

    def est_vivant(self):
        return self.actuel

    def set_voisins(self, voisins):
        self.voisins = voisins

    def get_voisins(self):
        return self.voisins

    def naitre(self):
        self.futur = True

    def mourir(self):
        self.futur = False

    def basculer(self):
        self.actuel = self.futur
    def __str__(self):
        """
        Permet d'afficher la cellule dans la console ou dans un appel print

        :return: "X" (str) ou "-" (str)
        """
        if self.est_vivant()==True:
            return "X"
        elif self.est_vivant()==False:
            return "-" # Tiret du 6

    def calcul_etat_futur(self):
        if self.actuel == True:
            if len(self.voisins) <= 2:
                self.futur = False
            elif 2 < len(self.voisins) < 4:
                self.futur = True
            elif len(self.voisins) > 4:
                self.futur = False
        elif self.actuel == False:
            if len(self.voisins) == 3:
                self.futur == True
            else:
                self.futur == False


