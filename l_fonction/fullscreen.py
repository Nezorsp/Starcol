import pygame

global largeur, hauteur
largeur, hauteur = 1280, 720

plein_ecran = False
def basculer_plein_ecran():
    global plein_ecran
    plein_ecran = not plein_ecran
    if plein_ecran:
        largeur, hauteur = 1920, 1080
        pygame.display.set_mode((largeur, hauteur), pygame.FULLSCREEN)
    else:
        largeur, hauteur = 1280, 720
        pygame.display.set_mode((largeur, hauteur))