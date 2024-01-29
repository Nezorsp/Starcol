import pygame

from l_fonction.fullscreen import largeur, hauteur

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Starcol")

logo_image = pygame.image.load("texture/Logo_app.ico")
pygame.display.set_icon(logo_image)