from random import randint


class Grille:
    """
    Représente une grille pour le Jeu de la Vie.

    Attributs:
        largeur (int): La largeur de la grille.
        hauteur (int): La hauteur de la grille.
        matrix (list[list[Cellule]]): Une matrice de cellules représentant l'état actuel de la grille.

    Méthodes:
        __init__(self, larg: int, haut: int)
        dans_grille(self, l: int, h: int) -> bool
        setXY(self, l: int, h: int, new: bool)
        getXY(self, l: int, h: int) -> Cellule
        get_largeur(self) -> int
        get_hauteur(self) -> int
        est_voisin(l: int, h: int, x: int, y: int) -> bool
        get_voisins(self, l: int, h: int) -> list[Cellule]
        affecte_voisins(self)
        __str__(self) -> str
        remplir_alea(self, taux: int)
        jeu(self)
        actualise(self)
    """
    def __init__(self, larg:int, haut:int):
        """
        Initialise une grille de jeu.

        Crée une grille de jeu avec une largeur et une hauteur données et remplit la grille de cellules mortes.

        Paramètres:
            larg (int): La largeur de la grille.
            haut (int): La hauteur de la grille.
        """
        self.largeur = larg
        self.hauteur = haut
        self.matrix = []
        for h in range(haut):
            ligne = []
            for l in range(larg):
                ligne.append(Cellule())
            self.matrix.append(ligne)

    def dans_grille(self, l:int, h:int) -> bool:
        """
        Vérifie si les coordonnées (l, h) sont à l'intérieur de la grille.

        Vérifie si les coordonnées sont valides dans la grille grâce à la largeur et la hauteur.

        Paramètres:
            l (int): Coordonnée en largeur.
            h (int): Coordonnée en hauteur.

        Retour:
            bool: True si les coordonnées sont à l'intérieur de la grille, sinon False.
        """
        return 0 <= l <= self.largeur and 0 <= h <= self.hauteur

    def setXY(self, l:int, h:int, new:bool):
        """
        Modifie l'état d'une cellule aux coordonnées (l, h).

        Modifie l'état d'une cellule aux coordonnées spécifiées.

        Paramètres:
            l (int): Coordonnée en largeur.
            h (int): Coordonnée en hauteur.
            new (bool): Nouvel état de la cellule.
        """
        self.matrix[h][l].actuel = new

    def getXY(self, l:int, h:int):
        """
        Récupère la cellule aux coordonnées (l, h).

        Récupère la cellule spécifiée par ses coordonnées dans la matrix.

        Paramètres:
            l (int): Coordonnée en largeur.
            h (int): Coordonnée en hauteur.

        Retour:
            Cellule: La cellule aux coordonnées spécifiées.
        """
        return self.matrix[h][l]

    def get_largeur(self) -> int:
        """
        Récupère la largeur de la grille.

        Récupère la largeur actuelle de la grille avec l'attribut largeur.

        Retour:
            int: La largeur de la grille.
        """
        return self.largeur

    def get_hauteur(self) -> int:
        """
        Récupère la hauteur de la grille.

        Récupère la hauteur actuelle de la grille avec l'attribut hauteur.

        Retour:
            int: La hauteur de la grille.
        """
        return self.hauteur

    @staticmethod
    def est_voisin(l:int, h:int, x:int, y:int) -> bool:
        """
        Méthode Statique

        Vérifie si les coordonnées (x, y) sont des voisins de la cellule aux coordonnées (l, h).

        Vérifie si les coordonnées spécifiées sont des voisins de la cellule en calculant la distance qui les sépare.

        Paramètres:
            l (int): Coordonnée en largeur.
            h (int): Coordonnée en hauteur.
            x (int): Coordonnée x du voisin potentiel.
            y (int): Coordonnée y du voisin potentiel.

        Retour:
            bool: True si les coordonnées sont des voisins, sinon False.
        """
        if (l, h) != (x, y):
            return abs(l - x) <= 1 and abs(h - y) <= 1

    def get_voisins(self, l:int, h:int) -> list:
        """
        Récupère la liste des cellules voisines de la cellule aux coordonnées (l, h).

        Récupère la liste des cellules voisines de la cellule spécifiée en parcourant la Grille et en vérifiant les voisins.

        Paramètres:
            l (int): Coordonnée en largeur.
            h (int): Coordonnée en hauteur.

        Retour:
            list[Cellule]: Liste des cellules voisines.
        """
        voisins = []
        for x in range(self.largeur):
            for y in range(self.hauteur):
                if self.dans_grille(x, y) and self.est_voisin(l, h, x, y):
                    voisins.append(self.getXY(x, y))
        return voisins

    def affecte_voisins(self):
        """
        Affecte les voisins de chaque cellule dans la grille.

        Affecte la liste des voisins pour chaque cellule dans la grille en utilisant la méthode get_voisins.

        """
        for l in range(self.largeur):
            for h in range(self.hauteur):
                self.matrix[h][l].set_voisins(self.get_voisins(l, h))

    def __str__(self) -> str:
        """
        Convertit la grille en une chaîne de caractères pour l'affichage.

        Convertit la grille en une chaîne de caractères où chaque cellule vivante est représentée par "X" et chaque cellule morte est représentée par "-".

        Retour:
            str: La représentation de la grille sous forme de chaîne de caractères.
        """
        ret = ""
        for h in self.matrix:
            ret += "\n"
            for l in h:
                ret += l.__str__()
        return ret

    def remplir_alea(self, taux:int):
        """
        Remplit la grille de manière aléatoire.

        Remplit la grille aléatoirement en fonction du taux spécifié en utilisant les méthodes naitre et mourir.

        Paramètres:
            taux (int): Le taux de remplissage en pourcentage.
        """
        for l in range(self.largeur):
            for h in range(self.hauteur):
                if randint(1, 100) <= taux:
                    self.matrix[h][l].naitre()
                else:
                    self.matrix[h][l].mourir()

    def jeu(self):
        """
        Exécute un cycle du Jeu de la Vie pour chaque cellule dans la grille.

        Exécute un cycle du Jeu de la Vie pour chaque cellule en calculant leur prochain état grâce à calcul_etat_futur.
        """
        for l in range(self.largeur):
            for h in range(self.hauteur):
                self.matrix[h][l].calcul_etat_futur()

    def actualise(self):
        """
        Met à jour l'état actuel des cellules dans la grille.

        Met à jour l'état actuel de chaque cellule dans la grille en utilisant la méthode basculer.
        """
        for l in range(self.largeur):
            for h in range(self.hauteur):
                self.matrix[h][l].basculer()


