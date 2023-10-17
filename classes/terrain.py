

import pygame
from pygame.locals import *

import variables as VAR
import classes.fonctions as FCT
import classes.cellule as CCE

class CTerrain:
    def __init__(self, _moteur):
        self.MOTEUR = _moteur
        self.dimX, self.dimY = 300, 300
        self.GRILLE = FCT.GenereMat2D(self.dimX, self.dimY, CCE.CCelule(self.MOTEUR))
    
    def initialisation(self):
        pass
    
    def afficher_couche_basse(self):
        for y in range(0, self.dimY):
            for x in range(0, self.dimX):
                VAR.fenetre.blit(VAR.image["gazon"], (x * VAR.pixelBloc, y * VAR.pixelBloc) )
                #VAR.fenetre.blit(VAR.image["gazon"], (150, 150))
    
    def afficher_couche_objets(self):
        pass
    
    def afficher_couche_haute(self):
        pass