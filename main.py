from cellules import *
import os
from time import sleep


def effacer_ecran():
    """
    Efface l'écran de la console.

    Cette fonction utilise la commande système 'cls' sur Windows et 'clear' sur les systèmes Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def infini():
    """
    Exécute le Jeu de la Vie de manière infinie.

    Crée une grille de jeu, la remplit aléatoirement en fonction du taux de remplissage,
    puis met à jour et affiche la grille de manière continue dans une boucle infinie.
    """
    jeuDeLaVie = Grille(largeur, hauteur)
    jeuDeLaVie.remplir_alea(remplissage)
    jeuDeLaVie.actualise()
    while True:
        jeuDeLaVie.affecte_voisins()
        jeuDeLaVie.jeu()
        jeuDeLaVie.actualise()
        effacer_ecran()
        print(jeuDeLaVie)


def limite(lim):
    """
    Exécute le Jeu de la Vie pour un nombre limité de cycles.

    Crée une grille de jeu, la remplit aléatoirement en fonction du taux de remplissage,
    puis met à jour et affiche la grille pour un nombre spécifié de cycles.

    Paramètres:
        lim (int): Le nombre de cycles à exécuter.
    """
    jeuDeLaVie = Grille(largeur, hauteur)
    jeuDeLaVie.remplir_alea(remplissage)
    jeuDeLaVie.actualise()
    for i in range(lim):
        jeuDeLaVie.affecte_voisins()
        jeuDeLaVie.jeu()
        jeuDeLaVie.actualise()
        effacer_ecran()
        print(jeuDeLaVie)
        if i == lim-1:
            print("\nFin du Jeu la Vie, extinction du programme dans 10 secondes !\nMerci d'avoir utlisé notre programme !")
            sleep(10)


print("\n\nBienvenue sur le Jeu de la Vie en Python")

try:
    largeur = int(input("\nVeuillez choisir une largeur de cadre (par défaut 50) : "))
    print(f"Valeur entrée : {largeur}")
except ValueError:
    largeur = 50
    print(f"Valeur invalide, donc valeur de largeur par défaut : {largeur}")

try:
    hauteur = int(input("\nVeuillez choisir une hauteur de cadre (par défaut 20) : "))
    print(f"Valeur entrée : {hauteur}")
except ValueError:
    hauteur = 20
    print(f"Valeur invalide, donc valeur de hauteur par défaut : {hauteur}")

try:
    remplissage = int(input("\nVeuillez choisir un taux de remplissage en pourcentage (par défaut 25) : "))
    if 0 <= remplissage <= 100:
        print(f"Taux entré : {remplissage}")
    else:
        remplissage = 25
        print(f"Taux invalide, cela doit être compris entre 0 et 100, donc taux par défaut : {remplissage}")
except ValueError:
    remplissage = 25
    print(f"Taux invalide, donc taux par défaut : {remplissage}")

try:
    tours = int(input("\nVeuillez choisir le nombre de cycles (par défaut 200) (0 pour infini) : "))
    print(f"Valeur entrée : {tours}")
    if tours == 0:
        print("Lancement !")
        sleep(1)
        infini()
    else:
        print("Lancement !")
        sleep(1)
        limite(tours)
except ValueError:
    tours = 200
    print(f"Valeur invalide, donc nombre de tours par défaut : {tours}")
    print("Lancement !")
    sleep(1)
    limite(tours)
