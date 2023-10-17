import pygame
from pygame.locals import *

import variables as VAR

import classes.ressources as CR
import classes.controles as CC
import classes.terrain as CT
import classes.joueurs as CJS

class CMoteur:
    def __init__(self):
        self.CONTROLES = CC.CControles(self)
        self.RESSOURCES = CR.CRessources(self)
        self.TERRAIN = CT.CTerrain(self)
        self.JOUEURS = CJS.CJoueurs(self)
        
    def demarrer(self):
        pygame.init()
        VAR.fenetre = pygame.display.set_mode(VAR.resolution, pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("Zeld|ouis")
        
        self.RESSOURCES.charger()
        
        self.boucle()
    

    def boucle(self):
        horloge = pygame.time.Clock()

        VAR.boucle = True
        while VAR.boucle:           
            self.CONTROLES.gestion_clavier()

         
            VAR.fenetre.fill((16,16,16))
            
            self.TERRAIN.afficher_couche_basse()
            self.TERRAIN.afficher_couche_objets()
            self.JOUEURS.afficher()
            self.TERRAIN.afficher_couche_haute()
           
            ecriture = pygame.font.SysFont('arial', 40) 
            image_texte = ecriture.render("Hello world", True, (255,0,0)) 
            VAR.fenetre.blit(VAR.image["gazon"], (150, 150))

       
            pygame.display.update()          
            horloge.tick(VAR.fps)

        pygame.quit() 