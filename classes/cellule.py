

import pygame
from pygame.locals import *

import variables as VAR
import classes.fonctions as FCT


class CCelule:
    def __init__(self, _moteur):
        self.MOTEUR = _moteur
        
        self.cBasse = 0
        self.cObjet = 0
        self.cHaute = 0
        
        self.bloquer = False
        
