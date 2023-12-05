from cellules import *
def effacer_ecran():
    print("\u001B[H\u001B[J")


jeuDeLaVie = Grille(50,50)
jeuDeLaVie.remplir_alea(75)
while True:
    jeuDeLaVie.jeu()
    jeuDeLaVie.actualise()
    jeuDeLaVie.__str__()
    effacer_ecran()
