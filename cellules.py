from random import randint

class Grille:
    largeur = None
    hauteur = None
    matrix = [[]]
    def __init__(self, larg, haut):
        self.largeur = larg
        self.hauteur = haut
        self.matrix = []
        for i in range(haut):
            ligne = []
            for j in range(larg):
                ligne.append(Cellule())
            self.matrix.append(ligne)

    def dans_grille(self, i, j):
        return 0 <= i <= self.largeur and 0 <= j <= self.hauteur
    def setXY(self, i, j, new):
        self.matrix[j][i].actuel = new
    def getXY(self, i, j):
        return self.matrix[j][i]

    def get_largeur(self):
        return self.largeur

    def get_hauteur(self):
        return self.hauteur

    def est_voisin(self, i, j, x, y):
        return abs(i - x) <= 1 and abs(j - y) <= 1

    def get_voisins(self, i, j):
        voisins = []
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if (x, y) != (i, j) and self.dans_grille((x, y)):
                    voisins.append(self.getXY(x, y))
        return voisins

    def affecte_voisins(self):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrix[j][i].set_voisins(self.get_voisins(i, j))

    def __str__(self):
        ret = ""
        for i in self.matrix:
            ret += "\n"
            for j in self.matrix:
                ret += str(j)
        return ret

    def remplir_alea(self, taux):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                if randint(1, 100) <= taux:
                    self.matrix[j][i].actuel = True
                else:
                    self.matrix[j][i].actuel = False

    def jeu(self):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrix[j][i].calcul_etat_futur()

    def actualise(self):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrix[j][i].basculer()

class Cellule:
    actuel = False
    futur = False
    voisins = []
    def __init__(self):
        self.actuel = False
        self.futur = False
        self.voisins = None
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
        if self.est_vivant():
            return "X"
        else:
            return "-" # Tiret du 6

    def calcul_etat_futur(self):
        if self.voisins is not None:
            if self.actuel:
                if len(self.voisins) < 2 or len(self.voisins) > 3:
                    self.futur = False
                else:
                    self.futur = True
            else:
                if len(self.voisins) == 3:
                    self.futur == True
                else:
                    self.futur == False


