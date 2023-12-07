from cellules import *
from time import sleep


def effacer_ecran():
    print("\u001B[H\u001B[J")


jeuDeLaVie = Grille(30,5)
jeuDeLaVie.remplir_alea(45)
jeuDeLaVie.actualise()
while True:
    jeuDeLaVie.affecte_voisins()
    jeuDeLaVie.jeu()
    jeuDeLaVie.actualise()
    print(jeuDeLaVie)
    sleep(0.5)
    effacer_ecran()