class Cellule:
    """
    Représente une cellule dans le Jeu de la Vie.

    Attributs:
        actuel (bool): L'état actuel de la cellule (vivante ou morte).
        futur (bool): L'état futur de la cellule calculé pour le prochain cycle.
        voisins (list[Cellule]): Liste des cellules voisines de la cellule.

    Méthodes:
        __init__(self)
        est_vivant(self) -> bool
        set_voisins(self, voisins: list[Cellule])
        get_voisins(self) -> list[Cellule]
        naitre(self)
        mourir(self)
        basculer(self)
        __str__(self) -> str
        calcul_etat_futur(self)
    """
    def __init__(self):
        """
        Initialise une cellule.

        Crée une cellule avec un état initial mort et sans voisins.
        """
        self.actuel = False
        self.futur = False
        self.voisins = []

    def est_vivant(self) -> bool:
        """
        Vérifie si la cellule est vivante.

        Vérifie si la cellule est dans un état vivant grâce à l'attribut actuel de la Cellule.

        Retour:
            bool: True si la cellule est vivante, sinon False.
        """
        return self.actuel

    def set_voisins(self, voisins:list):
        """
        Affecte la liste des cellules voisines à la cellule.

        Affecte la liste des cellules voisines à la cellule grâce à l'attribut voisins et l'argument du même nom.

        Paramètres:
            voisins (list[Cellule]): Liste des cellules voisines.
        """
        self.voisins = voisins

    def get_voisins(self) -> list:
        """
        Récupère la liste des cellules voisines de la cellule.

        Récupère la liste des cellules voisines de la cellule grâce à l'attribut voisins de la Cellule..

        Retour:
            list[Cellule]: Liste des cellules voisines.
        """
        return self.voisins

    def naitre(self):
        """
        Change l'état futur de la cellule pour indiquer une naissance.

        Change l'état futur de la cellule pour indiquer une naissance grâce à l'attribut futur.
        """
        self.futur = True

    def mourir(self):
        """
        Change l'état futur de la cellule pour indiquer une mort.

        Change l'état futur de la cellule pour indiquer une mort grâce à l'attribut mourir.
        """
        self.futur = False

    def basculer(self):
        """
        Passe à l'état futur de la cellule.

        Mets la valeur de l'attribut futur à l'attribut actuel.
        """
        self.actuel = self.futur

    def __str__(self) -> str:
        """
        Convertit la cellule en une chaîne de caractères pour l'affichage.

        Convertit la cellule en une chaîne de caractères où une cellule vivante est représentée par "X"et une cellule morte est représentée par "-".

        Retour:
            str: La représentation de la cellule sous forme de chaîne de caractères.
        """
        if self.est_vivant():
            return "X"
        else:
            return "-"   # Tiret du 6

    def calcul_etat_futur(self):
        """
        Calcule l'état futur de la cellule en fonction de ses voisins.

        Calcule l'état futur de la cellule en fonction du nombre de voisins vivants.
        """
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
