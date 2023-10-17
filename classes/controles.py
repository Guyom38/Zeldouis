import pygame
from pygame.locals import *

import variables as VAR

class CControles:
    def __init__(self, _moteur):
        self.MOTEUR = _moteur
    
    def gestion_clavier(self):
        for event in pygame.event.get():        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                VAR.boucle = False          
                    
        for key, values in VAR.CLAVIER.items():                            
            keys = pygame.key.get_pressed()                    
            if keys[values["GAUCHE"]] == 1:
                pass
            if keys[values["DROITE"]] == 1:
                pass
            if keys[values["HAUT"]] == 1:
                pass                    
            if keys[values["BAS"]] == 1:
                pass