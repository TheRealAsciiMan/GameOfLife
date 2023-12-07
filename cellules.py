from random import randint

#i largeur
#j hauteur

class Grille:
    def __init__(self, larg, haut):
        self.largeur = larg
        self.hauteur = haut
        self.matrix = []
        for h in range(haut):
            ligne = []
            for l in range(larg):
                ligne.append(Cellule())
            self.matrix.append(ligne)

    def dans_grille(self, l, h):
        return 0 <= l <= self.largeur and 0 <= h <= self.hauteur

    def setXY(self, l, h, new):
        self.matrix[h][l].actuel = new

    def getXY(self, l, h):
        return self.matrix[h][l]

    def get_largeur(self):
        return self.largeur

    def get_hauteur(self):
        return self.hauteur

    @staticmethod
    def est_voisin(l, h, x, y):
        if (l, h) != (x, y):
            return abs(l - x) <= 1 and abs(h - y) <= 1

    def get_voisins(self, l, h):
        voisins = []  #liste de Cellules
        for x in range(self.largeur):
            for y in range(self.hauteur):
                if self.dans_grille(x, y) and self.est_voisin(l, h, x, y):
                    voisins.append(self.getXY(x, y))
        return voisins

    def affecte_voisins(self):
        for l in range(self.largeur):
            for h in range(self.hauteur):
                self.matrix[h][l].set_voisins(self.get_voisins(l, h))

    def __str__(self):
        ret = ""
        for h in self.matrix:
            ret += "\n"
            for l in h:
                ret += l.__str__()
        return ret

    def remplir_alea(self, taux):
        for l in range(self.largeur):
            for h in range(self.hauteur):
                if randint(1, 100) <= taux:
                    self.matrix[h][l].naitre()
                else:
                    self.matrix[h][l].mourir()

    def jeu(self):
        for l in range(self.largeur):
            for h in range(self.hauteur):
                self.matrix[h][l].calcul_etat_futur()

    def actualise(self):
        for l in range(self.largeur):
            for h in range(self.hauteur):
                self.matrix[h][l].basculer()


class Cellule:
    def __init__(self):
        self.actuel = False
        self.futur = False
        self.voisins = []

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
            return "-"   # Tiret du 6

    def calcul_etat_futur(self):
        if self.est_vivant():
            cellules_vivantes = 0
            for v in self.voisins:
                if v.est_vivant():
                    cellules_vivantes += 1
            if cellules_vivantes == 2 or cellules_vivantes == 3:
                self.naitre()
            else:
                self.mourir()
        else:
            cellules_vivantes = 0
            for v in self.voisins:
                if v.est_vivant():
                    cellules_vivantes += 1
            if cellules_vivantes == 3:
                self.naitre()
            else:
                self.mourir()
