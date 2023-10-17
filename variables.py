from pygame.locals import *
from classes.fonctions import *


resolution = (800, 600)
fps = 60
zoom = 2
pixelBloc = 16
CLAVIER = {
    0: {"DROITE": K_d, "GAUCHE": K_q, "HAUT" : K_z, "BAS" : K_s, "ACTION1" : K_w, "ACTION2" : K_x},
    1: {"DROITE": K_RIGHT, "GAUCHE": K_LEFT, "HAUT" : K_UP, "BAS" : K_DOWN, "ACTION1" : K_l, "ACTION2" : K_m} }

urlWss = "wss://ws.ladnet.net"

music = False
fullHd = False
plein_ecran = False

web_socket_id_partie = generate_short_id()
liste_pseudos =  ["Nikou", "Bamboula", "PouetPouet", "Zigzag", "Chocolatine", "Bouffon", "Cacahuète", "Turlututu", 
                                 "Zigouigoui", "Babar", "PoufPouf", "Grincheux", "Rigolo", "Schtroumpf", "Gribouille", "Chiffon", "Cocorico", "Choucroute", "Poussin"] 


web_socket = False
fenetre = None
boucle_jeu = True
image = {}

