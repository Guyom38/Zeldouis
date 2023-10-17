
import pygame
from pygame.locals import *

import variables as VAR
import classes.fonctions as FCT

class CRessources:
    def __init__(self, _moteur):
        self.MOTEUR = _moteur
        
    def charger(self):
        self.charger_images()
        self.charger_audios()
    
    def charger_images(self):
        #FCT.charger_images_zoom("decors", FCT.Findfichier"decors.png", VAR.zoom)
        VAR.image["hero"] = pygame.image.load( FCT.Findfichier("player.png") ).convert_alpha() 
        VAR.image["mechant"] = pygame.image.load( FCT.Findfichier("skeleton.png") ).convert_alpha() 
        VAR.image["monstre"] = pygame.image.load( FCT.Findfichier("slime.png") ).convert_alpha() 


        VAR.image["gazon"] = pygame.image.load( FCT.Findfichier("grass.png") ).convert_alpha() 
        VAR.image["barriere"] = pygame.image.load( FCT.Findfichier("fences.png") ).convert_alpha() 
        VAR.image["objets"] = pygame.image.load( FCT.Findfichier("objects.png") ).convert_alpha() 
        VAR.image["coffre"] = pygame.image.load( FCT.Findfichier("chest_01.png") ).convert_alpha() 
        VAR.image["coffre_or"] = pygame.image.load( FCT.Findfichier("chest_02.png") ).convert_alpha() 
        VAR.image["murs"] = pygame.image.load( FCT.Findfichier("walls.png") ).convert_alpha() 
        VAR.image["decors_gazon"] = pygame.image.load( FCT.Findfichier("decor_16x16.png") ).convert_alpha() 
        VAR.image["decors"] = pygame.image.load( FCT.Findfichier("plains.png") ).convert_alpha() 
        VAR.image["decors_eau"] = [
                pygame.image.load( FCT.Findfichier("water1.png") ).convert_alpha() ,
                pygame.image.load( FCT.Findfichier("water2.png") ).convert_alpha() ,
                pygame.image.load( FCT.Findfichier("water3.png") ).convert_alpha() ,
                pygame.image.load( FCT.Findfichier("water4.png") ).convert_alpha() ,
                pygame.image.load( FCT.Findfichier("water5.png") ).convert_alpha() ,
                pygame.image.load( FCT.Findfichier("water6.png") ).convert_alpha() ]
                
        

    def charger_audios(self):
        #VAR.sons["poser_bombe"] = pygame.mixer.Sound('audios/bomb.wav')
        pass