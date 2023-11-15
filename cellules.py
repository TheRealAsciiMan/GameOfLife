

class Grille:
    largeur = None
    hauteur = None
    matrix = [[]]
    def __int__(self, larg, haut):
        self.largeur = larg
        self.hauteur = haut

    def dans_grille(self):
        for i in self.matrix:
            for j in self.matrix:






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


