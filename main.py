from cellules import *
from time import sleep


def effacer_ecran():
    print("\u001B[H\u001B[J")


jeuDeLaVie = Grille(100,10)
jeuDeLaVie.remplir_alea(45)
jeuDeLaVie.actualise()
print(jeuDeLaVie)



while True:
    jeuDeLaVie.jeu()
    jeuDeLaVie.actualise()
    sleep(1)
    print(jeuDeLaVie)
    effacer_ecran()